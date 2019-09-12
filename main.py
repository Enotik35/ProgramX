#Программа для скрытия информации

from tkinter import *

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

# Encryption core
def Encryption(word):
    word = word.lower()
    value = ''
    for letter in word:     # Цикл количество повторений которго равно буквам в слове
        if letter in letters:
            value = value + str(letters[letter])+','
    return value

def Decipher(word):
    new_word = ''
    text = word.split(sep=',')
    for value in text:
        for letter in letters:
            if str(value) == str(letters[letter]):
                new_word = new_word + str(letter)
    return new_word

old_text = ''

def Admin():
    pass

def Unknow(login, n, obj1=None, obj2=None, obj3=None, obj4=None, obj5=None, obj6=None):
    def Newfile():
        def Exitmenu():
            Name_file.grid_forget()
            Text_entry.grid_forget()
            Tittle.grid_forget()
            Newfile_exit_btn.grid_forget()
            Newfile_create_btn.grid_forget()

            Name_profile.grid(row=0, column=0, columnspan=2)
            Openfile_btn.grid(row=1, column=0)
            Newfile_btn.grid(row=1, column=1)
            Profile_exit_btn.grid(row=1, column=2)

        def Createfile():
            title = str(Text_entry.get())
            file = open('{1}file{0}.txt'.format(title, login), 'x')
            file.close()
            new_text = str(Tittle.get(1.0, END))
            file = open('{1}file{0}.txt'.format(title, login), 'r+')

            file.write(str(Encryption(Encryption(Encryption(new_text)))))
            Exitmenu()

        Name_profile.grid_forget()
        Openfile_btn.grid_forget()
        Newfile_btn.grid_forget()
        Profile_exit_btn.grid_forget()

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
            global old_text
            title = Text_entry.get()
            try:
                with open('{1}file{0}.txt'.format(title, login)) as file_handler:
                    for line in file_handler:
                        text = line.split(sep=' ')
                        for word in text:
                            new_text = Decipher(Decipher(Decipher(word)))
                            old_text = old_text + ' ' + new_text
                Text_open.insert(INSERT, '{}'.format(old_text))
            except IOError:
                pass

        def Exitmenu():
            Name_file.grid_forget()
            Text_entry.grid_forget()
            Open_file_btn.grid_forget()
            Newfile_exit_btn.grid_forget()
            Text_open.grid_forget()

            Name_profile.grid(row=0, column=0, columnspan=2)
            Openfile_btn.grid(row=1, column=0)
            Newfile_btn.grid(row=1, column=1)
            Profile_exit_btn.grid(row=1, column=2)

        Newfile_exit_btn = Button(text='Выход', bg='silver', fg='blue', command=Exitmenu)
        Name_file = Label(text='Введите название файла', bg='silver', fg='green')
        Text_entry = Entry(bg='silver', fg='red')
        Open_file_btn = Button(text='Открыть файл', bg='silver', fg='blue', command=Open)
        Text_open = Text(root, bg='silver', fg='red')

        Name_profile.grid_forget()
        Openfile_btn.grid_forget()
        Newfile_btn.grid_forget()
        Profile_exit_btn.grid_forget()

        Name_file.grid(row=0, column=0)
        Text_entry.grid(row=0, column=2)
        Open_file_btn.grid(row=2, column=0)
        Newfile_exit_btn.grid(row=2, column=3)
        Text_open.grid(row=1, column=0, columnspan=3)

    def Exit():
        Name_profile.grid_forget()
        Openfile_btn.grid_forget()
        Newfile_btn.grid_forget()
        Profile_exit_btn.grid_forget()

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

    if n == 0:

        Name.grid_forget()
        Password.grid_forget()
        Login_btn.grid_forget()
        Signup_btn.grid_forget()
        Name_entry.grid_forget()
        Password_entry.grid_forget()

        Name_profile.grid(row=0, column=0, columnspan=2)
        Openfile_btn.grid(row=1, column=0)
        Newfile_btn.grid(row=1, column=1)
        Profile_exit_btn.grid(row=1, column=2)

    if n == 1:

        Name_entry.grid_forget()
        Password_entry.grid_forget()
        obj1.grid_forget()
        obj2.grid_forget()
        obj3.grid_forget()
        obj4.grid_forget()
        obj5.grid_forget()
        obj6.grid_forget()

        Name_profile.grid(row=0, column=0, columnspan=2)
        Openfile_btn.grid(row=1, column=0)
        Newfile_btn.grid(row=1, column=1)
        Profile_exit_btn.grid(row=1, column=2)

global start_base

def Login():
    #   Открытие файла
    base_file_read = open('base2.txt', 'r')
    login = Encryption(Encryption(Encryption(str(Name_entry.get()))))
    for line in base_file_read:
        text = line.split(sep=".")
        if str(text[0]) == str(login):
            password = Encryption(Encryption(Encryption(str(Password_entry.get()))))
            if password == text[1]:
                profile = Decipher(Decipher(Decipher(login)))
                n = 0
                Unknow(profile, n)
                break
            else:
                break
    base_file_read.close()


def Signup():
    base_file_read = open('base2.txt', 'r')
    start_base = base_file_read.read()
    base_file_read.close()

    def Sign():
        password = Password_entry.get()
        password_two = Password2_entry.get()
        login = Name_entry.get()
        if password == password_two:
            word = str(Encryption(Encryption(Encryption(login)))) + '.' + str(Encryption(Encryption(Encryption(password)))) + '.'
            base_file_write = open('base2.txt', 'w')
            base_file_write.write(start_base)
            base_file_write.write('\n' + word)
            n = 1
            Unknow(login, n, Name_signup, Password_signup, Password2_signup, Exit_btn, Registration_btn, Password2_entry)
            base_file_write.close()

    def Exit():
        Name_signup.grid_forget()
        Password_signup.grid_forget()
        Password2_signup.grid_forget()
        Password2_entry.grid_forget()
        Registration_btn.grid_forget()
        Exit_btn.grid_forget()

        Name.grid(row=0, column=0, columnspan=2)
        Password.grid(row=1, column=0, columnspan=2)
        Login_btn.grid(row=2, column=1)
        Signup_btn.grid(row=2, column=4)


    Name_signup = Label(text='Введите ваше имя', bg='silver', fg='green')
    Password_signup = Label(text='Введите ваш пароль', bg='silver', fg='green')
    Password2_signup = Label(text='Повторно введите пароль', bg='silver', fg='green')
    Exit_btn = Button(text='Выход', bg='silver', fg='blue', command=Exit)
    Registration_btn = Button(text='Зарегистрироваться', bg='silver', fg='blue', command=Sign)
    Password2_entry = Entry(bg='silver', fg='red')


    Name.grid_forget()
    Password.grid_forget()
    Login_btn.grid_forget()
    Signup_btn.grid_forget()



    Name_signup.grid(row=0, column=0, columnspan=2)
    Password_signup.grid(row=1, column=0, columnspan=2)
    Password2_signup.grid(row=2, column=0, columnspan=2)
    Password2_entry.grid(row=2, column=2, pady=10, padx=10, columnspan=4)
    Registration_btn.grid(row=3, column=1)
    Exit_btn.grid(row=3, column=4)

    # Запись и сохранение

#Создать ткинтер
root = Tk()
root.resizable(width=False, height=False)
root.iconbitmap(r'D:\canvas\ProgramX\favicon.ico')
root.title('ProgramX')
root.configure(background='silver')

#NAME | LOGIN
Name = Label(text='Имя', bg='silver', fg='green')
Name.grid(row=0, column=0, columnspan=2)

Name_entry = Entry(bg='silver', fg='red')
Name_entry.grid(row=0, column=2, columnspan=4, pady=10, padx=10)


#PASSWORD
Password = Label(text='Пароль', bg='silver', fg='green')
Password.grid(row=1, column=0, columnspan=2)

Password_entry = Entry(bg='silver', fg='red')
Password_entry.grid(row=1, column=2, pady=10, padx=10, columnspan=4)


#BUTTON`S
Login_btn = Button(text='Войти', bg='silver', fg='blue', command=Login)
Login_btn.grid(row=2, column=1)

Signup_btn = Button(text='Регистрация', bg='silver', fg='blue', command=Signup)
Signup_btn.grid(row=2, column=4)



root.mainloop()
