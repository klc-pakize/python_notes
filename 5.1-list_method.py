
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
# aynı değerden birden fazla varsa ilk karşılaştığı değeri siler ve durur, if there is more than one of the same value, it deletes the first value it encounters and stops
# olmayan değer verildiğinde hata verir. | It gives an error when a non-existent value is given.
list_4 = [1, 2, "3", False, "12", False]
list_4_remove= list_4.remove(False)
print(list_4)  # [1, 2, "3", "12", False]


#? pop()
# Listeden index numarasına göre eleman siler, | It deletes element from the list by index number, 
# sildiği elemanı döndürür ve dönen elemanla işlem yapabiliriz. | It returns the element it deleted and we can manipulate the returned element.
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
