import random

def run():
    english_words = []
    spanish_words = []
    num_eng_words = 0
    num_esp_words = 0

    with open('./archivos/english_words.txt', 'r') as f:
        for i in f:
            english_words.append(i)
            num_eng_words += 1
    with open('./archivos/spanish_words.txt', 'r') as l:
        for i in l:
            spanish_words.append(i)
            num_esp_words += 1

    random_num = random.randint(0,num_eng_words)
    print(spanish_words[random_num])
    print(english_words[random_num])



if __name__ == '__main__':
    run()