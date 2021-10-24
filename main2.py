import os
import shutil
from sets import *



print("Файловый менеджер: \n" 
      "1.Создать папку \n"
      "2.Удалить папку \n"
      "3.Переместиться \n"
      "4.Вернуться в рабочую директорию \n"
      "5.Создать текстовый файл \n"
      "6.Записать текст в файл \n"
      "7.Посмотреть содержимое файла \n"
      "8.Удалить файл \n"
      "9.Скопировать файл в другую папку \n"
      "10.Переместить файл \n"
      "11.Переименовать файл")

request = ''

while request != 'end':
    request = input()



    if  request == "1":
        name = input()
        new_path = f"{direct}/{name}".format(name=name)
        os.mkdir(new_path)

    elif request == "2":
        try:
            name = input()
            dirrr = f"{direct}/{name}"
            os.rmdir(dirrr)
        except OSError:
            askk = input("Вы уверены, что хотите удалить непустую папку?: ")
            if askk == 'да':
                shutil.rmtree(dirrr)
                print("Готово!")
            else:
                os.chdir(direct)
                print(os.getcwd())


    elif request == "3":
        name = input()
        dirrr = f"{direct}/{name}"
        os.chdir(dirrr)
        print(os.getcwd())



    elif request == "4":
        os.chdir("/Users/Aram/Downloads/fileman")
        print(os.getcwd())

    elif request == "17":
        print(os.listdir(f"{os.getcwd()}"))

    elif request == "5":
        name = input('Имя файла:')
        open(name,'w')
        print(os.getcwd())


    elif request == "6":
        name = str(input('Файл: '))
        f = open(name,'w')
        f.write(input())
        f.close()

    elif request == "7":
        name = str(input())
        f = open(name)
        print(f.read())

    elif request == "8":
        name = input()
        os.remove(name)
        print("Готово!")



    elif request == "9":
        papka = input("Папка, из которой копируем: ")
        name = input('Файл: ')
        ppapka = input("Папка, в которую копируем: ")
        shutil.copy(f"{direct}/{papka}/{name}",f"{direct}/{ppapka}")

    elif request == "10":
        cur_kat = os.getcwd()
        naming = input('Файл: ')
        ppapkka = input("Папка, в которую перемещаем: ")
        os.replace(f"{cur_kat}/{naming}", f"{direct}/{ppapkka}/{naming}")

    elif request == "11":
        naming = input('Файл: ')
        new_name = input('Новое название: ')
        os.rename(f"{direct}/{naming}", f"{direct}/{new_name}")