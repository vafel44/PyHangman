import random

class WordsOperations:
    def __init__(self):
        
        pass

#выбор случайного слова из списка (list_of_words) и
#возвращение выбранного слова
def select_random_word(list_of_words: list):
    return random.choice(list_of_words)

#подсчёт уникальных символов в слове
def count_unique_letters(word):
    return len(set(word))

#пользовательский ввод - вводится строка и берётся первый символ,
#если их больше
def user_input():
    return input()[:1]

#подсчёт попыток 
def count_of_attempts(attempts):
    pass

#нахождение букв (c) в слове (word) и
#возвращение их индексов (indicies)
def letter_indices(c: str, word: str):
    #явная типизация данных (c: str, word: str)
    indices = []
    #индекс буквы в слове
    #по длине слова
    for i in range(len(word)):
        if word[i] == c: 
            indices.append(i)
    return indices
        
def find_letter_in_set(c: str, unique_letters_set: set):
    if c in unique_letters_set:
        return True
    else:
        return False
    
def replace_unguessed(unguessed_list, word, replace_letter):
    indices = letter_indices(replace_letter, word)
    
    for index in indices:
        unguessed_list[index] = replace_letter
    
    return unguessed_list
        
        





