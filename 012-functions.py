
#! Function: İşlev, yalnızca çağrıldığında çalışan bir kod bloğudur. | A function is a block of code which only runs when it is called.
#? def kelimesi ile başlar, fonksiyon ismi yapacağı işlem ile ilgili anahtar kelime niteliği barındırmalıdır.
#? It starts with the word def, the function name must contain a keyword attribute related to the operation it will perform.

def selamla():                    # ==> Girdiler parantez içine yazılır,  | Entries are written in parentheses,
    print('Merhaba.. Hello..')    # girdiler için değer atamak zorunda değiliz. | We don't have to assign values for the inputs.        
                                  # Parantez yinede belirtmek zorundayız. | We still have to specify the parentheses.

#####* yukarıda fonksiyonu tanımladık ama çalışması için çağırmamız gerekir:
# Bir işlevi çağırmak için, işlev adını ve ardından parantez kullanın:
#####* we defined the function above but we need to call it for it to work:
# To call a function, use the function name followed by parentheses:

selamla()  # Merhaba.. Hello..


#! Neden Kullanırız: | Why We Use:
#  1- Kod tekrarından kaçınma | Avoiding code duplication
#? 2- Soyutlama | Abstraction
#  3- Test etme, hata ayıklama | Testing, debugging
#? 4- Modulerlik(en küçük parçalara ayırmak) | Modularity (dividing into the smallest parts)
#  5- İş birliği(takım arkadaşlarıyla) | Collaboration (with teammates)

ali = [80, 65]
ayşe = [52, 73]
mehmet = [23, 52]

"""
Hazırladığımız senaryoya göre 3 öğrencinin ara sınav ve final notları bir liste halinde verilmektedir. Listelerin ilk unsurları öğrencilerin ara sınav notu, ikinci unsurları ise final notu olarak değerlendirilecektir. Vize notunun %40'ı, final notunun %60'ı alınacak ve ortalaması hesaplanacaktır.
According to the scenario we prepared, the midterm and final grades of 3 students are given in a list. The first elements of the lists will be evaluated as the students' midterm grade and the second elements as the final grade. The midterm grade will be 40%, the final grade 60% will be taken and the average will be calculated.
"""

ali_average = ali[0] * 0.4 + ali[1] * 0.6 
ayşe_average = ayşe[0] * 0.4 + ayşe[1] * 0.6 
mehmet_average = mehmet[0] * 0.4 + mehmet[1] * 0.6 
print(ali_average)  # 71.0
print(ayşe_average)  # 64.6
print(mehmet_average)  # 40.4

#!#### Bir olayı 1'den çok tekrar edersek kod tekrarına gireriz. Fonksiyonla yapmayı deneyelim:
#!#### If we repeat an event more than 1, we get code duplication. Let's try to do it with function:

def average(liste):
    return liste[0] * 0.4 + liste[1] * 0.6

print(average(ali), average(ayşe), average(mehmet))  # 71.0 64.6 40.4

#? Sınav oranları değişti | Exam rates have changed:
# Diğerinde tek tek değiştirmek zorunda kalırdık, 3 satırı da dikkatli incelemek zorunda kalıcaktık.
# Fonksiyon kullandığımızda sadece fonksiyon içindeki değeri değiştirmek yeterli olucaktırç Buda hata ayıklama ve test etmek için kolaylıktır.
# In the other, we would have to change one by one, we would have to examine all 3 lines carefully.
# When we use a function, it will be enough to change the value in the function. This is easy for debugging and testing.

ali_average = ali[0] * 0.3 + ali[1] * 0.7 
ayşe_average = ayşe[0] * 0.3 + ayşe[1] * 0.7 
mehmet_average = mehmet[0] * 0.3 + mehmet[1] * 0.7 

def average(liste):
    return liste[0] * 0.3 + liste[1] * 0.7



#? Soyutlama | Abstraction: 
def average(liste):
    avrg = liste[0] * 0.3 + liste[1] * 0.7
    return avrg

# print(avrg)  #! NameError: name 'avrg' is not defined
               #! Fonksiyon içinde tanımlı bir değişkeni fonksiyon dışında çağırırsak hata alırız. | If we call a variable defined inside the function outside the function, we will get an error.
               #! Fonksiyon diğer kodlardan izole bir şekilde çalıştığı için oluşacak muhtemel problerin önüne geçer. | Since the function works in isolation from other codes, it avoids possible problems.


#? Argüman Ya da Parametre | Parameters or Arguments
#  Bilgi, fonksiyonlara bağımsız değişken olarak iletilebilir.  | Information can be passed into functions as arguments.
#* Bağımsız değişkenler, fonksiyon adından sonra parantez içinde belirtilir. | Arguments are specified after the function name, inside the parentheses.
#  İstediğiniz kadar argüman ekleyebilirsiniz, sadece virgülle ayırın. | You can add as many arguments as you want, just separate them with a comma.
#* Parametre, fonksiyon tanımında parantez içinde listelenen değişkendir.

def take_square(number):    #** ==> number burda bir parametredir | number is a parameter here
    print(number * number)

# take_square() #! Hata veriyor, | It gives an error, 
                #! Fonksiyonu tanımlarken parametre alacağını belirtmiştik fakat fonksiyonu çağırırken herhangi bir argüman göndermedik.
                #! While defining the function, we stated that it will take a parameter, although we did not send any arguments when calling the function.
"""TypeError: take_square() missing 1 required positional argument: 'number'"""

take_square(7)  # 49


#? Keyfi Argümanlar, *args | Arbitrary Arguments, *args
#  İşlevinize kaç bağımsız değişkenin(argüman) iletileceğini bilmiyorsanız, parametre adından önce bir * ekleyin.
#* Bu şekilde, fonksiyon bir dizi bağımsız değişken(argüman) alır ve öğelere buna göre erişebilir:

#  If you don't know how many arguments to pass to your function, add a * before the parameter name.
#* This way, the function takes a set of arguments and can access the elements accordingly:

#! Argüman sayısı bilinmiyorsa, parametre adından önce bir * ekleyin:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#? Positional Arguments:
def yourSelf(name, city, age):
    print(f"I'm {name}, living {city}. I am {age} years old ")

yourSelf('Pakize', 'İstanbul', 24)  # I'm Pakize, living İstanbul. I am 24 years old
yourSelf('İstanbul', 24, 'Pakize')  # I'm İstanbul, living 24. I am Pakize years old


#? Keyword Arguments:
yourSelf(age=24, city="İstanbul", name="Pakize")  # I'm Pakize, living İstanbul. I am 24 years old
# yourSelf(name="Pakize", "İstanbul", 20)  #! Hata verir, ilk positional arguments varsa tanımlanır, sonra keyword arguments tanımlanır.
                                           #! It gives an error, first positional arguments are defined, then keyword arguments are defined.
yourSelf("Pakize", age=20, city="İstanul")  # I'm Pakize, living İstanul. I am 20 years old


#? Default Arguments:
def your_self(name, age, city ="İstanbul",  country ="Türkiye"):
    print(f"I'm {name}, living {country+'/'+city}. I am {age} years old ")

your_self("Pakize", "24")  # I'm Pakize, living Türkiye/İstanbul. I am 24 years old
your_self(name="John", age="58", city="New York" , country="ABD")  # I'm John, living ABD/New York. I am 58 years old


#? *args and **kwargs
#* *args: değişkenin içindeki elemanları birer birer al | get the elements inside the variable one by one
x = [1,2,3]
print(x)  # [1, 2, 3]
print(*x)  # 1 2 3

def asterix(a):
    print(a)
# asterix(4,5)  #! asterix() takes 1 positional argument but 2 were given
                #! hata verir, tek parametre verdik fonksiyona 2 adet argüman göndermeye çalıştık.

def sum(*args):
    s = 0
    for arg in args:
        s += arg
    return s

sonuc = sum(1, 2, 3, 4, 5)
print(sonuc) # 15


#* **kwargs: Girdiler key value şeklinde olmalıdır | Entries must be key values 
def double_asterix(**kw):
    print(kw)

double_asterix(a="1", b="2")  # {'a': 1, 'b': 2}

def mixs(a, b, *c, **d):
    print(a, b)  # 1 iki
    for i in c:
        print(i)  # 4
                  # 5
                  # alti

    for i in d:
        print(i, d[i])  # yedi 7
                        # sekiz 8
                        # _9 dokuz

mixs(1, "iki", 4,5,"alti", yedi=7, sekiz= 8, _9="dokuz")


#? Rastgele Anahtar Sözcük Argümanları, **kwargs | Arbitrary Keyword Arguments, **kwargs
# Fonksiyonun kaç tane anahtar sözcük(keyword) argüman aktarılacağını bilmiyorsanız, 
#* Fonksiyon tanımında parametre adından önce iki yıldız ** işareti ekleyin:
#  Bu şekilde, fonksiyon bir bağımsız değişkenler sözlüğü alır ve buna göre öğelere erişebilir:

# If you don't know how many keyword arguments the function will pass,
#* Add two asterisks ** before the parameter name in the function definition:
# This way, the function takes a dictionary of arguments and can access the elements accordingly:

#! Anahtar kelime bağımsız değişkenlerinin(argüman) sayısı bilinmiyorsa, parametre adından önce bir çift ** ekleyin:
def my_function(**kid):
  print("His last name is " + kid["lname"])  # His last name is Refsnes

my_function(fname = "Tobias", lname = "Refsnes")



#! Print ile Return arasındaki fark | Difference between Print and Return
#? Print, bir değeri konsola yazdırmak için kullanılır ve fonksiyonun geri kalanı için bir etkisi yoktur. Yani, bir değeri print ile yazdırdığınızda, bu değeri başka bir yerde kullanamazsınız.
#  Return ise, bir fonksiyondan bir değer döndürmek için kullanılır. Fonksiyon sonucunda döndürülen değer, başka bir değişkene atanabilir veya başka bir fonksiyonda kullanılabilir.
#? Kısacası Fonksiyon ile yapmış olduğum işlemde elde ettiğim sonucu başka yerlerde kullanmak isteyebilirim bu durumda return kullanmam gerekir. print bana sadece sonucu görüntülememe yardımcı olur.

def add_numbers(x, y):
    print(x + y)

an = add_numbers(5,9)  # 14
print(an)  # None


def get_cube(number):
    return number ** 3

gc = get_cube(8)
print(gc)  # 512


#! Değiştirmek | Change:

def change():
    k = 20
    print(k) 

change()  # 20
# print(k)  #! Hata verir: k değişkeni local bir değişkendir. | It gives an error: variable k is a local variable.
            #! Globalden local bir değişkene erişemiyoruz. | We cannot access a local variable from the global.

k = 25
def change_2():
    k = 30
    print(k)  

change_2()  # 30
print(k)  # 25 : Global değişkene erişebilir. | It can access the global variable.


#######! TAVSİYE EDİLMEZ | NOT RECOMMENDED #######!
def change_3():
    global k
    k = 45
    print(k) 

change_3()  # 45
print(k)  # 45


#! Fonksiyon Türleri | Function Types:
#? Built-in Functions:(Dahili Fonksiyonlar): 
# Python'da zaten tanımlanmış ve hazır olarak kullanılabilecek birçok dahili işlev vardır. 
# Bu fonksiyonların en sık kullanılanları arasında "print()", "len()", "input()", "range()", "open()" ve "str()" gibi fonksiyonlar yer alır.

# Python has many built-in functions already defined and readily available.
# Among the most common of these functions are functions such as "print()", "len()", "input()", "range()", "open()" and "str()".

#? print(): 
# Verilen argümanları standart çıktıya yazdırmak için kullanılır. | Used to print the given arguments to standard output.
print("Merhaba Dünya!") # Merhaba Dünya! 


#? len(): 
# Bir nesnenin uzunluğunu hesaplamak için kullanılır. | It is used to calculate the length of an object.
liste = [1, 2, 3, 4, 5]
print(len(liste)) # 5 


#? type(): 
# Bir nesnenin türünü döndürmek için kullanılır. | Used to return the type of an object.
sayi = 10
print(type(sayi)) # <class 'int'> 


#? range(): 
# Bir aralık nesnesi oluşturmak için kullanılır. | It is used to create a range object.
for i in range(1, 6):
    print(i) # 1, 2, 3, 4, 5 


#? zip(): 
# Verilen iterable nesnelerden eşleştirilmiş bir nesne oluşturmak için kullanılır.
# It is used to create a matched object from the given iterable objects.
liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
liste3 = [True, False, True]

for x in zip(liste1, liste2, liste3):
    print(x) # (1, 'a', True), (2, 'b', False), (3, 'c', True)


#? sum(): 
# Verilen sayısal değerlerin toplamını hesaplamak için kullanılır. | It is used to calculate the sum of the given numeric values.
liste = [1, 2, 3, 4, 5]
print(sum(liste)) # 15


#? max(): 
# Verilen sayısal değerlerin en büyük değerini döndürmek için kullanılır. | It is used to return the largest value of the given numeric values.
liste = [1, 2, 3, 4, 5]
print(max(liste)) # 5 


#? min(): 
# Verilen sayısal değerlerin en küçük değerini döndürmek için kullanılır. | It is used to return the smallest value of the given numeric values.
liste = [1, 2, 3, 4, 5]
print(min(liste)) # 1


#? all(): 
# Bu fonksiyon, bir iterable'ın tüm elemanlarının "True" olduğunu kontrol eder. | This function checks that all elements of an iterable are "True".
# Eğer tüm elemanlar "True" ise, fonksiyon "True" değerini döndürür. | If all elements are "True", the function returns "True".
# Aksi takdirde, "False" değerini döndürür. | Otherwise, it returns "False".
numbers = [2, 4, 6, 8, 10]
result = all(num % 2 == 0 for num in numbers)
print(result)  # True

numbers2 = [2, 3, 4, 6, 8, 10]
result2 = all(num % 2 == 0 for num in numbers2)
print(result2)  # False


#? any(): 
# Bu fonksiyon, bir iterable'ın en az bir elemanının "True" olduğunu kontrol eder. | This function checks that at least one element of an iterable is "True".
# Eğer en az bir eleman "True" ise, fonksiyon "True" değerini döndürür. | If at least one element is "True", the function returns "True".
# Eğer iterable'da hiçbir eleman "True" değilse, "False" değerini döndürür. | Returns "False" if no element in the iterable is "True".
numbers = [1, 3, 5, 7, 8]
result = any(num % 2 == 0 for num in numbers)
print(result)  # True

numbers2 = [1, 3, 5, 7, 9]
result2 = any(num % 2 == 0 for num in numbers2)
print(result2)  # False


#? filter(): 
# Bu fonksiyon, verilen bir fonksiyonu bir iterable nesnenin her elemanına uygular 
# ve sadece fonksiyonun "True" olarak değerlendirdiği elemanları içeren bir iterator nesnesi döndürür.

# This function applies a given function to every element of an iterable object
# and returns an iterator object containing only elements that the function considers "True".
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 6]

words = ["apple", "banana", "cherry", "date"]
short_words = filter(lambda x: len(x) < 6, words)
print(list(short_words))  # ['apple', 'cherry', 'date']


#? round(): 
# Bu fonksiyon, verilen sayıyı belirtilen bir ondalık basamağa yuvarlar. | This function rounds the given number to a specified decimal place.
# Varsayılan olarak, fonksiyon sayıyı en yakın tamsayıya yuvarlar. | By default, the function rounds the number to the nearest integer.
# Ondalık basamak sayısını belirtmek için, fonksiyona bir ikinci argüman olarak bir tam sayı verilebilir. | An integer can be given as a second argument to the function to specify the number of decimal places.
number = 3.14159265359
rounded = round(number, 2)
print(rounded)  # 3.14

number2 = 3.5
rounded2 = round(number2)
print(rounded2)  # 4


#? int(): 
# Bir sayısal değerin tamsayı kısmını döndürmek için kullanılır. | Used to return the integer part of a numeric value.
ondalikli_sayi = 5.9
print(int(ondalikli_sayi)) # 5 


#? float(): 
# Bir sayısal değerin ondalık kısmını döndürmek için kullanılır. | Used to return the decimal part of a numeric value.
tamsayi = 5
print(float(tamsayi)) # 5.0


#? str(): 
# Bir nesnenin karakter dizisi temsilini döndürmek için kullanılır. | Used to return the string representation of an object.
sayi = 10
print(str(sayi) + " tane elma var.") # 10 tane elma var.


#? list(): 
# Bir liste nesnesi oluşturmak için kullanılır. | It is used to create a list object.
liste = [1, 2, 3, 4, 5]
print(liste) # [1, 2, 3, 4, 5]


#? dict(): 
# Bir sözlük nesnesi oluşturmak için kullanılır. | It is used to create a dictionary object.
sozluk = {"ad": "Ahmet", "soyad": "Yılmaz", "yas": 25}
print(sozluk) # {'ad': 'Ahmet', 'soyad': 'Yılmaz', 'yas': 25} 


#? set(): 
# Bir küme nesnesi oluşturmak için kullanılır. | It is used to create a set object.
kume = {1, 2, 3, 4, 5}
print(kume) # {1, 2, 3, 4, 5}


#? tuple(): 
# Bir tuple nesnesi oluşturmak için kullanılır. | # Used to create a tuple object.
tuple = (1, 2, 3, 4, 5)
print(tuple) # (1, 2, 3, 4, 5) 


#* Şuana kadar yazıklarımız!!!!
#? User-defined Functions (Kullanıcı Tanımlı Fonksiyonlar): 
# Python'da, kullanıcılar kendi işlevlerini tanımlayabilir ve kullanabilir. 
# Bu tür işlevler, programın daha modüler ve okunaklı olmasına yardımcı olur.

# In Python, users can define and use their own functions.
# Such functions help the program to be more modular and readable.


#? Anonymous Functions (Lambda Fonksiyonları): 
# Python'da, lambda ifadesi kullanılarak anonim işlevler oluşturulabilir. 
# Bu tür işlevler genellikle tek bir satırlık işlemler için kullanılır ve lambda ifadesi kullanılarak tanımlanırlar.

# In Python, anonymous functions can be created using the lambda expression.
# Such functions are usually used for single-line operations and are defined using a lambda expression.

#* İki sayıyı toplamak için lambda fonksiyonu kullanma:
addition = lambda x, y: x + y
print(addition(3, 5)) # Output: 8

#* Bir listenin elemanlarını iki katına çıkarmak için lambda fonksiyonu kullanma:
my_list = [1, 2, 3, 4, 5]
doubled_list = list(map(lambda x: x * 2, my_list))
print(doubled_list) # Output: [2, 4, 6, 8, 10]

#* Bir listedeki sayıları filtrelemek için lambda fonksiyonu kullanma:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered_list) # Output: [2, 4, 6, 8, 10]

#* İki listenin elemanlarını toplayarak yeni bir liste oluşturmak için lambda fonksiyonu kullanma:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))
print(result) # Output: [5, 7, 9]

#* Bir dict. değerleri sıralamak için lambda fonksiyonu kullanma:
my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict) # Output: {'b': 1, 'c': 2, 'a': 