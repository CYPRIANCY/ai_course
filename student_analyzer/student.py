class Student:

    def __init__(self, name: str, scores: list[int | float]) -> None:

        if not isinstance(scores, list):
            raise TypeError("Scores must be provided as a list.")

        for score in scores:

            # Check if the score is an integer or float
            if isinstance(score, bool) or not isinstance(score, (int, float)):
                raise TypeError(
                    f"Invalid score '{score}': All scores must be numbers."
                )

            # Check if the score is within the normal 0-100 grading range
            if not (0 <= score <= 100):
                raise ValueError(
                    f"Invalid score {score}: Scores must be between 0 and 100."
                )

        self.name = name
        self.scores = scores

    def calculate_average(self) -> float:

        if self.scores == []:
            return 0.0

        average = sum(self.scores) / len(self.scores)
        return average

    def is_passed(self) -> bool:
        if self.calculate_average() >= 50:
            return True
        else:
            return False

    def get_grade(self) -> str:
        average = self.calculate_average()

        if average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "F"