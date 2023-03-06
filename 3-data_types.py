
#! Veri Tipleri:
# int ---> Tam Sayı
#? float ---> Ondalıklı Sayı
# str ---> "" veya '' içerisine yazılan bütün karakterler
#? bool ---> True veya False bilgisi

#! Data Types:
# int ---> Integer
#? float ---> Decimal Number
# str ---> All characters typed in "" or ''
#? bool ---> True or False info

#! Veri Tiplerine Neden İhtiyaç Duyarız:
#! Why We Need Data Types:

x = 10
y = 20
sum = x + y
print(sum)  # 30

#? Bu işlemdeki değişkenin değerlerini kullanıcıdan input ile alalım:
#? Let's get the values of the variable in this operation with input from the user:

x = input("x: ")  # input 10
y = input("y: ")  # input 20
sum = x + y
print(sum)  # 1020
print(type(sum))  # <class 'str'>

# input ile girilen karakterin tipi her zaman str, data tiplerini tanımlayarak bunu düzeltebiliriz.
# The type of character entered with the input is always str, we can fix this by defining the data types.

x = int(input("x: "))  # input 10
y = int(input("y: "))  # input 20
sum = x + y
print(sum)  # 30
print(type(sum))  # <class 'int'>


#! Tip Dönüşümü:
#! Type Conversion:

age = 24
weight = 48.7
name = 'Pakize'
isStudent = True

print(type(age))  # <class 'int'>
print(type(weight))  # <class 'float'>
print(type(name))  # <class 'str'>
print(type(isStudent))  # <class 'bool'>

#? int to float
resault = float(age)  
print(resault)  # 24.0 
print(type(resault))  # <class 'float'>

#? float to init 
resault2 = int(weight)
print(resault2)  # 48
print(type(resault2))  # <class 'int'>

#? bool to str 
resault3 = str(isStudent)
print(resault3)  # True
print(type(resault3))  # <class 'str'>

#? bool to int 
resault4 = int(isStudent)
print(resault4)  # 1
print(type(resault4))  # <class 'int'>

#? bool to float
resault5 = float(isStudent)
print(resault5)  # 1.0
print(type(resault5))  # <class 'float'>

#? int to str
resault6 = str(age)
print(resault6)  # 24
print(type(resault6))  # <class 'str'>

#? float to str
resault7 = str(weight)
print(resault7)  # 48.77
print(type(resault7))  # <class 'str'>


#! EXAMPLES:
#? 1- Daire Alanı: πr²
#?   Daire Çevresi: 2πr
#?   Yarıçapı verilen dairenin alanını ve çevresini hesaplayın:
# 1- Circle Area: πr²
#    Circle Circumference: 2πr
#    Calculate the area and perimeter of the circle given the radius:

radius = float(input('radius:'))
pi = 3.14
area = pi * (radius ** 2)
circumference = 2 * pi * radius
print("Circle Area:", area)
print("Circle Circumference:", circumference)


#? 2- mil = km / 1,609344
#?   Aracın kat ettiği mesafeyi kilometre cinsinden, mil cinsinden yazdırın:
#  2- mil = km / 1.609344
#     Print the distance traveled by the vehicle in kilometers, in miles:

km = float(input("km:"))
mil = km / 1.609344
print("mil:", mil)