import socket
import time

# Write a web browser
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  mysock.connect(("data.pr4e.org", 80))
except:
  print("server err")
  quit()

# Encoding the string to bytes object
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()

# encode() & b"" are equivalent

mysock.send(cmd)

# Reading data and decoding it
while True:
  data = mysock.recv(512)
  if len(data) < 1: break

  print(data.decode(), end="")

mysock.close()

# Using urllib instead
import urllib.request as url_req

uhandle = url_req.urlopen("http://data.pr4e.org/romeo.txt")

for line in uhandle:
  print(line.decode().strip())

# Computing the frequency
uhandle = url_req.urlopen("http://data.pr4e.org/romeo.txt")

counts = {}

for line in uhandle:
  words = line.decode().strip().split()

  for word in words:
    counts[word] = counts.get(word, 0) + 1

counts = sorted([(count, word) for word, count in counts.items()], reverse=True)

print(f"'{counts[0][1]}' is used {counts[0][0]} times")

# Ex 1, 2, & 5
import socket

url = input("Enter URL: ")

url = url.split("/")
url_connect = url[0]
url_req = "/".join(url)

print(url_connect, url_req)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  mysock.connect((url_connect, 80))
except:
  print("invalid url")
  mysock.close()
  quit()

req = f"GET http://{url_req} HTTP/1.0\r\n\r\n".encode()

mysock.send(req)

count = 0
data = b""

while True:
  data += mysock.recv(512)
  count += len(data)
  if count > 3000  or len(data) < 1: break

pos = data.find(b"\r\n\r\n")
data = data[pos+4:]

print(f"char count: {count}")

print(data.decode())

mysock.close()

# Ex 3
import urllib.request

url = input("Enter URL: ")

url = "http://" + url

try:
  res = urllib.request.urlopen(url)
except:
  print("invalid url")
  quit()

char_count = 0

while True:
  data = res.read(1024)
  char_count += len(data)
  if char_count > 3000 or len(data) < 1: break
  print(data.decode())

print(f"total char: {char_count}")
