import requests

res = requests.get("http://127.0.0.1:3000/search?city=kyiv")

print(res.json())

