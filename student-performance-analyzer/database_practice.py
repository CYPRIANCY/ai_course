import sqlite3


def create_connection(db_path: str = "students.db") -> sqlite3.Connection:
    connection = sqlite3.connect(db_path)
    return connection


def create_table(db_path: str = "students.db") -> None:
    connection = create_connection(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            score REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def get_students(db_path: str = "students.db",) -> list[tuple[int, str, int, float]]:
    connection = create_connection(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    return students

def add_student(name: str, age: int, score: float, db_path: str = "students.db") -> None:
    if not name.strip():
        raise ValueError("Student name cannot be empty.")

    if age <= 0:
        raise ValueError("Age must be greater than zero.")

    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    connection = create_connection(db_path)

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO students (name, age, score)
            VALUES (?, ?, ?)
            """,
            (name.strip(), age, score)
        )

        connection.commit()
        print("Student added successfully.")

    finally:
        connection.close()

def update_student_score(student_id: int, new_score: float, db_path: str = "students.db") -> bool:
    if not 0 <= new_score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    connection = create_connection(db_path)

    try:
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE students SET score = ? WHERE id = ?",
            (new_score, student_id)
        )

        connection.commit()

        return cursor.rowcount > 0

    finally:
        connection.close()

def delete_student(student_id: int, db_path: str = "students.db") -> bool:
    connection = create_connection(db_path)

    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )
        connection.commit()

        return cursor.rowcount > 0

    finally:
        connection.close()

if __name__ == "__main__":
    create_table()

    try:
        updated = update_student_score(11, 98.0)

        if updated:
            print("Student score updated successfully.")
        else:
            print("Student not found.")

    except ValueError as error:
        print("Validation error:", error)
    
    deleted = delete_student(student_id=13)

    if deleted:
        print("Student deleted successfully.")
    else:
        print("Student not found.")

    students = get_students()

    print("Students in database:")

    for student in students:
        print(student)