#2 задание
def max_el_in_list(l):
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            yield l[i]

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in max_el_in_list(my_list)]
print(new_list)
#3 задание
num = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(num)
#4 задание
def list_el (l):
    counter = {el: l.count(el) for el in l}
    print = counter
    for el in l:
        if counter[el] == 1:
            yield el
listok = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in list_el(listok)])
# 5 задание
from  functools import  reduce
def my_func (a, b):
    return  a * b
summa_numbers = [el for el in range(100, 1001)]
print(reduce(my_func, summa_numbers))
# 6 задание
from itertools import count, cycle
anti_loop = int(input("Введите число: "))
counter = 0
for i in count(anti_loop):
    if counter == anti_loop:
        break
    else:
        print(i)
        counter += 1


for i in cycle("ABC"):
    inputer = input("Для завершения нажмите 'Q', для продолжения нажмите 'Enter': ")
    print(inputer)
    if inputer != "Q" or "q":
        print(i)
    else:
        break
#никак не могу понять почему цикл не завершается.


