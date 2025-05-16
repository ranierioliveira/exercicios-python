def names_not_starting_with_a(names):
    '''Returns just names that do not start with the letter A'''
    filtered_names = []
    for name in names:
        if name.lower().startswith('a'):
            continue
        filtered_names.append(name)
    return filtered_names

names = ['Ranieri', 'Amanda', 'Carlos', 'Alice']
print(names_not_starting_with_a(names))

