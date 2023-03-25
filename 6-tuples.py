
#! TUPLES 
#? List gibidir tek farkı immutable'dir, yani değerleri güncellenmez.
#  Farklı veri tipleri aynı tuple içinde olabilir: (str, int, bool, float, list, set, dictionary)
#? Parantez koymaya gerek yoktur, birden fazla eleman var ise sadece virgül ile ayırmak yeterlidir: "a",1, 4, 4
#  Tek elemanlı bir tuple yapılmak isteniyorsa elemanın sonunda mutlaka virgül olmalıdır: (122,)
#? Elemanlar tekrarlanabilir ("a","b","a","a")

#? Oluşturmak:
# 1- () ==> name = "AYŞE" ==> tuple_1 = (name,) ==> ('AYŞE',)
# 2- tuple() ==> name = "AYŞE" ==> tuple_2 = tuple(name) ==> ('A', 'Y', 'Ş', 'E')

#! TUPLES 
#? It's like a List, except it's immutable, so its values are not updated.
#  Different data types can be in the same tuple: (str, int, bool, float, list, set, dictionary)
#? There is no need to put parentheses, if there is more than one element, it is sufficient to separate them with a comma: "a",1, 4, 4
#  If a single element tuple is desired, there must be a comma at the end of the element: (122,)
#? Elements are repeatable: ("a","b","a","a")


#? To create:
# 1- () ==> name = "AYŞE" ==> tuple_1 = (name,) ==> ('AYŞE',)
# 2- tuple() ==> name = "AYŞE" ==> tuple_2 = tuple(name) ==> ('A', 'Y', 'Ş', 'E')


#? Elemana Erişme (Indexing):
names = "Ali", "Veli", "Deli"
notes = 70, 80, 90

print(f"{names[0]} student's grade is {notes[0]}")  # Ali student's grade is 70
print(f"{names[1]} student's grade is {notes[1]}")  # Veli student's grade is 80  
print(f"{names[2]} student's grade is {notes[2]}")  # Deli student's grade is 90

#? nested tuple:
student = (
    ("Ali",70),
    ("Veli",80),
    ("Deli",90),
)

print(f"{student[0][0]} student's grade is {student[0][1]}")  # Ali student's grade is 70
print(f"{student[1][0]} student's grade is {student[1][1]}")  # Veli student's grade is 80
print(f"{student[2][0]} student's grade is {student[2][1]}")  # Deli student's grade is 90

#? Parçalama (Slicing):
car_brands = "Opel", "Dacia", "Mazda", "Toyota"

print(car_brands[0:3])  # ('Opel', 'Dacia', 'Mazda')
print(car_brands[:2])  # ('Opel', 'Dacia')  #? Başlangıç index numarası verilmez ise default olarak 0'dır | If the starting index number is not given, it is 0 by default.
print(car_brands[0:])  # ('Opel', 'Dacia', 'Mazda', 'Toyota')  #? Bitiş index numarası verilmez ise default olarak son index numarası + 1 'dir | If the end index number is not given, the last index number is + 1 by default.
print(car_brands[::-1])  # ('Toyota', 'Mazda', 'Dacia', 'Opel')


#? len()
# Tuple kaç elemandan oluştuğunu döndürür | Returns how many elements the tuple consists of
tuple_1 = (1, "s", 5, True, [2,"can"])
tuple_1_len = len(tuple_1)
print(tuple_1_len)  # 5


#? count()
# Tuple içinde, belirtilen öğenin kaç kez tekrarlandığını sayar ve sonucu döndürür. Var olmayan bir değer girilirse 0 döndürür.
#  Counts how many times the specified element is repeated in the tuple and orients the result. Return 0 if a non-existent value is entered
tuple_2 = (1, 1, 86, 1, 89, "1", False, (1,"b"))
tuple_2_count = tuple_2.count(1)
tuple_2_count2 = tuple_2.count("b")
print(tuple_2_count)  # 3
print(tuple_2_count2)  # 0


#? index()
# Tuple içinde, belirtilen öğenin bulunduğu ilk konumun indeks numarasını döndürür | Returns the index number of the first position in the tuple where the specified item is located
tuple_3 = (1, 8, 40, "pro", ("1","one"))
tuple_3_index = tuple_3.index(("1","one"))
print(tuple_3_index)  # 4