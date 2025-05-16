def names_starting_with_a(names):
    filtered_names = [name for name in names if name.lower().startswith('a')]
    return filtered_names

names = ['Ranieri', 'Amanda', 'Carlos', 'Alice']
print(names_starting_with_a(names))