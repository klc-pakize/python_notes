
#! Genel Olarak Dizi 
#! Array in General 
name = "Ali"
name2 = "Veli"
name3 = "Deli"

#? Yukarıdaki değişken tanımlamada bazı zamamnlarda değişken ismi bulurken güçlük çekebiliyoruz, bu durumlarda array(dizi)'e kullanmak daha mantıklıdır:
#? In the variable definition above, we may have difficulties in finding the variable name in some fields, in these cases it is more reasonable to use a array:

names = ["Ali", "Veli", "Deli"]

print(names[0])  # Ali
print(names[1])  # Veli
print(names[2])  # Deli

#! Python’da Dizi Türleri:  
#  1- List, sıralı ve değişken bir koleksiyondur. Yinelenen üyelere izin verir.
#? 2- Tuple, sıralı ve değişmez bir koleksiyondur. Yinelenen üyelere izin verir.
#  3- Set, sırasız, değiştirilemez* ve indekslenmemiş bir koleksiyondur. Yinelenen üye yok.
#? 4- Dictionary, sıralı** ve değişken bir koleksiyondur. Yinelenen üye yok.

# *Set öğeleri değiştirilemez, ancak istediğiniz zaman öğeleri kaldırabilir ve/veya ekleyebilirsiniz.
# **Python sürüm 3.7'den itibaren sözlükler sıralanmıştır . Python 3.6 ve önceki sürümlerde sözlükler sırasızdır .



#! Array Types in Python:
#  1- List is a collection which is ordered and changeable. Allows duplicate members.
#? 2- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#  3- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#? 4- Dictionary is a collection which is ordered** and changeable. No duplicate members.

# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#************************************************************************************

#! LIST: Birden çok öğeyi tek bir değişkende depolamak için kullanılır.
#? - [] ile gösterilir
#  - Sıralıdır (elemanların belirli bir sırası olduğu ve bu sıralamanın değişmeyeceği anlamına gelir.)
#? - Elemanlar tekrar edebilir ["a","b","a","a"]
#  - Elemanlar değiştirilebilir (Liste oluşturulduktan sonra listedeki öğeleri değiştirebilir, ekleyebilir ve kaldırabiliriz.)
#? - Farklı veri tipleri aynı list içinde olabilir: [str, int, bool, float, tuple, set, dictionary]
#  - list içinde list tanımlanabilir (nested list)

#? Oluşturmak:
# 1- [] ==> name = "AYŞE" ==> list_1 = [name] ==> ["AYŞE"]
# 2- list() ==> name = "AYŞE" ==> list_2 = list(name) ==> ["A", "Y", "Ş", "E"]

#! LIST: It is used to store multiple items in a single variable.
#? - Denoted by []
#  - Ordered (means that the elements have a specific order and this order will not change.)
#? - Elements are repeatable: ["a","b","a","a"]
#  - Elements can be changed (After the list is created, we can modify, add and remove items in the list.)
#? - Different data types can be in the same list: [str, int, bool, float, tuple, set, dictionary]
#  - list can be defined in list (nested list)

#? To create:
# 1- [] ==> name = "AYŞE" ==> list_1 = [name] ==> ["AYŞE"]
# 2- list() ==> name = "AYŞE" ==> list_2 = list(name) ==> ["A", "Y", "Ş", "E"]

list1 = ["abc", 34, True, 40, "male"]
print(type(list1))  # <class 'list'>

#? Elemana Erişme (Indexing):
names = ["Ali", "Veli", "Deli"]
notes = [70, 80, 90]

print(f"{names[0]} student's grade is {notes[0]}")  # Ali student's grade is 70
print(f"{names[1]} student's grade is {notes[1]}")  # Veli student's grade is 80  
print(f"{names[-1]} student's grade is {notes[-1]}")  # Deli student's grade is 90


#? nested list:
student = [
    ["Ali",70],
    ["Veli",80],
    ["Deli",90],
]

print(f"{student[0][0]} student's grade is {student[0][1]}")  # Ali student's grade is 70
print(f"{student[1][0]} student's grade is {student[1][1]}")  # Veli student's grade is 80
print(f"{student[2][0]} student's grade is {student[2][1]}")  # Deli student's grade is 90


#? Parçalama (Slicing):
car_brands = ["Opel", "Dacia", "Mazda", "Toyota"]

print(car_brands[0:3])  # ["Opel", "Dacia", "Mazda"]
print(car_brands[:2])  # ["Opel", "Dacia"]  #? Başlangıç index numarası verilmez ise default olarak 0'dır | If the starting index number is not given, it is 0 by default.
print(car_brands[0:])  # ["Opel", "Dacia", "Mazda", "Toyota"]  #? Bitiş index numarası verilmez ise default olarak son index numarası + 1 'dir | If the end index number is not given, the last index number is + 1 by default.
print(car_brands[::-1])  # ['Toyota', 'Mazda', 'Dacia', 'Opel']

#? Değer Güncelleme (Mutable)
car_brands[0] = "Honda"
print(car_brands)  # ['Honda', 'Dacia', 'Mazda', 'Toyota']  #? Artık Opel yerine Honda yazıyor | Now it says Honda instead of Opel 

car_brands[0:2] = ["BMW", "Mercedes"]
print(car_brands)  # ['BMW', 'Mercedes', 'Mazda', 'Toyota']  #? Artık 'Honda', 'Dacia' yerine "BMW", "Mercedes" yazıyor | Now it says "BMW", "Mercedes" instead of 'Honda', 'Dacia'

car_brands[0:2] = ["Audi"]
print(car_brands)  # ['Audi', 'Mazda', 'Toyota']  #? 2 Elemanın değişmesi için kod satırı girdik ama sadece 1 eleman verdik, bunun sonucunda 2. eleman için değer vermememize rağmen 2.elemanı sildi. | We entered a line of code to change 2 elements, but only gave 1 element, as a result, it deleted the 2nd element even though we did not give a value for the 2nd element.

car_brands[1:2] = ["Tesla", "RR", "Ferrari"]
print(car_brands)  # ['Audi', 'Tesla', 'RR', 'Ferrari', 'Toyota']  #? Belirttiğimiz index numarasından daha fazla eleman ekleyebiliriz | We can add more elements than the index number we specified.


price = [20, 45, 50, 10]
product = ["cucumber", "tomato", "pepper", "onion"]

print(f"{product[0]} is {price[0]} TL per kilo")  # cucumber is 20 TL per kilo
print(f"{product[1]} is {price[1]} TL per kilo")  # tomato is 45 TL per kilo
print(f"{product[2]} is {price[2]} TL per kilo")  # pepper is 50 TL per kilo
print(f"{product[3]} is {price[3]} TL per kilo")  # onion is 10 TL per kilo

price_product = [
    ["cucumber", 20],
    ["tomato", 45],
    ["pepper", 50],
    ["onion", 10],
]

print(f"{price_product[0][0]} is {price_product[0][1]} TL per kilo")  # cucumber is 20 TL per kilo
print(f"{price_product[1][0]} is {price_product[1][1]} TL per kilo")  # tomato is 45 TL per kilo
print(f"{price_product[2][0]} is {price_product[2][1]} TL per kilo")  # pepper is 50 TL per kilo
print(f"{price_product[3][0]} is {price_product[3][1]} TL per kilo")  # onion is 10 TL per kilo


#! Liste Metod | List Method

#? len()
# Listenin kaç elemandan oluştuğunu döndürür | Returns how many elements the list consists of
list_1 = [1, "s", 5, True]
list_1_len = len(list_1)
print(list_1_len)  # 4


#? append()
# Listenin sonuna bir eleman ekler | Adds an element to the end of the list
list_2 = [1, 2, 3, 4, 5]
list_2_append = list_2.append("numbers")
print(list_2)  # [1,2,3,4,5,"numbers"]


#? insert(index_no, eklenecek) | insert(index_no, will be added)
# İndex numarasını belirterek listeye eleman ekleme | Adding an element to the list by specifying the index number
list_3 = ["a", "c", "d", "e"]
list_3_insert = list_3.insert(1, "b")
print(list_3)  # ["a","b","c","d","e"]


#? remove()
# Listeden eleman siler, | It deletes an element from the list,
# aynı değerden birden fazla varsa ilk karşılaştığı değeri siler ve durur, | if there is more than one of the same value, it deletes the first value it encounters and stops
# olmayan değer verildiğinde hata verir. | It gives an error when a non-existent value is given.
list_4 = [1, 2, "3", False, "12", False]
list_4_remove= list_4.remove(False)
print(list_4)  # [1, 2, "3", "12", False]


#? pop()
# Listeden index numarasına göre eleman siler, | It deletes element from the list by index number, 
# sildiği elemanı döndürür ve dönen elemanla işlem yapabiliriz. | It returns the element it deleted and we can manipulate the returned element.
# Dizini belirtmezseniz, pop()yöntem son öğeyi kaldırır. | If you do not specify the index, the pop() method removes the last item.
list_5 = ["Iphone", "Samsung", "Oppo", "Huawei"]
list_5_pop = list_5.pop(1)
print(list_5_pop)  # Samsung


#? count()
# Bir listede aynı öğeden kaç tane olduğunu sayar, var olmayan bir değer girilirse 0 döndürür.
#  Counts how many of the same element in a list, returns 0 if a non-existent value is entered.
list_6 = [1, 55, 86, 1, 89, "a", False, [1,"c"]]
list_6_count = list_6.count(1)
list_6_count2 = list_6.count("b")
print(list_6_count)  # 2
print(list_6_count2)  # 0


#? copy()
"""
Normal şartlarda bir listeyi 2 farklı değişkene atayabiliriz örneğin: 
a = [1, 2, 3]
b = a
print(a) ==> [1, 2, 3]
print(b) ==>  [1, 2, 3]
şeklinde olur ama, a listesinde yaptığımız değişiklik b listesinde de gerçekleşir, çünkü bu iki değişken bellekte aynı liste adresine sahiptir. Bunun yerine copy() metodunu kullanmak gerekmektedir.

Normally we can assign a list to 2 different variables, for example:
a = [1, 2, 3]
b = a
print(a) ==> [1, 2, 3]
print(b) ==> [1, 2, 3]
but the change we make in list a also happens in list b, because these two variables have the same list address in memory. Instead, it is necessary to use the copy() method.
"""
list_7 = [[1,2], "a", False]
list_7_copy = list_7.copy()
print(list_7_copy)  # [[1, 2], 'a', False]
list_7_copy.append("copy")
print(list_7_copy)  # [[1, 2], 'a', False, 'copy']
print(list_7)  # [[1, 2], 'a', False]


#? index()
# Elemanları index numarasına göre bulma | Finding elements by index number
list_8 = [1, 8, 40, "pro"]
list_8_index = list_8.index("pro")
print(list_8_index)  # 3


#? reverse()
# Listeyi bulunduğu sıralamanın tersine çevirir. | Reverses the list in the order it is in.
list_9 = ["a","b","c","q"]
list_9_1 = [1, 5, 8]
list_9_reverse = list_9.reverse()
print(list_9)  # ['q', 'c', 'b', 'a']
list_9_reverse_1 = list_9_1.reverse()
print(list_9_1)  # [8, 5, 1]


#? sort()
# int değerlerini küçükten büyüğe ve str değerlerini alfabetik olarak sıralar, sorted() orjinal liseyi güncellemez ama sort() orjinal listeyi günceller. string ve int float değerleri birlikte sıralanmaz
# Sorts int values in ascending order and str values alphabetically, sorted() does not update the original high school, but sort() does update the original list. string and int float values do not sort together
list_10 = [8, 3, 4, 10, 86, 0.5]
list_10_sort = list_10.sort()
print(list_10)  # [0.5, 3, 4, 8, 10, 86]

list_10_1 = ["ala", "qal", "58", "isa"]
list_10_1_sort = list_10_1.sort()
print(list_10_1)  # ['58', 'ala', 'isa', 'qal']

list_10_2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list_10_2.sort(reverse = True)
print(list_10_2)  # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']


#? extend()
# Geçerli listeye başka bir listeden öğeler eklemek için yöntemi kullanın. | Use the method to add items from another list to the current list.
# yinelenebilir herhangi bir nesneyi (demetler, kümeler, sözlükler vb.) ekleyebilirsiniz. | you can include any iterable object (tuples, sets, dictionaries, etc.).
list_11 = ["apple", "banana", "cherry"]
list_12 = ["mango", "pineapple", "papaya"]
list_11.extend(list_12)
print(list_11)  # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

list_13 = ["apple", "banana", "cherry"]
list_14 = ("kiwi", "orange")
list_13.extend(list_14)
print(list_13)  # ['apple', 'banana', 'cherry', 'kiwi', 'orange']