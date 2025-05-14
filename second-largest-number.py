def second_largest_number(numbers):
    numbers.sort()
    return numbers[-2]

numbers = [32, 10, 58, 30, 55, 12, 28, 51]
print(second_largest_number(numbers))

#list.sort() function modifies the list and returns none
#sorted(list) function returns a new sorted list
