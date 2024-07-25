import sqlite3


class Students:

    def __init__(self):
        self.conn = sqlite3.connect('school.db')
        self.cur = self.conn.cursor()

    def create_new_table(self):
        self.cur.execute("DROP TABLE students")
        self.cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)')
        self.conn.commit()

    def insert_new_student(self, name, grade):
        self.cur.execute("INSERT INTO students (name, grade) VALUES (?,?)", (name, grade))
        self.conn.commit()

    def get_student_with_garde_above(self, grade):
        self.cur.execute("SELECT * FROM students WHERE grade > ?", (grade,))
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

        self.conn.commit()

    def delete_student_by_name(self, name):
        self.cur.execute(f"DELETE FROM students WHERE name = {name}")
        self.conn.commit()

    def update_grade_for_student_by_name(self, name):
        self.cur.execute(f"DELETE FROM students WHERE name = {name}")