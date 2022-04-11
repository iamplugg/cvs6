def first_task():
    a = input("Введите строки для вставки: ").split()
    b = input('Введите строку для вставки в середину списка: ')
    n = len(a)
    i = n//2
    a.insert(i, b)
    print(a)