#Программа для скрытия информации
print('Begin Code')
from core import Encryption, Decipher



def Unknow():
    print('Welcome unknown')
    print('Выберите действие: \n1.Написать новый текст \n2.Открыть существующий \n3.Выход')
    answer = int(input('->'))
    while answer != '':
        if answer == 1:
            pass                #New file.txt
        elif answer == 2:
            pass                #Open file.txt
        elif answer == 3:
            quit('Good Bye!')               #Function Exit
        elif str(answer) == 'exit':
            break
        else:
            print('Такого номера команды нет')
        answer = int(input('->'))



print('ProgramX started')
answer = int(input('Выберите 1.Войти 2.Создать аккаунт \n->:'))
global start_base

def Login():

    start_base = ''
    print('Вход')


#Открытие файла
    base_file_read = open('base2.txt','r')
    text = ''
    login = Encryption(input('Введите логин: \n->:'))
    for line in base_file_read:
        text = line.split(sep=".")
        while login != '':
            if str(text[0]) == str(login):
                password = Encryption(input('Введите пароль ->:'))
                if password == text[1]:
                    Unknow()
                    break
                elif str(password) == 'exit':
                    break
                else:
                    print(str(text[1]))
                    print(password)
            elif 'exit' == str(Decipher(login)):
                quit('exit')
            else:
                print('Неправильно введены данные')
            login = Encryption(input('Введите логин: \n->:'))
        start_base = start_base + line
    base_file_read.close()
    return start_base


def Signup():
    base_file_read = open('base2.txt', 'r')
    start_base = base_file_read.read()
    base_file_read.close()
    
    print('Создание нового пользователя')
    login = input('Введи логин \n->:')
    password = input('Введи пароль \n->:')
    password_two = input('Введи ещё раз пароль \n->:')
    # Запись и сохранение
    if password == password_two:
        word = str(Encryption(login)) + '.' +str(Encryption(password)) + '.'
        print(word)
        base_file_write = open('base2.txt','w')
        base_file_write.write(start_base)
        base_file_write.write('\n'+word)

        base_file_write.close()


while answer != '':
    if answer == 1:
        Login()
        break
    elif answer == 2:
        Signup()
        break
    else:
        print('Данной комманды нет')
        answer = int(input('Выберите 1.Войти 2.Создать аккаунт \n->:'))



print('End Code...')