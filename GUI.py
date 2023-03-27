import os
from pathlib import Path
import easygui as g

def start(fileName):
    checking = False
    fileObj = Path(fileName)
    checking = fileObj.is_file()
    fin = []
    if checking == False:
        list1 = ["ФИО", "Кабинет(номер)", "Принтер(принтер, МФУ, копир)", "Устройство(ПК, ноутбук, моноблок)", "Организация"]
        fin = g.multenterbox("Введите ФИО, номер кабинета, тип принтера(Принтер, МФУ, Копир), устройство(ПК, Ноутбук, Моноблок) и организацию",title = 'Ввод данных о пользователе',fields = (list1), )
        if fin is None:
            fin = ['None', 'None', 'None', 'None', 'None']
        else:
            try:
                os.mkdir("C:\Program Files\ConfigNKU")
            except Exception:
                Exception
            with open(fileName, "w") as file:
                    print("\n".join(map(str, fin)), file=file)
    else:
        fileopen = open(fileName, 'r')
        for line in fileopen:
            fin.append(line.rstrip('\n'))
        if len(fin) == 4:
            list2 = ["Организация"]
            fin2 = g.multenterbox("Введите Организацию",title = 'Ввод данных о пользователе',fields = (list2), )
            if fin2 is None:
                fin.append('None')
            else:
                fin.append(fin2[0])
            with open(fileName, "w") as file:
                    print("\n".join(map(str, fin)), file=file)
    return fin