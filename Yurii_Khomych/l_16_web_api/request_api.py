import json

import requests
from requests.auth import HTTPBasicAuth

# get_response = requests.get(
#     "http://127.0.0.1:8000/posts",
#     auth=HTTPBasicAuth('admin', '1111')
# )
# json.loads(requests.get(
#     "http://127.0.0.1:8000/users",
#     auth=HTTPBasicAuth('admin', '1111')
# ).text)

post_response = requests.put(
    "http://127.0.0.1:5000/1", data={"todos": "todo title"}
)
response = requests.get("http://127.0.0.1:5000/1")
x=1