def run():
    english_words = []
    spanish_words = []

    with open('./archivos/english_words.txt', 'r') as f:
        for i in f:
            english_words.append(i)
    with open('./archivos/spanish_words.txt', 'r') as l:
        for i in l:
            spanish_words.append(i)

    



if __name__ == '__main__':
    run()