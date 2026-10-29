def calculate_total(scores: list[int]) -> int:
    return sum(scores)


total: int = calculate_total([10, 25, 30])

print(total)