def is_alphanumeric(user_prompt):
    counter = 0
    for char in user_prompt:
        if char.isalnum():
            counter += 1
    return counter

user_prompt = input("Digite alguma coisa: ")
print(is_alphanumeric(user_prompt))