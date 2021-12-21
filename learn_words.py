import os 
import random
import time

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
    palabras_erradas_english = []
    palabras_erradas_spanish = []
    num_eng_words = 0
    num_esp_words = 0
    FASHAMOS = bool

    with open('./archivos/adverbs_nouns/english_wordsAN.txt', 'r', encoding='utf-8') as f:
    # with open('./archivos/erradas_eng.txt', 'r', encoding='utf-8') as f:
        for i in f:
            english_words.append(i.replace('\n', ''))
            num_eng_words += 1
    with open('./archivos/adverbs_nouns/spanish_wordsAN.txt', 'r', encoding='utf-8') as l:
    # with open('./archivos/erradas_esp.txt', 'r', encoding='utf-8') as l:
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
                palabras_erradas_english.append(english_words[random_num])
                palabras_erradas_spanish.append(spanish_words[random_num])
                FASHAMOS = True
                with open('./archivos/erradas_eng.txt', 'w', encoding='utf-8') as e:
                    for words in palabras_erradas_english:
                        e.write(words)
                        e.write('\n')
                with open('./archivos/erradas_esp.txt', 'w', encoding='utf-8') as s:
                    for words in palabras_erradas_spanish:
                        s.write(words)
                        s.write('\n')


            time.sleep(0.5)
            borrarPantasha()
        except IndexError as f:
            # print('No se puele')
            continue
        if num_eng_words == 0:
            print('Acabamooos!')
            if FASHAMOS == True:
                print('Erraste en las siguientes palabras: ')
                for i in palabras_erradas_english:
                    err = int(palabras_erradas_english.count(i))
                    print(i, palabras_erradas_english.count(i))
                    if palabras_erradas_english.count(i) > 1:
                        for l in range(0, err):
                            palabras_erradas_english.remove(i)
            else:
                print('Felicidades!! No erraste ninguna palabra')

            time.sleep(10)
            borrarPantasha()
            break


if __name__ == '__main__':
    run()