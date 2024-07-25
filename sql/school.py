import sqlite3

conn = sqlite3.connect('school.db')

cur = conn.cursor()
cur.execute("DROP TABLE students")
cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)')
conn.commit()

print("start")
cur.execute("INSERT INTO students (name, grade) VALUES ('Anan',90)")
cur.execute("INSERT INTO students (name, grade) VALUES ('Sam',60)")
cur.execute("INSERT INTO students (name, grade) VALUES ('Bob',45)")
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)
conn.commit()

print("\nAll students that there grade is higher than 80")
cur.execute("SELECT * FROM students WHERE grade > ?", (80,))
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
print("\nafter delete")
cur.execute("DELETE FROM students WHERE name = 'Bob'")
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
print("\nafter update")
cur.execute("UPDATE students SET grade = 95 WHERE name = 'Sam'")
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)
conn.commit()

conn.close()
