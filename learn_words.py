import os 
import random
import time
from typing import Counter 

def borrarPantasha():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')

def get_word_user():
    word_user = input('Ingrese la palabra: ')
    # print(word_user)
    return word_user

def run():
    borrarPantasha()
    english_words = []
    spanish_words = []
    palabras_erradas = []
    num_eng_words = 0
    num_esp_words = 0
    cont = 0 

    with open('./archivos/totests.txt', 'r', encoding='utf-8') as f:
        for i in f:
            english_words.append(i.replace('\n', ''))
            num_eng_words += 1
    with open('./archivos/papruebas.txt', 'r', encoding='utf-8') as l:
        for i in l:
            spanish_words.append(i.replace('\n', ''))
            num_esp_words += 1
    while True:
        try:
             
            random_num = random.randint(0,num_eng_words - 1)

            print(english_words[random_num])
            palabra = get_word_user()

            if palabra == spanish_words[random_num]:
                print('Sí!')
                spanish_words.pop(random_num)
                english_words.pop(random_num)
                num_eng_words -= 1
            else:
                print('No')
                print(spanish_words[random_num]) 
                palabras_erradas.append(english_words[random_num])
                cont += 1
                # si no es correcta, crear una variable que guarde la palabra 
                # y la muestre al final del programa. Mostrará que palabras fueron 
                # erradas y cuantas veces se erraron


            time.sleep(0.5)
            borrarPantasha()
        except IndexError as f:
            # print('No se puele')
            continue
        if num_eng_words == 0:
            print('Acabamooos!')
            print('Erraste en las siguientes palabras: ')
            for i in palabras_erradas:
                print(i, palabras_erradas.count(i))
                pass

            time.sleep(5)
            borrarPantasha()
            break


if __name__ == '__main__':
    run()