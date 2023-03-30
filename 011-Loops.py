
#! Loops (while - for) Neden ihtiyaç duyarız ? | Why do we need ?

products = ["iphone 11", "iphone 12", "iphone 13", "samsung s22", "iphone 14"]
print(products[0])  # iphone 11
print(products[1])  # iphone 12
print(products[2])  # iphone 13
print(products[3])  # samsung s22
print(products[4])  # iphone 14
#! Bu işlem tekrarlayan bir işlemdir, bunun yerine döngülerden for döngüsünü kullanabiliriz. Kod yazarken en temel kurallardan birinin tekrara düşmemek olduğunu söyleyebiliriz.
#! This operation is a repetitive operation, instead we can use the for loop from the loops. We can say that one of the most basic rules is not to fall into repetition while writing code.

for pro in products:
    print(pro)  # iphone 11
                # iphone 12
                # iphone 13
                # samsung s22
                # iphone 14

#! while : While döngüsü, belirli bir koşul doğru olduğu sürece tekrar eden bir döngüdür. 
# syntax:
#        while condition:    ====> #? condition şart anlamına gelir, 
#           body                   #? condition == True ise body kısmı çalışır False olduğunda döngü durur.

#! while : A while loop is a loop that repeats as long as a certain condition is true.
# syntax:
#        while condition:    ====>  #? If condition == True, the body part works. If it is False, the loop stops.
#           body                  


x = int(input("number: "))

while x > 0:
    print("Enter number")
    x = int(input("number: "))
print("You did not enter a number matching the condition.")



#! for : For döngüsü, bir koleksiyondaki elemanların her biri üzerinde belirli bir işlem yapmak için kullanılan bir döngüdür.
# syntax:
#        for i in ___:   
#           body           

#! for : A for loop is a loop used to perform a specific operation on each of the elements in a collection.
# syntax:
#        for i in ___:   
#           body 

for c in "hey":
    print(c)  # h
              # e
              # y

#? range(): 
# Belirli bir aralıkta sayılar üretir. Örneğin, 
# "for i in range(5):" ifadesi, i değişkenine 0 ile 4 arasındaki sayıları atayarak çalışır.
# Generates numbers in a specified range. For example, the statement 
# "for i in range(5):" works by assigning the numbers 0 to 4 to the variable i.

for a in range(3,15):  # 3 = start, 15 = stop, 1 = default step 
    print(a)  # 3
              # 4
              # 5
              # 6
              # 7
              # 8
              # 9
              # 10
              # 11
              # 12
              # 13
              # 14
           
sum = 0
for y in range(10):
    sum = sum + y  # sum = sum + y == sum += y
    print(sum)  # 0
                # 1
                # 3
                # 6
                # 10
                # 15
                # 21
                # 28
                # 36
                # 45

base = 1
for i in range(5):
    base *= 5
    print(base)  # 5
                 # 25
                 # 125
                 # 625
                 # 3125

# i değerini kullanmadığımız zamanlar olabilir, bu durumlarda i yerine _ kullanabiliriz.
# There may be times when we do not use the value i, in which cases we can use _ instead of i.
base = 1
for _ in range(5):
    base *= 5
    print(base)  # 5
                 # 25
                 # 125
                 # 625
                 # 3125


#? enumerate(): 
# Bir dizi, list veya tuple içindeki elemanları hem elemanın kendisi hem de elemanın indeksi ile birlikte döndürür. Örneğin, 
# "for index, value in enumerate(my_list):" ifadesi, my_list içindeki her bir elemanın hem kendisini hem de indeksini index ve value değişkenlerine atayarak çalışır.
# Returns the elements in an array, list, or tuple, along with the element itself and the element's index. For example,
# The statement "for index, value in enumerate(my_list):" works by assigning both itself and its index to each element in my_list to the variables index and value.

my_list = ['apple', 'banane', 'pear']
for index, value in enumerate(my_list):
    print(f"{index}: {value}")  # 0: apple
                                # 1: banane
                                # 2: pear


#? zip(): 
# Birden fazla dizi, liste veya tuple eşleştirerek her bir elemanın karşılıklı elemanları ile birlikte döndürür. Örneğin, 
# "for x, y in zip(list1, list2):" ifadesi, list1 ve list2 içindeki elemanları sırayla x ve y değişkenlerine atayarak çalışır.
# Matches multiple arrays, lists, or tuples and returns each element with its corresponding elements. For example,
# The statement "for x, y in zip(list1, list2):" works by assigning the elements in list1 and list2 to x and y respectively.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for x, y in zip(list1, list2):
    print(f"{x}: {y}")  # 1: a
                        # 2: b
                        # 3: c


#? reversed(): 
# Bir dizi, liste veya tuple elemanlarını tersten döndürür. Örneğin, 
# "for i in reversed(my_list):" ifadesi, my_list içindeki elemanları tersten döndürerek i değişkenine atayarak çalışır.
# Reverses the elements of an array, list, or tuple. For example,
# The statement "for i in reversed(my_list):" works by reversing the elements in my_list and assigning them to the variable i.

my_list = ['cat', 'dog', 'chicken']
for i in reversed(my_list):
    print(i)  # chicken
              # dog
              # cat


#? dict. with for loop

tel = [
    {"product_name":"iphone 12", "product_price": 20000},
    {"product_name":"iphone 12 Pro", "product_price": 25000},
    {"product_name":"iphone 13", "product_price": 35000},
    {"product_name":"iphone 13 Pro", "product_price": 45000},
]

sum = 0
for t in tel:
    print(t)  # {'product_name': 'iphone 12', 'product_price': 20000}
    print(t["product_name"])  # iphone 12
    sum += t["product_price"]
print(sum)  # 125000



#? break: 
# Döngüyü aniden sonlandırmak için kullanılır. Belirli bir koşul sağlandığında döngüyü tamamen durdurur.
# Used to abruptly terminate the loop. It stops the loop completely when a certain condition is met.

for i in range(2,10,2):
    if i == 8:
        break
    print(i)  # 2
              # 4
              # 6

x = 0
while x < 10:
    x += 1
    if x == 5:
        break
    print(x)  # 1
              # 2
              # 3
              # 4


#? continue: 
# Döngünün o anki turunu atlamak için kullanılır. Belirli bir koşul sağlandığında o turda geri kalan kodları atlar ve döngünün sonraki turuna geçer.
# Used to skip the current round of the loop. When a certain condition is met, it skips the remaining codes in that round and moves on to the next round of the loop.
for i in range(4):
    if i == 2:
        continue
    print(i)  # 0
              # 1
              # 3
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)  # 1
              # 2
              # 4
              # 5


#? pass: 
# Döngü içinde herhangi bir işlem yapmadan devam etmek için kullanılır. Genellikle, döngü yapısını oluştururken henüz içeriği belirlemediğimiz durumlarda kullanılır.
# It is used to continue without any action inside the loop. It is often used when we have not yet specified the context when creating the loop structure.
a = 0
while a >= 5:
    pass 

for k in range(1,100,5):
    pass