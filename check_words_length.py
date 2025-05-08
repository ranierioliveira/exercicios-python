def check_words_length(words):
    shortest_word = words[0]
    largest_word = words[0]
    
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(largest_word):
            largest_word = word 
    
    return f"A menor palavra da lista é {shortest_word} e a maior é {largest_word}!"

words =  ["python", "asimov", "código", "web", "programação"]
print(check_words_length(words))