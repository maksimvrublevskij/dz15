n_zad = int(input("Сколько задач задали?  "))
unit_1 = set(input("Какие задачи сделал первый ученик?  ").replace(" ", ""))
unit_2 = set(input("какие задачи сделал второй ученик?  ").replace(" ", ""))
a = len(unit_1.union(unit_2))
if a <= n_zad:
    b = n_zad - len(unit_1.union(unit_2))
    print(f'осталось решить {b} задач')
else:
    print('Столько задач не задавали.')