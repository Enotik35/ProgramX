#Программа для скрытия информации
from tkinter import *
import random
from tkinter import filedialog as fd

root = Tk()
token_int = random.randint(3, 7)
token = token_int

letters = {
    'a': '123',   '0': 'qwe', '[': 'vfr', 'й': 'q1we2',
    'b': '234',   '1': 'wer', ']': 'bgt', 'ф': 'w1e2r',
    'c': '345',   '2': 'ert', '{': 'nhy', 'х': 'e3rt1',
    'd': '456',   '3': 'rty', '}': 'mju', 'ц': 'q2a2z2',
    'e': '567',   '4': 'tyu', '=': 'kio', 'ч': 'w3s3x3',
    'f': '678',   '5': 'yui', ':': 'mgw', 'щ': 'riuheriu',
    'g': '789',   '6': 'uio', 'а': 'q9ke9', 'ш': 'r23',
    'h': '890',   '7': 'iop', 'б': 'l5m64l', 'ъ': 'gr3',
    'i': '901',   '8': 'opa', 'в': 'e8hg7', 'ы': 'df5',
    'j': '102',   '9': 'sdf', 'г': 'mj87bvuh9', 'ь': 'gfdht6',
    'k': '109',  '10': 'dfg', 'д': 'hgnb45', 'э': 'qwdsa3',
    'l': '210',   ' ': ' ',   'е': 'gdteb837', 'ю': 'bhnjm4',
    'm': '321',   '.': 'jvy', 'ё': 'tdgv64bnfh', 'я': 'q6g7',
    'n': '432',   ',': 'rfe', 'ж': 'dfhiug', '\n': '753159',
    'o': '543',   '!': 'qaz', 'з': 'qwyerjg',
    'p': '654',   '@': 'wsx', 'и': 'bnfgiur',
    'q': '765',   '(': 'edc', 'к': 'werrwe',
    'r': '876',   ')': 'rfv', 'л': 'ytjty',
    's': '987',   '%': 'tgb', 'м': 'revfrdeh',
    't': '780',   '$': 'yhn', 'н': 'nytdfg',
    'u': '129',   '#': 'ujm', 'о': 'uifda',
    'v': '238',   '<': 'ikl', 'п': 'noergoi',
    'w': '347',   '>': 'olp', 'р': 'uo[ptpotykop',
    'x': '453',   '+': 'zaq', 'с': 'infdbnkjbg',
    'y': '562',   '-': 'xsw', 'т': 'ewuyfihiu',
    'z': '671',   '/': 'cde', 'у': 'oeru9pmcfviobm',
}


def clean():
    elments = root.grid_slaves()
    for l in elments:
        l.grid_forget()

# Encryption core


def encryption(word):
    global token
    value = ''
    while token != 0:
        word = word.lower()
        for letter in word:     # Цикл количество повторений которго равно буквам в слове
            if letter in letters:
                value = value + str(letters[letter])+','
        token -= 1
    return value


def decipher(word):
    global token
    new_word = ''
    while token != 0:
        text = word.split(sep=',')
        for value in text:
            for letter in letters:
                if str(value) == str(letters[letter]):
                    new_word = new_word + str(letter)
        token -= 1
    return new_word

old_text = ''

titles = []

def Unknow(login):
    def Newfile():
        def Exitmenu():
            clean()

            Name_profile.grid(row=0, column=0, columnspan=2)
            Openfile_btn.grid(row=1, column=0)
            Newfile_btn.grid(row=1, column=1)
            Profile_exit_btn.grid(row=1, column=2)

        def Createfile():
            global titles
            title = str(Text_entry.get())

            titles.append(title)
            file = open('{1}file{0}.txt'.format(title, login), 'x')
            file.close()
            new_text = str(Tittle.get(1.0, END))
            file = open('{1}file{0}.txt'.format(title, login), 'r+')

            file.write(str(encryption(new_text)))
            Exitmenu()

        clean()

        Name_file = Label(text='Введите название файла', bg='silver', fg='green')
        Text_entry = Entry(bg='silver', fg='red')
        Tittle = Text(bg='silver', fg='red')
        Newfile_exit_btn = Button(text='Выход', bg='silver', fg='blue', command=Exitmenu)
        Newfile_create_btn = Button(text='Создать', bg='silver', fg='blue', command=Createfile)

        Name_file.grid(row=0, column=0)
        Text_entry.grid(row=0, column=2, columnspan=2)
        Tittle.grid(row=1, column=0, columnspan=3)
        Newfile_exit_btn.grid(row=2, column=3)
        Newfile_create_btn.grid(row=2, column=0)

    def Openfile():

        def Open():
            filename = fd.askopenfilename()
            print(filename)
            global old_text
            title = filename
            try:
                with open(title) as file_handler:
                    for line in file_handler:
                        text = line.split(sep=' ')
                        for word in text:
                            new_text = decipher(word)
                            old_text = old_text + ' ' + new_text
                Text_open.insert(INSERT, '{}'.format(old_text))
            except IOError:
                pass

        def Exitmenu():
            clean()

            Name_profile.grid(row=0, column=0, columnspan=2)
            Openfile_btn.grid(row=1, column=0)
            Newfile_btn.grid(row=1, column=1)
            Profile_exit_btn.grid(row=1, column=2)

        Open_file_listbox = Listbox()
        for titl in titles:
            Open_file_listbox.insert(0, titl)

        Newfile_exit_btn = Button(text='Выход', bg='silver', fg='blue', command=Exitmenu)
        Open_file_btn = Button(text='Открыть файл', bg='silver', fg='blue', command=Open)
        Text_open = Text(root, bg='silver', fg='red')

        clean()

        Open_file_listbox.grid(row=1, column=0)
        Open_file_btn.grid(row=2, column=0)
        Newfile_exit_btn.grid(row=2, column=3)
        Text_open.grid(row=1, column=1, columnspan=3)

    def Exit():
        clean()

        Name.grid(row=0, column=0, columnspan=2)
        Password.grid(row=1, column=0, columnspan=2)
        Login_btn.grid(row=2, column=1)
        Signup_btn.grid(row=2, column=4)
        Name_entry.grid(row=0, column=2, columnspan=4, pady=10, padx=10)
        Password_entry.grid(row=1, column=2, columnspan=4, pady=10, padx=10)

    Name_profile = Label(text='*_* {0}'.format(login), bg='silver', fg='red')
    Openfile_btn = Button(text='Открыть файл', bg='silver', fg='blue', command=Openfile)
    Newfile_btn = Button(text='Создать файл', bg='silver', fg='blue', command=Newfile)
    Profile_exit_btn = Button(text='Выход', bg='silver', fg='blue', command=Exit)

    clean()

    Name_profile.grid(row=0, column=0, columnspan=2)
    Openfile_btn.grid(row=1, column=0)
    Newfile_btn.grid(row=1, column=1)
    Profile_exit_btn.grid(row=1, column=2)

global start_base
def Login():
    global token
    # Открытие файла
    try:
        base_file_read = open('base2.txt', 'r')
    except IOError:
        print('ОШИБКА: Нет базы')
    login = encryption(str(Name_entry.get()))
    for line in base_file_read:
        text = line.split(sep=".")
        if str(text[0]) == str(login):
            password = encryption(str(Password_entry.get()))
            if password == text[1]:
                token = int(decipher(text[2]))
                profile = decipher(login)
                Unknow(profile)
                break
            else:
                break
    base_file_read.close()


def Signup():
    base_file_read = open('base2.txt', 'r')
    start_base = base_file_read.read()
    base_file_read.close()
    clean()
    def Sign():
        password = Password_entry.get()
        password_two = Password2_entry.get()
        login = Name_entry.get()
        if password == password_two:
            print(login, password, token_int)
            word = str(encryption(login)) + '.' + str(encryption(password)) + '.'+ str(encryption(str(token_int))) + '.'
            base_file_write = open('base2.txt', 'w')
            base_file_write.write(start_base)
            base_file_write.write('\n' + word)
            Unknow(login)
            base_file_write.close()

    def Exit():
        clean()

        Name.grid(row=0, column=0, columnspan=2)
        Name_entry.grid(row=0, column=2, columnspan=4, pady=10, padx=10)
        Password.grid(row=1, column=0, columnspan=2)
        Password_entry.grid(row=1, column=2, pady=10, padx=10, columnspan=4)
        Login_btn.grid(row=2, column=1)
        Signup_btn.grid(row=2, column=4)


    Exit_btn = Button(text='Выход', bg='silver', fg='blue', command=Exit)
    Registration_btn = Button(text='Зарегистрироваться', bg='silver', fg='blue', command=Sign)
    Name_entry.grid(row=0, column=2, columnspan=4, pady=10, padx=10)
    Password_entry.grid(row=1, column=2, pady=10, padx=10, columnspan=4)
    Name_signup.grid(row=0, column=0, columnspan=2)
    Password_signup.grid(row=1, column=0, columnspan=2)
    Password2_signup.grid(row=2, column=0, columnspan=2)
    Password2_entry.grid(row=2, column=2, pady=10, padx=10, columnspan=4)
    Registration_btn.grid(row=3, column=1)
    Exit_btn.grid(row=3, column=4)


# Запись и сохранение
Name_signup = Label(text='Введите ваше имя', bg='silver', fg='green')
Password_signup = Label(text='Введите ваш пароль', bg='silver', fg='green')
Password2_signup = Label(text='Повторно введите пароль', bg='silver', fg='green')
Password2_entry = Entry(bg='silver', fg='red')

# Создать ткинтер

root.resizable(width=False, height=False)
# root.iconbitmap(r'\favicon.ico')
root.title('ProgramX')
root.configure(background='silver')
# NAME | LOGIN
Name = Label(text='Имя', bg='silver', fg='green')
Name.grid(row=0, column=0, columnspan=2)
Name_entry = Entry(bg='silver', fg='red')
Name_entry.grid(row=0, column=2, columnspan=4, pady=10, padx=10)
# PASSWORD
Password = Label(text='Пароль', bg='silver', fg='green')
Password.grid(row=1, column=0, columnspan=2)
Password_entry = Entry(bg='silver', fg='red')
Password_entry.grid(row=1, column=2, pady=10, padx=10, columnspan=4)
# BUTTON`S
Login_btn = Button(text='Войти', bg='silver', fg='blue', command=Login)
Login_btn.grid(row=2, column=1)
Signup_btn = Button(text='Регистрация', bg='silver', fg='blue', command=Signup)
Signup_btn.grid(row=2, column=4)


root.mainloop()
