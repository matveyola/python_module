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


def get_non_negative_float(text):
    while True:
        num = get_float(text)
        if num >= 0:
            return num
        else:
            print('Введіть невід\'ємне число')
            continue

print(get_float("Enter float value: "))