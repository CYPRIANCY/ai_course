import logging

from .student import Student

logger = logging.getLogger(__name__)

class PerformanceAnalyzer:

    def __init__(self, students: list[Student]) -> None:
        self.students = students

    def count_students(self) -> int:
        count_student = len(self.students)

        logger.info("Counted %s students", count_student)
        
        return count_student

    def calculate_class_average(self) -> float:
        if not self.students:
            return 0.0

        total = 0.0

        for student in self.students:
            total += student.calculate_average()

        return total / len(self.students)

    def count_passed(self) -> int:
        count_pass = 0

        for student in self.students:
            if student.is_passed():
                count_pass += 1

        return count_pass

    def count_failed(self) -> int:
        count_fail = 0

        for student in self.students:
            if not student.is_passed():
                count_fail += 1

        return count_fail

    def get_top_student(self) -> str | None:
        if len(self.students) == 0:
            return None

        current_top_student = self.students[0]

        for student in self.students:
            if (
                student.calculate_average()
                > current_top_student.calculate_average()
            ):
                current_top_student = student

        return current_top_student.name