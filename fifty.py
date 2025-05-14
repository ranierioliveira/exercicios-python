def fifty(element):
    return abs(50 - element) 

def sorted_elements(elements):
    return sorted(elements, key=fifty)


values = [60, 20, 90, 10, 55]
print(sorted_elements(values))
    
#abs retorna só o valor e ignora se é negativo