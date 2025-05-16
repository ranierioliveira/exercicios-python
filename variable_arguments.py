def largest_number(*args):
    largest_number = args[0]
    for arg in args:
        if arg > largest_number:
            largest_number = arg
    return largest_number
        
print(largest_number(8, 5, 7, 17))