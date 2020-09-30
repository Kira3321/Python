#первое задание
a=10
b=100
c=a + b
print (a, b, c)
lol=int(input("введите целое число " ))
lal=str(input("введите слово " ))
print(lol)
print(lal)
#второе задание
Input=int(input("введите число сенкунд "))
minutes=Input // 60
second=minutes%60
hour=minutes // 60
if second >= 60:
    second//60
    minutes+=1
    print("часы:", hour, "минуты", minutes, "секунды", second)
elif second <= 60:
    second=Input
    print("часы:", hour, "минуты", minutes, "секунды", second)
elif minutes >=60:
    minutes//60
    hour+=1
    print("часы:", hour, "минуты", minutes, "секунды", second)
elif Input == 1:
    second+=1
    print("часы:", hour, "минуты", minutes, "секунды", second)
else:
    second<=60
    minutes<=60
    print("часы:",hour,"минуты",minutes,"секунды",second)
#третье задание
put=int(input("ввелите целое число "))
summa=put + (put * 11) + (put * 111)
print(summa)
#четвертое задание
v=int(input("находим самое большое  число из введенных "))
m=v%10
v=v//10
while v > 0:
    if v%10 > m:
        m = v%10
    v = v//10
    print(v)
    print(m)
print(m)
#пятое задание
var=int(input("введите выручку, целым числом "))
var1=int(input("введите убыток "))
perensumm=var - var1
if perensumm > 0:
    print("ваша прибыль ",perensumm)
    workers = int(input("укажите численность сотрудников "))
    sumworkers = perensumm / workers
    print(sumworkers)
elif perensumm == 0:
    print("вы ничего не волучили, прибыль=0, нет денег на сотрудников")
else:
    perensumm < 0
    print("ваш убыток ", perensumm, "нет денег для выплаты сотрудникам")
#шестое задание
x=2
y=3
i=1
while x < y:
    x*=1.1
    i+=1
print("кличество дней ", i, "результат ", x)
