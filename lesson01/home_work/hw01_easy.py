
__author__ = 'Самолетова Е.С.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

number = int(input("Введите целое число:" ))
ostatok1 = number//10
otdelenia = number%10
i=1
while ostatok1>10:
    otdelenia = ostatok1%10
    ostatok1=ostatok1//10
    print("Число", i,"начиная с последней",otdelenia)
    i=i+1
print("Начальная цифра", ostatok1, "последняя цифра", number%10)
   


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

number1 = int(input("Введите первое число" ))
number2 = int(input("Введите второе число" ))
print ("Число 1 =", ((number1+number2)-number1))
print ("Число 2 =", ((number1+number2)-number2))


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"


age = int(input("Введите ваш возраст:" ))
if age < 18 :
    print ("Извините, пользование данным ресурсом только с 18 лет")
else :
    print ("Доступ разрешен")

        
