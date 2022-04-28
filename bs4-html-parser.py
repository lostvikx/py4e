from bs4 import BeautifulSoup
import urllib3

print("Welcome To BS4 Link Parser")

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

for chunk in res.stream(1024):
  chunk_count += len(chunk)
  html += chunk

soup = BeautifulSoup(html, "html.parser")

# Use this to release the http connection back to the connetion pool so that it can be re-used.
res.release_conn()

# Find all anchor tags
a_tags = soup.find_all("a")

for tag in a_tags:
  print(f"TAG: {tag}")
  print("URL: %s" % tag.get("href"))
  print(f"Attrs: {tag.attrs}")
  print("\n")

print(f"bytes received: {chunk_count}")


# Find all p tags
p_tags = soup.find_all("p")

print("p tags: %d" % len(p_tags))
