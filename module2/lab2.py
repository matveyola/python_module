"""
Зробимо функцію, яка буде перевіряти чи input є дійсним числом 
за допомогою конструкції try except
"""

def get_float(text):
    while True:
        try:
            num = float(input(text))
        except ValueError:
            print('Введіть дійсне число')
            continue
        else:
            break
    return num


"""
Зробимо функцію, яка буде перевіряти чи input є натуральним числом 
за допомогою конструкції try except
"""


def get_natural(text):
    while True:
        try:
            num = int(input(text))
        except ValueError:
            print('Введіть натуральне число')
            continue
        else:
            if num > 0:
                break
            else:
                print('Введіть натуральне число')
    return num

"""
Наступна функція служить для виконання першого завдання
"""

def task1():
    print('\n\nЛабораторна робота №2(Організація циклу за допомогою оператора for), Варіант 25')
    print('Терещенко М.В., студент групи КМ-32')
    print("\nОбчислити Σ від i = 1 до n для виразу 2^i / (x - n)")
    while True:
        x, n, sum = get_float('Введіть значення x: '), get_natural('Введіть значення n: '), 0
        if x - n == 0:  # так як на нуль ділити не можна, то одразу зробимо так, щоб в знаменнику не було нуля
            print('x не може дорівнювати n, бо тоді вираз не матиме значення')
            continue
        else:
            break
    for i in range(1, n + 1):
        sum += 2**i / (x - n)
    return f'Дана сума дорівнює {sum:.1f}'

"""
Ця функція служить для виконання другого завдання
"""

def task2():
    print(
        '\n\nЛабораторна робота №2(Організація циклу за допомогою оператора while), Варіант 25')
    print('Для чисел, що вводяться, визначити відсоток додатнихі негативних чисел. При уведенні числа − 65432 закінчити роботу.')
    print('Терещенко М.В., студент групи КМ-32')
    all, pos, neg = 0, 0, 0
    while True:
        number = get_float('Введіть число ')
        all += 1
        if number == 65432:
            if all == 1:
                return "Не було введено жодного числа"
            all -= 1
            break
        elif number > 0:
            pos += 1
        elif number < 0:
            neg += 1
    return "Відсоток додатніх чисел - {:.1f}%, а відсоток від\'ємних чисел - {:.1f}%".format(pos / all * 100, neg / all * 100)


"""
Меню для вибору завдання
"""


def choose_task():
    print("\nОрганізація циклу за допомогою оператора for(Завдання 1)")
    print("Організація циклу за допомогою оператора while(Завдання 2)")
    print("Закінчити роботу з програмою(3)")
    task = input(
        "Оберіть завдання зі списку ввівши з клавіатури номер завдання: ")
    if task == '1':
        print('\n' + task1() + '\n')
    elif task == '2':
        print('\n' + task2() + '\n')
    elif task == '3':
        return False
    else:
        print("\nВи ввели неправильний номер завдання")


"""
Цикл, який буде ідти до моменту, поки користувач не обере варіант: "Закінчити роботу з програмою"
"""
while True:
    if choose_task() is False:
        break