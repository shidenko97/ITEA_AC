TODO
1. Use best async approach to load data from:
    * https://jsonplaceholder.typicode.com/posts
    * https://jsonplaceholder.typicode.com/comments
    * https://jsonplaceholder.typicode.com/albums
    * https://jsonplaceholder.typicode.com/photos
    * https://jsonplaceholder.typicode.com/todos
    * https://jsonplaceholder.typicode.com/users
2. To each user dict in users list from `https://jsonplaceholder.typicode.com/users`
join `todos`, `albums` -> `photos`, `posts` -> `comments`.
Implement best async approach.
3. Write final data to json file.
4. Write three versions of `ex_3_download_emails_serial.py`:
    * Serial
    * Processes
    * Threads

Update code in `ex_3_download_emails_serial.py` via splitting
functions for async approach.
Write time of each program execution into file.