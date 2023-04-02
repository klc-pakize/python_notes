
#! Function:
#? def kelimesi ile başlar, fonksiyon ismi yapacağı işlem ile ilgili anahtar kelime niteliği barındırmalıdır.
#? It starts with the word def, the function name must contain a keyword attribute related to the operation it will perform.

def selamla():                    # ==> Girdiler parantez içine yazılır,  | Entries are written in parentheses,
    print('Merhaba.. Hello..')    # girdiler için değer atamak zorunda değiliz. | We don't have to assign values for the inputs.        
                                  # Parantez yinede belirtmek zorundayız. | We still have to specify the parentheses.

#####* yukarıda fonksiyonu tanımladık ama çalıştırırsak devreye girer ve işlem yapar, çalıştırmak için;
#####* We defined the function above, but if we run it, it will be activated and processed, to run;

selamla()  # Merhaba.. Hello..


def take_square(number):    # ==> number burda bir parametredir | number is a parameter here
    print(number * number)

# take_square() #! Hata veriyor, | It gives an error, 
              #! Fonksiyonu tanımlarken parametre alacağını belirtmiştik fakat fonksiyonu çağırırken herhangi bir argüman göndermedik.
              #! While defining the function, we stated that it will take a parameter, although we did not send any arguments when calling the function.
"""TypeError: take_square() missing 1 required positional argument: 'number'"""

take_square(7)  # 49


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


#! Positional Arguments:
def yourSelf(name, city, age):
    print(f"I'm {name}, living {city}. I am {age} years old ")

yourSelf('Pakize', 'İstanbul', 24)  # I'm Pakize, living İstanbul. I am 24 years old
yourSelf('İstanbul', 24, 'Pakize')  # I'm İstanbul, living 24. I am Pakize years old

#! Keyword Arguments:
yourSelf(age=24, city="İstanbul", name="Pakize")  # I'm Pakize, living İstanbul. I am 24 years old
# yourSelf(name="Pakize", "İstanbul", 20)  #! Hata verir, ilk positional arguments varsa tanımlanır, sonra keyword arguments tanımlanır.
                                           #! It gives an error, first positional arguments are defined, then keyword arguments are defined.
yourSelf("Pakize", age=20, city="İstanul")  # I'm Pakize, living İstanul. I am 20 years old

#! Default Arguments:
def your_self(name, age, city ="İstanbul",  country ="Türkiye"):
    print(f"I'm {name}, living {country+'/'+city}. I am {age} years old ")

your_self("Pakize", "24")  # I'm Pakize, living Türkiye/İstanbul. I am 24 years old
your_self(name="John", age="58", city="New York" , country="ABD")  # I'm John, living ABD/New York. I am 58 years old

#! *args and **kwargs
#? *args: değişkenin içindeki elemanları birer birer al | get the elements inside the variable one by one

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

#? **kwargs: Girdiler key value şeklinde olmalıdır | Entries must be key values 

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