from colorama import Fore, Back, Style

class color:
    name = str(input("Здравствуйте!Пожалуйста введите ваше имя:"))
    year = int(input("А так же введите пожалуйста ваш возраст:"))
    if year <= 6:
        print(Fore.YELLOW, name, "В данный момент вы учитесь в садике!\n")
        if year <= 6:
            print(Back.BLACK, "В следуещем году вы пойдёте в школу!")
    elif year <= 10:
        print(Fore.CYAN, name, "Вы сейчас в младших классах!\n")
        if year == 10:
            print(Back.BLACK, " В следуещем году вы будете в средних классах!\n")
    elif year <= 15:
        print(Fore.GREEN, name, "В данный момент вы в средних классах!\n")
    elif year <= 17:
        print(Fore.RED, name, "Вы в старших классах!\n")
        if year == 17:
            print(Back.BLACK, "В этом году вы закончите школу!")