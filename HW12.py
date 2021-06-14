import collections

filename = input('Введите название файла (например, Pride_and_Prejudice.txt): ')  # 'Pride_and_Prejudice.txt'


def get_words(filename):
    with open(filename, encoding='utf-8') as f:
        t = f.read()
        trash = ',./ ?(){}[]=+><!@#$%^&*:;"_`~|-\—1234567890«»'
        text = t.split()
        words = []
        for word in text:
            word = word.strip(trash).lower()
            if len(word) > 0:
                words.append(word)
    return words


def words_ED(words):
    words = get_words(filename)
    cnt = collections.Counter()
    for word in words:
        if word.endswith('ed'):
            cnt[word] += 1
    return cnt


def ED_y(words):
    words = get_words(filename)
    cnt_y = collections.Counter()
    for word in words:
        if word.endswith('ied'):
            cnt_y[word] += 1
    return cnt_y


def main():
    words = get_words(filename)
    a = len(words_ED(words))
    b = len(ED_y(words))
    print('Количество форм на -ed:', a)
    print('Из них образованы от глаголов на -y:', b)
    print('Остальные образованы от глаголов на -е:', a - b)


if __name__ == '__main__':
    main()
