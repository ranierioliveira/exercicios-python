def average(numbers):
    total = 0
    number_quantity = len(numbers)
    for number in numbers:
        total += number
    return total / number_quantity

numbers = [10, 20, 30, 40, 50]
print(average(numbers))
