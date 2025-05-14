def alphabet_id(id_user):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for idx, letter in enumerate(alphabet, start = 1):
        if idx == id_user:
            return letter.upper()
    return ''
        
print(alphabet_id(10))