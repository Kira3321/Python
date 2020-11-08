#1 Задание
my_list = [404, 'job', True, None, [22, 11, 44]]
print(type(my_list))
my_dict = dict(aoi=21, gig=789, lal=my_list)
print(type(my_dict))
print(my_dict)
dupe = (1, 15, 13, my_list, my_dict)
print(type(dupe))
print(dupe)
#2 Задание
l = list(input("Введите числа: "))
print(l)
for el in range(0, len(l) - 1, 2):
    l[el], l[el + 1] = l[el +1], l[el]
print(l)
#3 задание
person_calendary=int(input('Ввелите месяц от 1 до 12, для определения времени года: '))
my_list=['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
month=person_calendary - 1
print(my_list[month])
my_dict= dict(Зима=(1, 2, 12), Весна=(3, 4, 5), Лето=(6, 7, 8), Осень=(9, 10, 11))
for key in my_dict.keys():
    if person_calendary in my_dict[key]:
        print(key)
#4 Задание
user_put = input("Введите слова через пробел: ").split()
for i, word in enumerate(user_put):
    print(f'{i}) {word[:10]}')
#5 Задание
number = [0]
while True:
    user_numb = input('Введите номер, составим рейтинг от 0 до 9: ')
    if user_numb == "end":
        break
    elif int(user_numb) in (1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
        user_numb = int(user_numb)
        for el in number:
            if user_numb >= el:
                el -= 1
                number.insert([el], user_numb)
                print(number)
            else:
                continue
    else:
        continue
print(number)

