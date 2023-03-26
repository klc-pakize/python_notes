
#! SETS : Kümeler gibi düşünülebilir.
#  - Sıralanamaz
#? - Elemanlar tekrar edemez, her eleman unic
#  - Elemanlar değiştirilemez
#? - Farklı veri tipleri aynı sets içinde olabilir: {str, int, bool, float, tuple, list, dictionary}
#  - List ve Dictionary göre daha performanslıdır
#? İndexlenemez

#? Oluşturmak:
# 1- {} ==> set_1 = { 1, "b", 2}  ==> set_1 = {1, 2, 'b'}
# 2- set() ==> set_2 = set([ 1, 2, 3, ("4","dört",4)])  ==> set_2 = {1, 2, 3, ('4', 'dört', 4)}

#! SETS : Can be thought of as sets.
#  - Unsortable
#? - Elements cannot repeat, each element is unic
#  - Elements cannot be changed
#? - Different data types can be in the same sets: {str, int, bool, float, tuple, list, dictionary}
#  - Better performance than List and Dictionary
#? - Cannot be indexed

#? To create:
#1 1- {} ==> set_1 = { 1, "b", 2} ==> set_1 = {1, 2, 'b'}
#2 2- set() ==> set_2 = set([ 1, 2, 3, ("4","four",4)]) ==> set_2 = {1, 2, 3, ('4', 'four', 4)}

#? add() 
# Bir elemanı sete ekler.
# Adds an element to the set.
set_1 = {1, 2, 3, 4, 5}

set_1_add = set_1.add(6)
print(set_1)  # {1, 2, 3, 4, 5, 6}


#? clear() 
# setin tüm elemanlarını siler.
# deletes all elements of the set.
set_2 = {1, "2", 2.8, 4,"5"}

set_2_clear = set_2.clear()
print(set_2)  # set()


#? copy() 
# setin bir kopyasını oluşturur.
# creates a copy of the set.
set_3 = {1, "2", 2.8, 4,"5", ("a","b")}

set_3_copy = set_3.copy()
print(set_3_copy)  # {'5', 1, 2.8, 4, ('a', 'b'), '2'}


#? difference() 
# set ve diğer bir set arasındaki farkları döndürür.
# returns the differences between a set and another set.
set_4 = {1, "2", 2.8, 4,"5", ("a","b")}
set_5 = {0, "2", 2.8, 4, 5, ("a","b")}

diff_set = set_4.difference(set_5)
print(diff_set)  # {1, '5'}


#? discard() 
# bir elemanı setten siler. Eğer eleman sette yoksa, hiçbir şey yapmaz.
# deletes an element from the set. If the element is not in the set, it does nothing.
set_6 = {1, "2", 2, 4,"5", ("a","b")}

set_6_discard = set_6.discard(2)
print(set_6)  # {1, '2', 4, ('a', 'b'), '5'}


#? union()
#  setleri birleştirir ve yeni bir set oluşturur.
# merges the sets and creates a new set.
set_7 = {1, "2", 2, 4,"5", ("a","b")}
set_7_1 = {1, ("a",56)}

set_union = set_7.union(set_7_1)
print(set_union)  # {1, 2, ('a', 'b'), 4, '2', '5', ('a', 56)}


#? intersection()
#  setlerin kesişimini döndürür.
# returns the intersection of the sets.
set_8 = {1, "2", 2, 4,"5", ("a","b")}
set_8_1 = {50.78, "can", ("a","b")}

set_intersection = set_8.intersection(set_8_1)
print(set_intersection)  # {('a', 'b')}


#? symmetric_difference()
#  setlerin simetrik farklarını döndürür
# returns the symmetric differences of sets
set_9 = {1, "2", 2, 4,"5", ("a","b")}
set_9_1 = {50.78, "can", ("a","b")}

set_symmetric_difference = set_9.symmetric_difference(set_9_1)
print(set_symmetric_difference)  # {1, 2, 4, '5', 'can', '2', 50.78}


#? remove()
#  bir elemanı setten siler. Eğer eleman sette yoksa, KeyError hatası verir.
# deletes an element from the set. If the element is not in the set, it throws a KeyError.
set_10 = { "a", 87}

set_10_remove = set_10.remove("a")
print(set_10)  # {87}


#? pop()
#  setin rastgele bir elemanını siler ve o elemanı döndürür.
# deletes a random element of the set and returns that element.
set_11 = {1, "a","b"}

set_11_pop = set_11.pop()
print(set_11_pop)  # 1


#? update()
#  bir seti diğer set ile birleştirir.
# combines one set with another set.
set_12 = {1, "2", 2, 4,"5", ("a","b")}

set_12_update = set_12.update(["apple", "cat"])
print(set_12)  # {1, 2, '2', 4, ('a', 'b'), 'apple', 'cat', '5'}

