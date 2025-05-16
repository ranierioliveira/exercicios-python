def dict_to_tuple(people):
   names = tuple(people.keys())
   
   for name in names:
       age = people[name]
       print(f'{name} tem {age} anos')

people = {"Ranieri": 23, "Marta": 22, "Thais": 22}
dict_to_tuple(people)

'''8. Dicionário e tupla
Descrição: Crie um dicionário com 3 pessoas e suas idades. Converta as chaves em uma tupla e imprima cada nome com sua idade no formato: Maria tem 22 anos.'''