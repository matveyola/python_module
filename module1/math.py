import math
import time
# Documentation https://docs.python.org/3/library/math.html
"""
26) Ввести число х. Надрукувати в порядку зростання числа: sin x, cos x, ln x 
Якщо при будь-якому х деякі з виразів не мають сенсу, вивести повідомлення 
про це і порівнювати значення тільки тих, які мають сенс.
"""

# try:
#     x = float(input("Введіть число x: "))
#     sin_x = math.sin(x)
#     cos_x = math.cos(x)

#     # Перевірка, чи x > 0 для обчислення ln(x)
#     if x > 0:
#         ln_x = math.log(x)
#         # Порівняння всіх значень
#         if sin_x <= cos_x and sin_x <= ln_x:
#             print(f"sin(x): {sin_x}")
#             if cos_x <= ln_x:
#                 print(f"cos(x): {cos_x}")
#                 print(f"ln(x): {ln_x}")
#             else:
#                 print(f"ln(x): {ln_x}")
#                 print(f"cos(x): {cos_x}")
#         elif cos_x <= sin_x and cos_x <= ln_x:
#             print(f"cos(x): {cos_x}")
#             if sin_x <= ln_x:
#                 print(f"sin(x): {sin_x}")
#                 print(f"ln(x): {ln_x}")
#             else:
#                 print(f"ln(x): {ln_x}")
#                 print(f"sin(x): {sin_x}")
#         else:
#             print(f"ln(x): {ln_x}")
#             if sin_x <= cos_x:
#                 print(f"sin(x): {sin_x}")
#                 print(f"cos(x): {cos_x}")
#             else:
#                 print(f"cos(x): {cos_x}")
#                 print(f"sin(x): {sin_x}")
#     else:
#         print("ln(x) не має сенсу для x ≤ 0")
#         # Порівняння лише sin(x) і cos(x)
#         if sin_x <= cos_x:
#             print(f"sin(x): {sin_x}")
#             print(f"cos(x): {cos_x}")
#         else:
#             print(f"cos(x): {cos_x}")
#             print(f"sin(x): {sin_x}")

# except ValueError:
#     print("Введено некоректне значення, спробуйте ще раз.")




try:
    x = float(input("Введіть число x: "))
    results = []
    
    sin_x, cos_x = math.sin(x), math.cos(x)
    
    # Додавання sin(x) і cos(x) в список результатів
    results.append(('sin(x)', sin_x))
    results.append(('cos(x)', cos_x))
    
    # Перевірка чи x > 0 для обчислення ln(x)
    if x > 0:
        ln_x = math.log(x)
        results.append(('ln(x)', ln_x))
    else:
        print("ln(x) не має сенсу для x ≤ 0")
    # Сортування результатів за зростанням значень
    sorted_results = sorted(results, key=lambda pair: pair[1])
    
    # Виведення результатів
    print("Числа в порядку зростання:")
    for name, value in sorted_results:
        print(f"{name}: {round(value,3)}")
        time.sleep(3)

except ValueError:
    print("Введено некоректне значення, спробуйте ще раз.")