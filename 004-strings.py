
#! Strings: 
#  "" ve '' içine yazılan bütün karakterler string'dir. | All characters written in "" and '' are strings. 
#? String yazarken hangi tırnak modeli ile başladıysak onunla bitirmeliyiz. Örneğin: | When writing a string, we must end with whichever nail model we started with. For example:
# string_1 = "I am Pakize' ==> ✖️
string_2 = "I am Pakize"  # ==> ✔️
string_2 = 'I am Pakize'  # ==> ✔️

#? String yazarken başladığımız tırnak modelini yazmış olduğumuz text'in içinde kullanamayız. Örneğin: | We should not use the quotation model that we started while writing a string in the text we have written. For example:
# string_3 = 'I'm Pakize' ==> ✖️
string_4 = "I'm Pakize"  # ==> ✔️
string_5 = 'I"m Pakize'  # ==> ✔️

name = 'Pakize'
last_name = 'KILIÇ'
age = '24'

message = "My name is " + name + " " +last_name + ". I am " + age + " years old."

print(message)  # My name is Pakize KILIÇ. I am 24 years old.

#! String Slicing  str[start:stop:step] 
#!                           stop dahil değildir | stop is not included
#!                           step default = 1 

print(message[0])  # M
print(message[-1])  # .
print(message[-3])  # l
print(message[0:7:2])  # M ae
print(message[6:16])  # e is Pakiz
print(message[0:2])  # My
print(message[:2])  # My
print(message[5:])  # me is Pakize KILIÇ. I am 24 years old. 
print(message[-3:-1])  # ld
print(message[-4:])  # old.
print(message[:])  # My name is Pakize KILIÇ. I am 24 years old.
print(message[::-1])  # .dlo sraey 42 ma I .ÇILIK ezikaP si eman yM


#! String Format

productName = "apple"
price = 15
kg = 1.5

# #? msg = kg + " kg of " + productName + " price " + (price * kg) # TypeError: unsupported operand type(s) for +: 'float' and 'str'
msg = str(kg) + " kg of " + productName + " price " + str(price * kg) 
print(msg)  # 1.5 kg of apple price 22.5

msg2 = "{} kg of {} price {}".format(kg, productName, (price * kg))
print(msg2)  # 1.5 kg of apple price 22.5

msg3 = "{1} kg of {2} price {0}".format((price * kg), kg, productName)
print(msg3)  # 1.5 kg of apple price 22.5

msg4 = "{k} kg of {pn} price {pk}".format(pk= price*kg , k=kg, pn=productName)
print(msg4)  # 1.5 kg of apple price 22.5

#! f-string

msg5 = f"{kg} kg of {productName} price {price * kg}"
print(msg5)  # 1.5 kg of apple price 22.5


#! String Method

# upper()
#? Makes all letters big. | Tüm harfleri büyük yapar.
note = "Python is easy to learn because it is a high level of language."
conclusion = note.upper()
print(conclusion)  # PYTHON IS EASY TO LEARN BECAUSE IT IS A HIGH LEVEL OF LANGUAGE.

# lower()
#? Makes all letters small. | Tüm harfleri küçük yapar.
note2 = "Python is easy to learn because it is a high level of language."
conclusion2 = note2.lower()
print(conclusion2)  # python is easy to learn because it is a high level of language.

# title()
#? Caps the first letters of words | Kelimelerin ilk harflerini büyük yapar
note3 = "Python is easy to learn because it is a high level of language."
conclusion3 = note3.title()
print(conclusion3)  # Python Is Easy To Learn Because It Is A High Level Of Language.

# capitalize()
#? The first letter of the first word makes capital letters | İlk kelimenin ilk harfi büyük harf yapar
note4 = "Python is easy to learn because it is a high level of language."
conclusion4 = note4.capitalize()
print(conclusion4)  # Python is easy to learn because it is a high level of language
 
# isupper()
#? Checks if all letters are uppercase | Bütün harfler büyük harf mi diye kontrol eder
note5 = "Python is easy to learn because it is a high level of language."
conclusion5 = note5.isupper()
print(conclusion5)  # False

# split()
#? Makes all the words an element of the list | Tüm kelimeleri listenin bir öğesi yapar
note6 = "Python is easy to learn because it is a high level of language."
conclusion6 = note6.split()
print(conclusion6)  # ['Python', 'is', 'easy', 'to', 'learn', 'because', 'it', 'is', 'a', 'high', 'level', 'of', 'language.']

# split()
#? 
note7 = "Python is easy to learn . because it is a high level of language"
conclusion7 = note7.split(".")
print(conclusion7)  # ['Python is easy to learn ', ' because it is a high level of language']

# strip()
#? Divides one element of the list up to the point as the other element after the point | Listenin bir öğesini, noktadan sonraki diğer öğe olarak noktaya böler
note8 = "  Python is easy to learn because it is a high level of language.   "
conclusion8 = note8.strip()
print(conclusion8)  # Python is easy to learn because it is a high level of language.

# index()
#? Is there a word entered, and if so, how many index numbers does it have? if it does not exist, it gives an error | Girilen bir kelime var mı ve eğer öyleyse, kaç tane dizin numarası var? eğer yoksa, bir hata verir
note9 = "Python is easy to learn because it is a high level of language."
conclusion9 = note9.index("high")
print(conclusion9)  # 40

# startswith()
#? Does the sentence start with the entered word or letter? If so, if not True, false returns. It has case sensitivity. Cümle girilen kelime veya harf ile mi başlıyor. Eğer öyleyse True değilse false döner. Büyük küçük harf duyarlılığı vardır.
note10 = "Python is easy to learn because it is a high level of language."
conclusion10 = note10.startswith("Python")
print(conclusion10)  # True

# endswith()
#? Does the sentence end with the entered word or letter. If so, false returns if Not True. It has case sensitivity. | Cümle girilen kelime veya harf ile mi bitiyor. Eğer öyleyse True değilse false döner. Büyük küçük harf duyarlılığı vardır.
note11 = "Python is easy to learn because it is a high level of language."
conclusion11 = note11.endswith("P")
print(conclusion11)  # False

# replace("1","2")
#? It allows us to change the character or word in the sentence. 1 parameter is what is requested to change, parameter 2 is what is wanted to be written new. | Cümle içerisinde karakter veya kelime değişikliği yapmamızı sağlar. 1 parametre değişmesi istenen şey, 2. parametre yeni yazılması istenen şey. 
note12 = "Python is easy to learn because it is a high level of language."
conclusion12 = note12.replace("Python","JavaScripts")
print(conclusion12)  # JavaScripts is easy to learn because it is a high level of language.

# isalpha()
#? Returns True if it contains only alphabetic characters, or False if it does not. | Yalnızca alfabetik karakterler içeriyorsa True, içermiyorsa False değerini döndürür.
not1 = "abcssd"
con1 = not1.isalpha()
print(con1)  # True

# isdigit()
#? Returns True if it contains only numeric characters, or False if it does not. | Yalnızca sayı karakterler içeriyorsa True, içermiyorsa False değerini döndürür.
not2 = "12389"
con2 = not2.isdigit()
print(con2)  # True