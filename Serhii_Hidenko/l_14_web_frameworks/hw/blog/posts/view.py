from flask import Blueprint, request, redirect, current_app, url_for
from flask import render_template
from flask_security import login_required

from blog import db
from blog.posts.models import Post, Tag, Comment
from blog.posts.forms import PostForm, TagForm, CommentForm

posts = Blueprint('posts', __name__, template_folder='templates')


# http://localhost/blog/create
@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('posts.index'))
    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/<slug>/edit/', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)


@posts.route('/')
def index():
    q = request.args.get('q')

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
    else:
        posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=2)
    return render_template('posts/index.html', pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    tags = post.tags
    comments = post.comments
    form = CommentForm()
    return render_template('posts/post_detail.html', post=post, tags=tags,
                           comments=comments, form=form)


# http://localhost/blog/tag/python
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)


@posts.route('/create-tag', methods=['POST', 'GET'])
@login_required
def create_tag():
    if request.method == 'POST':
        name = request.form['name']

        tag = Tag(name=name)
        db.session.add(tag)
        db.session.commit()

        return redirect(url_for('posts.index'))
    form = TagForm()
    return render_template('posts/create_tag.html', form=form)


@posts.route('/<slug>/edit-tag/', methods=['POST', 'GET'])
@login_required
def edit_tag(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()

    if request.method == 'POST':
        form = TagForm(formdata=request.form, obj=tag)
        form.populate_obj(tag)
        db.session.commit()

        return redirect(url_for('posts.index'))

    form = TagForm(obj=tag)
    return render_template('posts/edit_tag.html', tag=tag, form=form)


@posts.route('/like-post/<slug>', methods=['GET'])
@login_required
def like_post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()

    post.like_count += 1
    db.session.commit()

    return redirect(url_for('posts.post_detail', slug=post.slug))


@posts.route('/dislike-post/<slug>', methods=['GET'])
@login_required
def dislike_post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()

    post.dislike_count += 1
    db.session.commit()

    return redirect(url_for('posts.post_detail', slug=post.slug))


@posts.route('/comment/<slug>/', methods=['POST'])
@login_required
def comment(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()

    form = CommentForm(formdata=request.form)

    if form.validate():
        current_app.logger.exception('Something wrong')
        comment = Comment(post_id=post.id, name=form.name.data,
                          text=form.text.data)
        db.session.add(comment)
        db.session.commit()

    return redirect(url_for('posts.post_detail', slug=post.slug))
