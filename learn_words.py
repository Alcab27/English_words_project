from os import PathLike
import random
import os 

def get_word_user():
    word_user = input('Ingrese la palabra: ')
    # print(word_user)
    return word_user


def run():
    english_words = []
    spanish_words = []
    num_eng_words = 0
    num_esp_words = 0

    with open('./archivos/english_words.txt', 'r', encoding='utf-8') as f:
        for i in f:
            english_words.append(i.replace('\n', ''))
            num_eng_words += 1
    with open('./archivos/spanish_words.txt', 'r', encoding='utf-8') as l:
        for i in l:
            spanish_words.append(i.replace('\n', ''))
            num_esp_words += 1

    random_num = random.randint(0,num_eng_words - 1)

    print(english_words[random_num])
    palabra = get_word_user()

    if palabra == spanish_words[random_num]:
        print('Sí!')



    # print(spanish_words[random_num]) 
    # palabras y numero que nos arroja 
    # print(str(random_num))



if __name__ == '__main__':
    run()