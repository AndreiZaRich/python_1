numbers = [1, 2, 3, 5, 8, 15, 23, 38]

even_squares = [(num, num ** 2) for num in numbers if num % 2 == 0]

print(even_squares)