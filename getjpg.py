# import socket
# from time import sleep

# HOST = "data.pr4e.org"
# PORT = 80

# img_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try:
#   img_socket.connect((HOST, PORT))
# except:
#   print("server err")
#   quit()

# # sendall is high level implementation of the send method
# img_socket.sendall(b"GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n")

# # Total bytes of data
# t_count = 0

# # Picture in binary
# picture = b""

# while True:
#   data = img_socket.recv(512)
#   if len(data) < 1: break
#   # Using this to slow down our program
#   # sleep(0.25)
#   picture += data
#   t_count += len(data)
#   print(len(data))

# # Find header end
# pos = picture.find(b"\r\n\r\n")
# print("Headers\r\n", picture[:pos].decode())

# # Remove the headers
# picture = picture[pos+4:]

# # Create a file
# with open("./src/stuff.jpg", "wb") as f:
#   f.write(picture)

# f.close()

# print("file close: ", f.closed)


# Using urllib instead
import urllib.request as url_req

img = url_req.urlopen(
    "https://www.google.com/logos/doodles/2021/tim-berglings-32nd-birthday-6753651837109058.7-l.png")

f_size = 0
img_handle = open("./src/googleimg.jpg", "wb")

while True:
  info = img.read(1024)
  if len(info) < 1: break
  f_size += len(info)

  if img_handle.writable: img_handle.write(info)
  else: 
    print("file write err")
    img_handle.close()
    quit()
    
print(f_size, "copying complete.")

img_handle.close()
