import requests

# pip install requests
response1 = requests.get("http://localhost:8888")
response2 = requests.put("http://localhost:8888")
response3 = requests.post("http://localhost:8888")
response4 = requests.delete("http://localhost:8888")
response5 = requests.head("http://localhost:8888")
