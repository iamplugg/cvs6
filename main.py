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
def first_task():
    a = input("Введите строки для вставки: ").split()
    b = input('Введите строку для вставки в середину списка: ')
    n = len(a)
    i = n//2
    a.insert(i, b)
    print(a)
