import json
import sqlite3

con = sqlite3.connect("./db/rosterdb")
cur = con.cursor()

cur.executescript("""
  DROP TABLE IF EXISTS User;
  DROP TABLE IF EXISTS Course;
  DROP TABLE IF EXISTS Member;
  DROP TABLE IF EXISTS TeacherOrNot;

  CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
  );

  CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
  );

  CREATE TABLE TeacherOrNot (
    id INTEGER PRIMARY KEY UNIQUE,
    type TEXT UNIQUE
  );

  CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
  );

  INSERT INTO TeacherOrNot (id, type) VALUES (0, \"Student\");
  INSERT INTO TeacherOrNot (id, type) VALUES (1, \"Teacher\");
""")

fname = input("Enter file name: ")

if len(fname) < 1: fname = "roster_sample.json"

data = open(f"./db/{fname}", "r")
json_data = json.loads(data.read())

# Every 5th loop, commit (save sql file) {write to the disk}
commit_number = 0

for entry in json_data:

  user_name = entry["name"]
  course_title = entry["course"]
  user_role = entry["role"]

  # print((user_name, course_title, user_role))

  # One student 
  cur.execute("INSERT OR IGNORE INTO User (name) VALUES (?)", (user_name,))

  cur.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)", (course_title,))

  # Select user id
  cur.execute("SELECT id FROM User WHERE name = ?", (user_name,))

  user_id = cur.fetchone()[0]

  # Select course id
  cur.execute("SELECT id FROM Course WHERE title = ?", (course_title,))

  course_id = cur.fetchone()[0]

  cur.execute("INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)", (user_id, course_id, user_role))

  if commit_number % 5 == 0: con.commit()

print("Execution Complete!")

join_query = """
  SELECT User.name AS \"Name\", Course.title AS \"Course\", TeacherOrNot.type AS \"Member\" 
  FROM User JOIN Member JOIN Course JOIN TeacherOrNot 
  ON Member.user_id = User.id AND Member.course_id = Course.id AND Member.role = TeacherOrNot.id 
  ORDER BY \"Course\", \"Member\" DESC, \"Name\";
"""

for row in cur.execute(join_query):
  print(str(row[0]), str(row[1]), str(row[2]))

data.close()
con.close()
