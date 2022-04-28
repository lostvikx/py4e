import urllib3

# Always create an instance of PoolManager
http = urllib3.PoolManager()

# This is super simple
res = http.request("GET", "https://httpbin.org/ip")

post_res = http.request(
  "POST",
  "https://httpbin.org/post",
  fields={
    "hello": "world"
  }
)

print(res.status)
# 200
print(res.data)  # Can use .decode()
# b'{\n  "origin": "132.154.104.201"\n}\n'
print(res.headers)
# HTTPHeaderDict({"Content-Length": "32", ...})

