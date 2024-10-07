import data
import os
import words_operations as wor
import messages as msg

class GameCore:
    
    def __init__(self):
        self.state = 1
        #буква, введённая пользователем
        self.p_letter = None

        #список слов, который задаётся в файле data.py
        self.list_of_words = data.themes.get('NatureRU')
        
        #случайно выбранное слово из списка 
        self.random_word = wor.select_random_word(self.list_of_words)

        self.rm_len = len(self.random_word)

        #количество попыток из уникальных букв в слове
        self.attempts = wor.count_unique_letters(self.random_word)

        #генерация списка отгаданных/неотгаданных букв и преобразование его к строке
        self.unguessed_list = ["_"] * self.rm_len #generate array with "_"
        self.unguessed_string = "  ".join(self.unguessed_list) #generate string from array with "_"

    def game_start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(msg.msg_dict.get("Hello"))
        print(msg.msg_dict.get("Guess").format(self.rm_len))
        print(msg.msg_dict.get("Antogonize1"))

        self.game_cycle() 

    def game_cycle(self):
            
        while self.attempts != 0:
            print(self.check_win())
            if self.state == 0:
                break
                        
            print(msg.msg_dict.get('Input1'))
            self.p_letter = wor.user_input()[:1]
            letter_in_word = wor.find_letter_in_set(self.p_letter, self.random_word) 
            
            os.system('cls' if os.name == 'nt' else 'clear')

            if letter_in_word:
                print(msg.msg_dict.get('Correct'))
                self.unguessed_list = wor.replace_unguessed(self.unguessed_list, self.random_word, self.p_letter)    

            elif not letter_in_word:
                print(msg.msg_dict.get('Incorrect'))
                self.attempts -= 1

            print(" ".join(self.unguessed_list))

    def check_win(self):
        
        if "_" not in self.unguessed_list:
            self.state = 0
            return msg.msg_dict.get('Win')
            
        elif self.attempts == 0:
            self.state = 0
            return msg.msg_dict.get('Lose').format(self.random_word)

        else:
            return msg.msg_dict.get('AttemptsLeft').format(self.attempts)