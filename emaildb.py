import sqlite3

con = sqlite3.connect("./db/emaildb")
cur = con.cursor()

# If a table name Counts exists delete it.
cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (email TEXT, count INTEGER)")

file_name = input("Enter file name: ")

# The mbox file
if len(file_name) < 1: file_name = "mbox-short.txt"

f_handle = open(f"./src/{file_name}")

# Every 5th loop, commit (save sql file) {write to the disk}
commit_number = 0

for line in f_handle:

  commit_number += 1

  if not line.startswith("From: "): continue

  line = line.strip().split()

  email_id = line[1]

  # Execute SQL Query
  # Use this to prevent an sql injection
  cur.execute("SELECT count FROM Counts WHERE email=:email_id", {"email_id": email_id})

  # This fetches the first result from the previous SELECT query.
  row = cur.fetchone()

  # If none insert, else update.
  if row is None:
    cur.execute("INSERT INTO Counts (email, count) VALUES (:email_id, 1)", {"email_id": email_id})
  else:
    cur.execute("UPDATE Counts SET count = count + 1 WHERE email=?", (email_id,))

  if commit_number % 5 == 0: con.commit()

# Top 10 highest frequencies.
select_query = "SELECT * FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(select_query):
  print(row[0], row[1])

f_handle.close()
con.close()