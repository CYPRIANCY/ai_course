import os
import tempfile
import unittest

from database_practice import (
    add_student,
    create_table,
    delete_student,
    get_students,
    update_student_score,
)


class TestDatabasePractice(unittest.TestCase):

    def setUp(self) -> None:
        # Create a temporary database file for each test.
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.db_path = temp_file.name
        temp_file.close()

        # Create the students table in the temporary database.
        create_table(self.db_path)

    def tearDown(self) -> None:
        # Remove the temporary database after each test.
        os.unlink(self.db_path)

    def test_add_student(self) -> None:
        add_student("Test Student", 20, 85.0, self.db_path)

        students = get_students(self.db_path)

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0][1], "Test Student")
        self.assertEqual(students[0][2], 20)
        self.assertEqual(students[0][3], 85.0)

    def test_update_student_score(self) -> None:
        add_student("Test Student", 20, 85.0, self.db_path)
        students = get_students(self.db_path)
        student_id = students[0][0]

        updated = update_student_score(
            student_id, 95.0, self.db_path
        )

        self.assertTrue(updated)
        self.assertEqual(get_students(self.db_path)[0][3], 95.0)

    def test_update_nonexistent_student(self) -> None:
        updated = update_student_score(999, 75.0, self.db_path)

        self.assertFalse(updated)

    def test_delete_student(self) -> None:
        add_student("Test Student", 20, 85.0, self.db_path)
        student_id = get_students(self.db_path)[0][0]

        deleted = delete_student(student_id, self.db_path)

        self.assertTrue(deleted)
        self.assertEqual(get_students(self.db_path), [])

    def test_delete_nonexistent_student(self) -> None:
        deleted = delete_student(999, self.db_path)

        self.assertFalse(deleted)

    def test_reject_invalid_score(self) -> None:
        with self.assertRaises(ValueError):
            add_student("Test Student", 20, 150.0, self.db_path)


if __name__ == "__main__":
    unittest.main()