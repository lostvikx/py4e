import urllib3
import re

print("Welcome To HTML Link Scraper")

url = input("Enter: ")

if not url.startswith("http://") and not url.startswith("https://"): 
  url = "https://" + url

# instantiate new PoolManager
http = urllib3.PoolManager()

# Response Object
res = http.request(
  "GET", 
  url,
  preload_content=False
)

# Print Status
print(f"status code: {res.status}")

# Streaming contents
chunk_count = 0
html = b""

# 16-bits or 2-bytes
for chunk in res.stream(512):
  chunk_count += len(chunk)
  html += chunk

# Use this to release the http connection back to the connetion pool so that it can be re-used.
res.release_conn()

# List of links
links = re.findall(b"href=\"(http[s]?://.+?)\"", html)

for link in links:
  print(link.decode())

print(f"bytes received: {chunk_count}")