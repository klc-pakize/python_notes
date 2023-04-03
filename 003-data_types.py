
#! Numerik Veri Tipleri:
#  int ---> Tam Sayı
#? float ---> Ondalıklı Sayı
#  str ---> "" veya '' içerisine yazılan bütün karakterler
#? bool ---> True veya False bilgisi
#  complex ---> a+bj olarak ifade edilen hemen hemen hiç kullanılmaz.

#! Numeric Data Types:
#  int ---> Integer
#? float ---> Decimal Number
#  str ---> All characters typed in "" or ''
#? bool ---> True or False info
#  complex ---> Expressed as a+bj is almost never used.

#! Veri Tiplerine Neden İhtiyaç Duyarız:
#! Why We Need Data Types:

x = 10
y = 20
sum = x + y
print(sum)  # 30
print(type(sum))  # int

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

#! Python Numaraları
#? Python'da üç sayısal tür vardır: | There are three numeric types in Python:
# 1- int
# 2- float
# 3- complex
# Sayısal tipteki değişkenler, onlara bir değer atadığınızda oluşturulur: | Variables of numeric types are created when you assign a value to them:
x = 1
y = 2.8
z = 1j 
print(type(x))  # int
print(type(y))  # float
print(type(z))  # complex

#? Int 
# Int veya tamsayı, pozitif veya negatif, ondalık basamak içermeyen, sınırsız uzunlukta bir tam sayıdır. | Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))  # int
print(type(y))  # int
print(type(z))  # int

#? Float
# Bir veya daha fazla ondalık basamak içeren pozitif veya negatif bir sayıdır. | Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Float, 10'un kuvvetini belirtmek için "e" harfi bulunan bilimsel sayılar da olabilir. | Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 1.10
y = 1.0
z = -35.59

print(type(x))  # float
print(type(y))  # float
print(type(z))  # float

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


#? Complex
# Karmaşık sayılar sanal kısım olarak "j" ile yazılır: | Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))  # complex
print(type(y))  # complex
print(type(z))  # complex

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

#! Not: Karmaşık sayıları başka bir sayı türüne dönüştüremezsiniz.
#! Note: You cannot convert complex numbers into another number type.


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

#? Rastgele Sayı
# Python'un rasgele bir sayı yapmak için bir random() işlevi yoktur, | Python does not have a random() function to make a random number, 
# ancak Python'un rasgele sayılar yapmak için kullanılabilecek random adlı yerleşik bir modülü vardır: | but Python has a built-in module called random that can be used to make random numbers:

# 1 ile 9 arasında rastgele bir sayı görüntüleyin: | display a random number between 1 and 9:
import random

print(random.randrange(1, 10))


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