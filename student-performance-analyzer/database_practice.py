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

# Update the score for student ID 1
cursor.execute(
    "UPDATE students SET score = ? WHERE id = ?",
    (92, 1)
)

connection.commit()

print("Rows updated:", cursor.rowcount)

# Retrieve the updated student
cursor.execute(
    "SELECT * FROM students WHERE id = ?",
    (1,)
)

student = cursor.fetchone()

print("Updated student:", student)

# Delete the student whose ID is 3
cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (3,)
)

connection.commit()

print("Rows deleted:", cursor.rowcount)

# Display the remaining students
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("Remaining students:")

for student in students:
    print(student)


minimum_score = 80

cursor.execute(
    "SELECT * FROM students WHERE score > ?",
    (minimum_score,)
)

matching_students = cursor.fetchall()

print("Students scoring above", minimum_score)

for student in matching_students:
    print(student)


cursor.execute("""
    INSERT INTO students (name, age, score)
    VALUES (?, ?, ?)
""", ("Cyprian", 31, 85.5)
)
connection.commit()

cursor.execute("SELECT * FROM students")

student = cursor.fetchone()

print("First students:", student)

for student in students:
    print(student)

connection.close()