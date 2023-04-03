
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

#? >= (büyük veya eşit mi | greater or equal)
a = 13
b = 13
conclusion = a >= b
print(conclusion)  # True

a = 10
b = 25
conclusion = a >= b
print(conclusion)  # False


#? <= (küçük veya eşit mi | less than or equal)
a = 3.5
b = 1.5
conclusion = a <= b
print(conclusion)  # False

a = 0
b = 0
conclusion = a <= b
print(conclusion)  # True


#! Mantıksal Operatörü (Logical Operator):

#? And: Bir tane False değer varsa False sonuç verir | Returns False if there is one False value
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


#? Or: Bir tane True değeri varsa sonuç True | If there is one True value, the result is True
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


#? Not: True değeri False, False değeri True çevirir. Aynı zamanda False karşılığı 0, True karşığı 1'dir. | True converts False and False to True. Also, False corresponds to 0, True corresponds to 1.
# not(True) ==> False
# not(False) ==> True
# not(1) ==> 0
# not(0) ==> 1


a = 25
b = not(a == 85)
print(b)  # True


#? True ve False Olarak Değerlendirilen İfadeler | Expressions Evaluating True and False
# Numerik olarak 0 olan bütün değerler ve None değeri False:
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(0 + 0j))  # False
print(bool(None))  # False

# Bütün boş collection data tipindeki yapılar ve boş stringler False:
print(bool([]))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(set()))  # False
print(bool(""))  # False


#? isinstance() 
# Python dilinde bir built-in fonksiyondur ve bir nesnenin belirli bir sınıfın bir örneği olup olmadığını kontrol etmek için kullanılır.
# iki argüman alır: birinci argüman, kontrol edilecek nesnedir, ikinci argüman ise kontrol edilecek sınıftır. 
# Fonksiyon, nesnenin belirtilen sınıfın bir örneği olup olmadığını kontrol eder ve sonuç olarak True veya False döndürür.

# It is a built-in function in Python and is used to check if an object is an instance of a particular class.
# takes two arguments: the first argument is the object to check, the second argument is the class to check. 
# The function checks if the object is an instance of the specified class and returns True or False as a result.

x = 200
print(isinstance(x, int))  # True


#? İşlem Önceliği | Process priority
# 1- Not
# 2- And
# 3- Or

q = not False and True
print(q)  # True

w = True or False and False
print(w)  # True


#? Objeleri Logical Operator ile kullanmak | Using Entities with the Logical Operator
# and operatoru False değer arar, ilk bulduğu False değeri döndürür ve devamındaki objeleri kontrol etmez. Eğer bulamazsa son objeyi döndürür.

t = 5 and "string" and ["a",1] and [] and True
print(t)  # []

j = ["a"] and "False" and 1 and "True" and {"true":"True"}
print(j)  # {'true': 'True'}

# or operatoru True değer arar, ilk bulduğu True değeri döndürür ve devamındaki objeleri kontrol etmez. Eğer bulamazsa son objeyi döndürür.

t = 0 or "" or 1 or []  
print(t)  # 1

j = [] or False or 0 or {}
print(j)  # {}


#! Kimlik operatörü (Identity operator):
# İki değeri karşılaştırmak için kullanılan bir karşılaştırma operatörüdür. Bu operatör, karşılaştırılan iki değerin tamamen aynı olup olmadığını kontrol eder.
# It is a comparison operator used to compare two values. This operator checks if the two values being compared are exactly the same.

num1 = 10
num2 = 10
str1 = "10"

print(num1 is num2)  # True - num1 ve num2 aynı sayıdır | num1 and num2 are the same number
print(num1 is str1)  # False - num1 sayıdır ancak str1 stringdir | num1 is number but str1 is string
print(num1 is not str1)  # True - num1 sayıdır ancak str1 stringdir ve eşit değiller | num1 is number but str1 is string and they are not equal


#! Üyelik Operatörleri
# Nesnede belirtilen değere sahip bir dizi varsa True döndürür
# Returns True if a sequence with the specified value is present in the object

x = ["apple", "banana"]

print("banana" in x)  # True
print("pear" in x)  # False
print("salad" not in x)  # True
print("banena" not in x)  # False
