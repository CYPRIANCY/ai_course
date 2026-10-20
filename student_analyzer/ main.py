from .student import Student
from .performance import PerformanceAnalyzer

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
    main()


# if __name__ == "__main__":
#     main()




# student1 = Student("Cyprian", [70, 80, 90])
# student2 = Student("David", [12, 45, 25])

# multiple_students = [student2, student1]

# for multiple_student in multiple_students:
#     print("Name: ", multiple_student.name)
#     print("Average: ", multiple_student.calculate_average())
#     print("Passed: ", multiple_student.is_passed())
#     print("Grade: ", multiple_student.get_grade())
#     print("-" * 60)

# class PerformanceAnalyzer:

#     def __init__(self, students):
#         self.students = students

#     def count_students(self):
#        count_student = len(self.students)
#        return count_student

#     def calculate_class_average(self):
#             if not self.students:
#                 return 0 
            
#             total = 0 

#             for student in self.students:
#                 total += student.calculate_average()
            
#             return total / len(self.students)


#     def count_passed(self):
#         count_pass = 0
#         for student in self.students:
#             if student.is_passed():
#                 count_pass += 1
#         return count_pass

#     def count_failed(self):
#         count_fail = 0
#         for student in self.students:
#             if not student.is_passed():
#                 count_fail += 1
#         return count_fail

#     def get_top_student(self):
#         if len(self.students) == 0:
#             return None

#         current_top_student = self.students[0]

#         for student in self.students:
#             if student.calculate_average() > current_top_student.calculate_average():
#                 current_top_student = student

#         return current_top_student.name


# analyzer = PerformanceAnalyzer(multiple_students)
# print("Total students:", analyzer.count_students())
# print("Class average:", analyzer.calculate_class_average())
# print("Passed Student:", analyzer.count_passed())
# print("Failed Student:", analyzer.count_failed())
# print("Top Student:", analyzer.get_top_student())student@leef-HP-All-in-One-22-df0xxx:~/Desktop/AI_course/oop/lesson15_student_analyzer$ 

