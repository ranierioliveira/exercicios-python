def fruts(fruts_list):
    fruts_list.append('banana')
    fruts_list[1] = 'maçã'
    
    if 'laranja' in fruts_list:
        fruts_list.remove('laranja')
    
    return sorted(fruts_list, key=str.lower)
    #key=str.lower ignora se é maiúscula ou minúscula

print(fruts(['abacaxi', 'limão', 'laranja', 'abacate']))