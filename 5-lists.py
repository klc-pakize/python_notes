
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
#  1- List
#? 2- Tuple
#  3- Set
#? 4- Dictionary 

#! Array Types in Python:
#  1- List
#? 2- Tuple
#  3- Set
#? 4- Dictionary

#************************************************************************************

#! LIST: Birden çok veriyi gruplama ve bir arada tutma
#? - [] ile gösterilir
#  - Sıralanabilir
#? - Elemanlar tekrarlanabilir ["a","b","a","a"]
#  - Elemanlar değiştirilebilir
#? - Farklı veri tipleri aynı list içinde olabilir 
#  - list içinde list tanımlanabilir (nested list)

#? Oluşturmak
# 1- [] ==> name = "AYŞE" ==> list_1 = [name] ==> ["AYŞE"]
# 2- list() ==> name = "AYŞE" ==> list_2 = list(name) ==> ["A", "Y", "Ş", "E"]

#! LIST: Grouping and keeping multiple data together
#? - Denoted by []
#  - Sortable
#? - Elements are repeatable: ["a","b","a","a"]
#  - Elements can be changed
#? - Different data types can be in the same list: [str, int, bool, float]
#  - list can be defined in list (nested list)

#? To create
# 1- [] ==> name = "AYŞE" ==> list_1 = [name] ==> ["AYŞE"]
# 2- list() ==> name = "AYŞE" ==> list_2 = list(name) ==> ["A", "Y", "Ş", "E"]

names = ["Ali", "Veli", "Deli"]
notes = [70, 80, 90]

print(f"{names[0]} student's grade is {notes[0]}")  # Ali student's grade is 70
print(f"{names[1]} student's grade is {notes[1]}")  # Veli student's grade is 80  
print(f"{names[2]} student's grade is {notes[2]}")  # Deli student's grade is 90


# nested list:
student = [
    ["Ali",70],
    ["Veli",80],
    ["Deli",90],
]

print(f"{student[0][0]} student's grade is {student[0][1]}")  # Ali student's grade is 70
print(f"{student[1][0]} student's grade is {student[1][1]}")  # Veli student's grade is 80
print(f"{student[2][0]} student's grade is {student[2][1]}")  # Deli student's grade is 90



car_brands = ["Opel", "Dacia", "Mazda", "Toyota"]

print(car_brands[0:3])  # ["Opel", "Dacia", "Mazda"]
print(car_brands[:2])  # ["Opel", "Dacia"]  #? Başlangıç index numarası verilmez ise default olarak 0'dır | If the starting index number is not given, it is 0 by default.
print(car_brands[0:])  # ["Opel", "Dacia", "Mazda", "Toyota"]  #? Bitiş index numarası verilmez ise default olarak son index numarası + 1 'dir | If the end index number is not given, the last index number is + 1 by default.
print(car_brands[::-1])  # ['Toyota', 'Mazda', 'Dacia', 'Opel']

# Elemanlar değiştirilebilir (Elements can be changed)
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