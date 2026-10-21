import logging

from .student import Student
from .performance import PerformanceAnalyzer

logger = logging.getLogger(__name__)

def main() -> None:
    student1 = Student("Cyprian", [70, 80, 90])
    student2 = Student("David", [12, 45, 25])

    multiple_students = [student2, student1]

    for student in multiple_students:
        print("Name:", student.name)
        print("Average:", student.calculate_average())
        print("Passed:", student.is_passed())
        print("Grade:", student.get_grade())
        print("-" * 60)

    analyzer = PerformanceAnalyzer(multiple_students)
    print("Total students:", analyzer.count_students())
    print("Class average:", analyzer.calculate_class_average())
    print("Passed Student:", analyzer.count_passed())
    print("Failed Student:", analyzer.count_failed())
    print("Top Student:", analyzer.get_top_student())


if __name__ == "__main__":
   if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s",
    )

    logger.info("Student Performance Analyzer starting")

    main()

    logger.info("Student Performance Analyzer finished")