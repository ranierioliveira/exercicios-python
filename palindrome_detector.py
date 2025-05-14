def palindrome_detector(word):
    if word[::-1] == word:
        return True
    else:
        return False

word  = "arara"
print("A palavra " + word + " é um palíndrono? ")
print(palindrome_detector(word))