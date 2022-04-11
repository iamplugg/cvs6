def second_task():
    a = input("Введите строки для вставки: ").split()
    c = input('Введите строку для вставки: ')
    b = int(input("Введите позицию для вставки: "))

    try:
        if a[b] in a:
            print("operation is not possible")
    except LookupError:
        a.append(c)
        print(a)