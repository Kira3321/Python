# 1 задание
my_list = [404, 'job', True, None, [22, 11, 44]]
print(type(my_list))
my_dict = dict(aoi=21, gig=789, lal=my_list)
print(type(my_dict))
print(my_dict)
dupe = (1, 15, 13, my_list, my_dict)
print(type(dupe))
print(dupe)
# 2 задание
my_list = [14, 23, 21, 99, 88]
print(len(my_list))
#3 задание
person_calendary=int(input('Ввелите месяц от 1 до 12, для определения времени года: '))
my_list=['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
month=person_calendary - 1
print(my_list[month])
my_dict= dict(Зима=(1, 2, 12), Весна=(3, 4, 5), Лето=(6, 7, 8), Осень=(9, 10, 11))
for key in my_dict.keys():
    if person_calendary in my_dict[key]:
        print(key)

