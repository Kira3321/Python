# 1 задание
#try:
#    sum_input = int(input("Введите сумму кредита: "))
#    day_input = int(input("Введите дни кредита: "))
#    prossent_input = float(input("Введите процент кредита: "))
#except ZeroDivisionError:
#    print("Указывать ноль нельзя")
#def square (x, y , u):
#    """Расчет процентов по кредиту по дням"""
#    return (sum_input * prossent_input / 365) * day_input
#print(square(sum_input, day_input, prossent_input))
#2 задание
#aa = input("Введитее имя: ")
#bb = input("Введите фамилию: ")
#cc = input("Введите номер телефона: ")
#dd = input("Введите почту: ")
#ee = input("Введите город проживания: ")
#def personal_date(put_name, put_last_name, phone_nomber, mail_adres, put_city):
#    return " ".join([put_name, put_last_name, phone_nomber, mail_adres, put_city])
#print(personal_date(aa, bb, cc, dd, ee))
# #3 задание
# num_1=int(input("Введите первое число: "))
# num_2=int(input("Введите второе чило: "))
# num_3=int(input("Введиете третье число: "))
# def sum_two (z, x, c):
#     if z > c < x:
#         return z + x
#     elif z > x < c:
#         return  z + c
#     else:
#         return  x + c
# print(sum_two(num_1, num_2, num_3))
# #4 Задание
# def my_func():
#     num_1 = int(input("Введите 1 число: "))
#     num_2 = int(input("Введите 2 число: "))
#     return  num_1 ** (-num_2)
# print(my_func())
# def my_func_1():
#     num_1 = int(input("Введите 1 число: "))
#     num_2 = int(input("Введите 2 число: "))
#     num_2 -= 1
#     for i in range(num_2):
#         num_1 /= num_1
#         print(num_1)
#         print(i)
#     return num_1
# print(my_func_1())
# #5 Задание
# summa = 0
# while True:
#     put_number = input("Введите числа через пробел: ").split()
#     for i in put_number:
#         print(i)
#         print(type(i))
#         if i != 'q':
#             summa += int(i)
#             print(summa)
#         elif i == 'q':
#             print(summa)
#             break
#     """никак не могу разобраться почему не прерывается цикл
#     """
