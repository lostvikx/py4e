# file_name = input("Enter file name: ")

# try:
#   fhandle = open(f"./src/{file_name}", "r")
# except:
#   print("file open err")
#   quit()

# for line in fhandle:
#   line = line.strip()
#   words = line.split()

#   # IndexError
#   if words[0] == "From": print(line)

#   # This works
#   if line.startswith("From"): print(line)

# fhandle.close()

with open('./src/mbox-short.txt', 'r') as f:
  res = [line.strip() for line in f if line.strip().startswith('From')]

print(res)