
#! Atama Operatörü (Assignment Operator):
#  '=' işareti ile atama işlemi yapılır, | Assignment is done with the '=' sign,
#? Sağdan sola doğru atama işlemi gerçekleştirilir. | Assignment is performed from right to left.

x = 20
y = 50
z = 80
print(x, y, z)  # 20 50 80

x, y, z = 20, 50, 80
print(x, y, z)  # 20 50 80

#! 3 değişken tanımlayıp 3'ten fazla değişken değeri tanımlarsak hata alırız. Bu hatayı önlemek için değişkenlerin başına '*' ekleyebiliriz. | If we define 3 variables and define more than 3 variable values, we will get an error. To avoid this error, we can add '*' to the beginning of the variables.

# x, y, z = 10, 20, 30, 40, 50
# print(x, y, z)  #! ValueError: too many values to unpack (expected 3)
x, y, *z = 10, 20, 30, 40
print(x, y, z)  # 10 20 [30, 40]
x, *y, z = 10, 20, 30, 40
print(x, y, z)  # 10 [20, 30] 40



#! Karşılaştırma Operatörü (Compare Operator):
#  Belirli durumları karşılaştırmak için kullanılırlar. | They are used to compare certain situations
#? Karşılaştırma sonucunda True veya False döndürürler. | They return True or False as a result of the comparison.

#? == (eşit mi | is it equal)
info_email = "test@gmail.com"
student_email = "test@gmail.com"

conclusion = info_email == student_email
print(conclusion)  # True

info_email = "test123@gmail.com"
student_email = "test@gmail.com"

conclusion = info_email == student_email
print(conclusion)  # False


#? != (eşit değil mi | isn't it equal)
info_phone = 1223334444
student_phone = 1223334444

conclusion = info_phone != student_phone
print(conclusion)  # False

info_phone = 122333444455555
student_phone = 1223334444

conclusion = info_phone != student_phone
print(conclusion)  # True


#? > (büyük mü | is it big)
a = 89
b = 29
conclusion = a > b
print(conclusion)  # True

a = 18
b = 98
conclusion = a > b
print(conclusion)  # False


#? < (küçük mü | is it small)
a = 3.5
b = 13
conclusion = a < b
print(conclusion)  # True

a = 120
b = 25
conclusion = a < b
print(conclusion)  # False

#? > (büyük veya eşit mi | greater or equal)
a = 13
b = 13
conclusion = a >= b
print(conclusion)  # True

a = 10
b = 25
conclusion = a >= b
print(conclusion)  # False


#? < (küçük veya eşit mi | less than or equal)
a = 3.5
b = 1.5
conclusion = a <= b
print(conclusion)  # False

a = 0
b = 0
conclusion = a <= b
print(conclusion)  # True


#! Mantıksal Operatörü (Logical Operator):

#? And
# True and True = True
# False and False = False
# True and False = False
# False and True = False

info_email = "test123@gmail.com"
info_password = "Test123"

student_email = "test123@gmail.com"
student_password = "Test123"
status_1 = info_email == student_email  # True
status_2 = info_password == student_password  # True
print(status_1 and status_2)  # True

student_email = "test123.@gmail.com"
student_password = "Test123"
status_1 = info_email == student_email  # False
status_2 = info_password == student_password  # True
print(status_1 and status_2)  # False


#? Or
# True or True = True
# False or False = False
# True or False = True
# False or True = True

info_email = "test123@gmail.com"
info_password = "Test123"

student_email = "test123@gmail.com"
student_password = "Test123"
status_1 = info_email == student_email  # True
status_2 = info_password == student_password  # True
print(status_1 and status_2)  # True

student_email = "test123.@gmail.com"
student_password = "Test123"
status_1 = info_email == student_email  # False
status_2 = info_password == student_password  # True
print(status_1 and status_2)  # True


#? Not
# not(True) ==> False
# not(False) ==> True

a = 25
b = not(a == 85)
print(b)  # True


#! Kimlik operatörü (Identity operator):
# İki değeri karşılaştırmak için kullanılan bir karşılaştırma operatörüdür. Bu operatör, karşılaştırılan iki değerin tamamen aynı olup olmadığını kontrol eder.
# It is a comparison operator used to compare two values. This operator checks if the two values being compared are exactly the same.

num1 = 10
num2 = 10
str1 = "10"

print(num1 is num2)  # True - num1 ve num2 aynı sayıdır | num1 and num2 are the same number
print(num1 is str1)  # False - num1 sayıdır ancak str1 stringdir | num1 is number but str1 is string
print(num1 is not str1)  # True - num1 sayıdır ancak str1 stringdir ve eşit değiller | num1 is number but str1 is string and they are not equal