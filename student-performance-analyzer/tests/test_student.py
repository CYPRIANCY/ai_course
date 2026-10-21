import unittest
from unittest.mock import Mock

from student_analyzer.student import Student
from student_analyzer.performance import PerformanceAnalyzer

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Test Student", [70, 80, 90])

    def test_calculate_average(self):
        self.assertEqual(self.student.calculate_average(), 80.0)

        student2 = Student("Another Student", [20, 40])
        self.assertEqual(student2.calculate_average(), 30.0)

    def test_empty_scores(self):
        # Pass an empty list [] as the scores argument
        student = Student("Empty Student", [])
        # Check that an empty score list returns 0
        self.assertEqual(student.calculate_average(), 0)

    def test_invalid_score(self):
        # Start a student with valid scores first
        student = Student("Test Student", [70, 80, 90])
        
        # Check that an invalid score (120) raises ValueError
        with self.assertRaises(ValueError):
            Student("Test", [120])  # Note: Change 'add_score' if your method has a different name

        # Check that a Boolean value is rejected as a score
        with self.assertRaises(TypeError):
            Student("Test", [True])
    
    def test_is_passed(self):
        # TODO: Create a student with average 80
        # Assert that is_passed() returns True
        student = Student("Alice", [80, 80, 80])
        self.assertTrue(student.is_passed())

    def test_get_grade(self):
        # TODO: Create a student with average 65
        # Assert that get_grade() returns "B"
        student = Student("Bob", [60, 70])  # Average is 65
        self.assertEqual(student.get_grade(), "B")

    def test_text_score_raises_type_error(self):
        # TODO: Assert that creating a student with ["hello", 80] raises TypeError
        with self.assertRaises(TypeError):
            Student("Charlie", ["hello", 80])
    
    def test_scores_must_be_list(self):
        with self.assertRaises(TypeError):
            Student("Alice", "70, 80, 90")

    def test_get_grade_a(self):
        student = Student("Alice", [70, 70, 70])
        self.assertEqual(student.get_grade(), "A")

    def test_get_grade_c(self):
        student = Student("Bob", [50, 50, 50])
        self.assertEqual(student.get_grade(), "C")

    def test_get_grade_f(self):
        student = Student("Charlie", [40, 40, 40])
        self.assertEqual(student.get_grade(), "F")

class TestPerformanceAnalyzer(unittest.TestCase):

    def setUp(self):
        self.student1 = Student("Cyprian", [70, 80, 90])
        self.student2 = Student("David", [12, 45, 25])

        self.analyzer = PerformanceAnalyzer(
            [self.student1, self.student2]
        )

    def test_count_students(self):
        self.assertEqual(self.analyzer.count_students(), 2)

    def test_count_passed(self):
        self.assertEqual(self.analyzer.count_passed(), 1)

    def test_count_failed(self):
        self.assertEqual(self.analyzer.count_failed(), 1)

    def test_get_top_student(self):
        self.assertEqual(self.analyzer.get_top_student(), "Cyprian")
    
    def test_empty_class_count(self):
        analyzer = PerformanceAnalyzer([])
        self.assertEqual(analyzer.count_students(), 0)

    def test_empty_class_average(self):
        analyzer = PerformanceAnalyzer([])
        self.assertEqual(analyzer.calculate_class_average(), 0)
    
    def test_empty_class_top_student(self):
        analyzer = PerformanceAnalyzer([])
        self.assertIsNone(analyzer.get_top_student())

    def test_equal_average_top_student(self):
        student1 = Student("Alice", [70, 80])
        student2 = Student("Bob", [60, 90])

        analyzer = PerformanceAnalyzer([student1, student2])

        self.assertEqual(analyzer.get_top_student(), "Alice")
    
    def test_calculate_class_average(self):
        student1 = Student("Alice", [70, 80])
        student2 = Student("Bob", [60, 90])

        analyzer = PerformanceAnalyzer([student1, student2])

        self.assertEqual(analyzer.calculate_class_average(), 75.0)
    
    def test_later_student_becomes_top_student(self):
        student1 = Student("Alice", [50, 60])
        student2 = Student("Bob", [90, 100])

        analyzer = PerformanceAnalyzer([student1, student2])

        self.assertEqual(analyzer.get_top_student(), "Bob")
    
    def test_count_passed_with_mocks(self):
        from unittest.mock import Mock

        student1 = Mock()
        student1.is_passed.return_value = True

        student2 = Mock()
        student2.is_passed.return_value = False

        student3 = Mock()
        student3.is_passed.return_value = True

        analyzer = PerformanceAnalyzer(
            [student1, student2, student3]
        )

        self.assertEqual(analyzer.count_passed(), 2)

if __name__ == "__main__":
    unittest.main()
