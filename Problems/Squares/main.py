def sq_sum(*numbers):
    squares = [number ** 2 for number in numbers]
    return sum(squares)
