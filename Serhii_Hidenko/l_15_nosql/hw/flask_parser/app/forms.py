from wtforms import Form, FileField
from wtforms.validators import DataRequired


class FileForm(Form):
    """Form for uploading json file with insights"""

    file = FileField('File to parse', validators=[DataRequired])
