from asyncio import sleep
import time
import os
import json
import csv
def udalitjson():
    savename = input()
    try:
        os.remove(f"{savename}.json")
        print(f"Сохранение '{savename}' удалено.")
    except FileNotFoundError:
        print(f"Сохранение '{savename}' не найдено.")

def zagruzjson(savename):
    try:
        with open(f"{savename}.json", "r") as file:
            game_data = json.load(file)
            print(f"Сохранение '{savename}' загружено.")
    except FileNotFoundError:
        print(f"Сохранение '{savename}' не загружено.")

def line ():
    print ("----------------------------------------------------------------------------------------------------------------------------")
def cohec ():
    time.sleep (1.2)
    print ("...1...")
    time.sleep (1.5)
    print ("...2...")
    time.sleep (1.5)
    print ("...3...")
    time.sleep (1.5)
def timer():
    time.sleep (1)
def smilik ():
    smil = "\u263A"
    print (smil)

def chetverti():
    cohec()
    line()
    print("\'Потеря времени\'")
    timer()
    print("Спустя долгое бездействие тебе стало скучно, из-за чего ты и уснул\nК сожалению, тебе не удолось дожить до 4 утра")
    line()
    print("Хотите сохраниться?\n1.да\n2.нет")
    ser = input()
    if ser == "1":
        with open('output.json', 'w') as file:
            json.dump(data, file, indent=4)
        with open('output.csv', 'a', newline='') as file:
            fieldnames = ['name', 'inventar']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    elif ser == "2":
        exit()
    else:
        print("Нужно вводить номер варианта ответа")
        exit()
def pit ():
    print ("ты долго блуждал по темной роще. Она казалась нескончаемой.\nУ тебя кончались силы, но и время поджимало\n1. Остановитmся\n2. Продолжить путь".capitalize())
    dsa = input()
    timer ()
    if (dsa =="1"):
        chetverti()
    elif (dsa =="2"):
        print ("ура! Наконец то перед тобой показались верхушки крестов - это церковь\nТы знал то, как проводить изгание.\nЗакончив ритуал, ты заметил, что свечки не погасли\nХотя ты их точно тушил...\n1. Затушить\n2. Оставить все как есть, вдруг это знак?".capitalize())
        htr = input()
        timer ()
        if (htr =="1"):
            print ("Вдруг на улице резко пошел дождь. Взошло солнце\nТы знал, что это хороший знак\nДобравшись до дома, ты наконец- то уснул")
            cohec ()
            line()
            print ("\'Долгожданный конец\'")
            timer ()
            print ("Это конец. задание выполнено!\nНо на долго ли?")
            line ()
            timer ()
            print ("Спасибо за прохождение игры!\nСохранить игру?\n1.да\n2.нет")
            sder = input()
            if sder == "1":
                with open('output.json','w') as file:
                    json.dump(data,file,indent=4)
                with open('output.csv', 'a',newline='')as file:
                    fieldnames = ['name','inventar']
                    writer = csv.DictWriter(file,fieldnames=fieldnames)
                    writer.writeheader()
                    for row in data:
                        writer.writerow(row)
            elif sder == "2":
                print("Пока")
                exit()
            person.clear()
            inventar.clear()
            line ()
            smilik()
            print("\n")
        elif (htr == "2"):
            cohec()
            line ()
            print ("\'Последняя надежда\'")
            timer()
            print ("Лишь свечи удерживали ее в этом мире.\nКак жаль, что твои труды были напрасны")
            line ()
            exit()
        else:
            print ("Нужно вводить номер варианта ответа")
            exit()
    else:
        print ("Нужно вводить номер варианта ответа")
        exit()
def tretii (inventar):
    print ("Забешавши в ванну, ты обнаружил, что там никого нет\nПора выдвигаться\n1. Спуститься в подвал\n2. Пока что подождать здесь")
    timer()
    inventar["inventar2"]=" свечи"
    inventar["inventar3"] = " крест"
    inventar["inventar4"] = " святая вода"
    line ()
    print ("Твой инвентарь: " + inventar["inventar"]+inventar["inventar2"]+inventar["inventar3"]+inventar["inventar4"])
    line ()
    ase = input ()
    timer ()
    if (ase == "1"):
        print ("Ты спустился в подвал, ведь там был запасной выход.\n1. Выйти на улицу\n2. Вернутся в дом и переждать")
        ryt = input()
        timer ()
        if (ryt =="1"):
            pit ()
        elif (ryt == "2"):
            chetverti()
        else:
            print ("Нужно вводить номер варианта ответа")
            exit()
    elif (ase == "2"):
        chetverti()
    else:
        print ("Нужно вводить номер варианта ответа")
        exit()
def six (data):
    print ("Пройдя длинные неизвестные коридоры, тебе удалось отыскать ванну.\nОднако ты заметил кое чтоЮ что мешало продолжить путь. \nА именно большой топор, который был воткнут в дверь и, видимо, не единожды\n1. Вытащить топор и резко забежать в ванную\n2. Пока что не заходить")
    wer = input ()
    timer ()
    if (wer == "1"):
        tretii (inventar)
    elif (wer == "2") :
        print ("Ты развернулся и тут же увидел ее\nУродливая улыбка, широко распахнутые глаза.\nПохоже ты попался\n1. Забежать в ванну\n2. Попробовать заговорить с ней")
        gse = input()
        timer ()
        if (gse == "1"):
            tretii(inventar)
        elif (gse == "2"):
            print ("Ты попытался что то промямлить.\nОна улыбнулась. Самое время\n1. Бежать к выходу\n2. Застыть на месте")
            yrt = input()
            timer()
            if (yrt == "1"):
                cohec()
                line()
                print("\'Лабиринт\'")
                timer()
                print("Убегая от нее, ты заблудился в собственном доме.\nБлуждая уже 12 день, ты снова наткнулся на нее\nВ этот раз убежать не удалось")
                line()
                print("Хотите сохраниться?\n1.да\n2.нет")
                ser = input()
                if ser == "1":
                    with open('output.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    with open('output.csv', 'a', newline='') as file:
                        fieldnames = ['name', 'inventar']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        for row in data:
                            writer.writerow(row)
                elif ser == "2":
                    exit()
                else:
                    print("Нужно вводить номер варианта ответа")
                    exit()
            elif (yrt == "2"):
                cohec()
                line ()
                print ("\'Ошибка\'")
                timer()
                print ("Было глупо просто стоять на месте, она же не слепая")
                line ()
                print("Хотите сохраниться?\n1.да\n2.нет")
                ser = input()
                if ser == "1":
                    with open('output.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    with open('output.csv', 'a', newline='') as file:
                        fieldnames = ['name', 'inventar']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        for row in data:
                            writer.writerow(row)
                    exit()
                elif ser == "2":
                    exit()
                else:
                    print("Нужно вводить номер варианта ответа")
                    exit()
            else:
                print ("Нужно вводить номер варианта ответа")
                exit()
        else:
            print ("Нужно вводить номер варианта ответа")
            exit()
    else:
        print ("Нужно вводить номер варианта ответа")
        exit()
def samiiperv ():
    print ("Вернувшись назад, от темного коридора не осталось и следа.\nПродолжая блуждать, ты совсем потерялся. Что делать дальше?\n1. Стоять на месте\n2. Продолжать блуждать")
    fad = input()
    timer ()
    if (fad == "1"):
        chetverti()
    elif (fad == "2"):
        vtoroe ()
    else:
        print ("Нужно вводить номер варианта ответа")
        exit()
def vtoroe ():
    print ("ура! Ты нашел потайную комнату\nПо крайней мере ты здесь никогда не бывал\nЗабавно путешествовать по своему дому и не знать, что ждет тебя дальше\n1. Вернутся в темный коридор\n2. Подняться на 2 этаж")
    ref = input()
    timer ()
    if (ref == "1"):
        samiiperv()
    elif (ref == "2"):
        print ("Узкие проходы привели тебя к лестнице\nТы неспешно поднялся\n1. Остаться на 2 этаже.\n2. Вернутся в коридор")
        der = input()
        timer ()
        if (der== "1"):
            print ("Кажется твой дом был намного уютнее, чем сейчас\nОна портила его своим присутствием\nДва часа ночи. Время поджимает.\nНеобходимо срочно добраться до ванной.О! Шкаф!\n1. Спуститься на первый этаж и искать ванную там\n2. Искать ванную на 2 этаже\n3. Открыть шкаф")
            rek = input()
            timer ()
            if (rek=="1"):
                cohec ()
                line ()
                print ("\'Только вперед\'")
                timer ()
                print ("Времени мало, пути назад нет")
                line()
                print("Хотите сохраниться?\n1.да\n2.нет")
                ser = input()
                if ser == "1":
                    with open('output.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    with open('output.csv', 'a', newline='') as file:
                        fieldnames = ['name', 'inventar']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        for row in data:
                            writer.writerow(row)
                elif ser == "2":
                    exit()
                else:
                    print("Нужно вводить номер варианта ответа")
                    exit()
            elif (rek == "2"):
                six(inventar)
            elif (rek == "3"):
                print ("Ты медленно подходишь к шкафу..")
                timer ()
                print ("Вы точно хотите открыть его?\n1.Да\n2.Нет")
                fsd = input ()
                timer()
                if (fsd == "1"):
                    cohec()
                    line ()
                    print ("\'Ты никогда не смотрел хороры?\'")
                    timer ()
                    print ("Самое глупое в этой ситуации. Она следила за тобой")
                    line ()
                    print("Хотите сохраниться?\n1.да\n2.нет")
                    ser = input()
                    if ser == "1":
                        with open('output.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        with open('output.csv', 'a', newline='') as file:
                            fieldnames = ['name', 'inventar']
                            writer = csv.DictWriter(file, fieldnames=fieldnames)
                            writer.writeheader()
                            for row in data:
                                writer.writerow(row)
                    elif ser == "2":
                        exit()
                    else:
                        print("Нужно вводить номер варианта ответа")
                        exit()
                elif (fsd == "2"):
                    cohec()
                    line ()
                    print ("\'Умное решение! Но слишком поздно\'")
                    timer ()
                    print ("Она следила за тобой! Как только ты отвернулся от шкафа,она выпрыгнула на тебя")
                    line ()
                    print("Хотите сохраниться?\n1.да\n2.нет")
                    ser = input()
                    if ser == "1":
                        with open('output.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        with open('output.csv', 'a', newline='') as file:
                            fieldnames = ['name', 'inventar']
                            writer = csv.DictWriter(file, fieldnames=fieldnames)
                            writer.writeheader()
                            for row in data:
                                writer.writerow(row)
                    elif ser == "2":
                        exit()
                    else:
                        print("Нужно вводить номер варианта ответа")
                        exit()
                else:
                    print ("Нужно вводить номер варианта ответа")
                    exit()
            else:
                print ("Нужно вводить номер варианта ответа")
                exit()
        elif (der == "2"):
            samiiperv()
    else:
        print ("Нужно вводить номер варианта ответа")
        exit()
while True :
    name = input('\nВведите свой ник!')
    inventar = {"inventar": "подушка"}
    with open('output.csv', 'a', newline='') as file:
        writer = csv.writer(file)
    data = [
        {"name": name, "inventar": inventar}
    ]
    with open('output.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Меню:\n1.Начать игру\n2.Настройки сохранения\n3.Закончить игру")
    gtg = input()
    if gtg == "1":
        person = {"name": name}
        print("Привет, " +person["name"].capitalize() + "\nТвой инвентарь: " + inventar["inventar"])
        line()
        timer()
        print("Цель: Каждый год к тебе в дом приходит странная женщина\nКак только это происходит начинается игра\nТвоя задача выжить и изгнать ее до 4 утра\nВ противном случае она не уйдет никогда\nДля выхода из игры нажми 4 ")
        timer()
        print("\nТы проснулся ночью и почувствовал чей то взгляд на себе\nВзглянув на дверь ты увидел пару светящихся глаз в темноте\n\'" + (name).capitalize() + "\'- послышалось в темноте\nТы знаешь, что она пришла за тобой\nИгра началась!\n1. Лучше остаться в кровати\n2. Покинуть комнату")
        vfer = input()
        timer()
        if (vfer == "1"):
            cohec()
            line()
            print("\'Гляделки\'")
            timer()
            print("Ее глаза никогда не потухнут, в отличии от твоих\nТы позволил себе закрыть глаза на пару секунд, но этого было достаточно чтобы она забрала их у тебя навсегда")
            line()
            print("Хотите сохраниться?\n1.да\n2.нет")
            ser = input()
            if ser == "1":
                with open('output.json', 'w') as file:
                    json.dump(data, file, indent=4)
                with open('output.csv', 'a', newline='') as file:
                    fieldnames = ['name', 'inventar']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in data:
                        writer.writerow(row)
            elif ser == "2":
                exit()
            else:
                print("Нужно вводить номер варианта ответа")
                exit()
        elif (vfer == "2"):
            print("Ты не оглядываясь шагнул в темноту и через время оказался в коридоре\nПозади послышался шум\n1. Вернуться назад\n2. Продолжать идти")
            vfe = input()
            timer()
            if (vfe == '1'):
                print("Возвращаясь назад, ты не узнавал свой дом\nКажется с каждым его проходом дом меняет форму и окрас\nВот например куда ведет этот поворот?\nКто тебя там ждет?\n1. Вернутся обратно в коридор\n2. Продолжить идти")
                vf = input()
                timer()
                if (vf == "1"):
                    samiiperv()
                elif (vf == "2"):
                    vtoroe()
                else:
                    print("Нужно вводить номер варианта ответа")
                    exit()
            elif vfe == "2":
                vtoroe()
            else:
                print("Нужно вводить номер варианта ответа")
                exit()
        elif vfer == "4":
            exit()
        else:
            print("Нужно вводить номер варианта ответа")
            exit()
    elif gtg == "2":
        print("1.Загрузить сохранение\n2.Удалить сохранение")
        gtga = input ()
        if gtga == "1":
            print("Напишите название сохранения")
            savename = input ()
            zagruzjson(savename)
        elif gtga == "2":
            print("Напишите название сохранения")
            udalitjson()
        else:
            print("Нужно вводить  1 или 2")
    elif gtg == "3":
        text = "игра завершена!"
        exit()
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
        exit()



