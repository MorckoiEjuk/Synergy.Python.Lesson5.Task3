inv = int(input("Минимальная сумма инвестиций - "))
mike = int(input("У Майкла долларов - "))
ivan = int(input("У Ивана долларов - "))

if (mike >= inv) and (ivan >= inv):
    print("2")
elif (mike >= inv) and (ivan < inv):
    print("Mike")
elif (mike < inv) and (ivan >= inv):
    print("Ivan")
elif (mike < inv) and (ivan < inv) and (mike + ivan >= inv):
    print("1")
else:
    print("0")
input("Нажмите ENTER чтобы закрыть программу")