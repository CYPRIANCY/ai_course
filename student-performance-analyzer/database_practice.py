import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        score REAL NOT NULL
    )
""")

cursor.execute("""
    INSERT INTO students (name, age, score)
    VALUES (?, ?, ?)
""", ("Cyprian", 31, 85.5)
)
connection.commit()

cursor.execute("SELECT * FROM students")

student = cursor.fetchone()

print("First students:", student)

# for student in students:
#     print(student)

connection.close()