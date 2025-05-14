import random

def password_generator():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_characters = ['%', '&', '$', '#', '@', '!', '#', ')', ')', '(', '*']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    elements = []
    
    elements.append(random.choice(alphabet))
    elements.append(random.choice(alphabet))
    elements.append(random.choice(alphabet).upper())
    elements.append(random.choice(alphabet).upper())
    elements.append(str(random.choice(numbers)))
    elements.append(str(random.choice(numbers)))
    elements.append(random.choice(special_characters))
    elements.append(random.choice(special_characters))
    random.shuffle(elements)
    password = ''.join(elements)
    return password
    
print(password_generator())

