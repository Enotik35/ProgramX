
letters = {
    'a': 123,   '0': 'qwe',
    'b': 234,   '1': 'wer',
    'c': 345,   '2': 'ert',
    'd': 456,   '3': 'rty',
    'e': 567,   '4': 'tyu',
    'f': 678,   '5': 'yui',
    'g': 789,   '6': 'uio',
    'h': 890,   '7': 'iop',
    'i': 901,   '8': 'opa',
    'j': 102,   '9': 'sdf',
    'k': 109,   '10': 'dfg',
    'l': 210,
    'm': 321,
    'n': 432,
    'o': 543,
    'p': 654,
    'q': 765,
    'r': 876,
    's': 987,
    't': 780,
    'u': 129,
    'v': 238,
    'w': 347,
    'x': 453,
    'y': 562,
    'z': 671,
}

#Encryption core

text = 'Aider'.lower()


def Encryption(word):
    value = ''

    for letter in word: # Цикл количество повторений которго равно буквам в слове
        if letter in letters:
            value = value + str(letters[letter])+',' # Для каждой буквы есть ее значение в словаре

    return value

#



def Decipher(word):
    new_word = ''
    text = word.split(sep=',')
    for value in text:
        for letter in letters:
            if str(value) == str(letters[letter]):
                new_word = new_word + str(letter)
    return new_word

