
#! DICTIONARY : Sınırsız item(öğe) topluluğudur.
#  key: value olarak oluşturulur.
#? key'ler yalnızca tuple gibi immutable(değişmez) değerleri alabilir, value'ler her şeyi alabilir.

#? Oluşturmak:
# 1- {} ==> dict_1 = {"a": 1, "b": 2, "c": 3}  ==> dict_1 = {'a': 1, 'b': 2, 'c': 3}
# 2- dict() ==> dict_2 = dict(a=1, b=2, c=3)  ==> dict_2 = {'a': 1, 'b': 2, 'c': 3}

#! DICTIONARY : It is an unlimited collection of items.
#  It is created as key: value.
#? Keys can only take immutable values such as tuples, values can take anything.

#? To create:# 
# 1- {} ==> dict_1 = {"a": 1, "b": 2, "c": 3}  ==> dict_1 = {'a': 1, 'b': 2, 'c': 3}
# 2- dict() ==> dict_2 = dict(a=1, b=2, c=3)  ==> dict_2 = {'a': 1, 'b': 2, 'c': 3}


#? Elemana Erişme (Indexing):
city_number_plate = {
    "İstanbul" : 34,
    "İzmir" : 35,
    "Sakarya" : 54,
    "Karadeniz" : ["Rize", 53, "Trabzon", 61],
}

print(f"İstanbul plate: {city_number_plate['İstanbul']}")  # İstanbul plate: 34
print(f"İzmir plate: {city_number_plate['İzmir']}")  # İzmir plate: 35
print(f"Sakarya plate: {city_number_plate['Sakarya']}")  # Sakarya plate: 54
print(f"{city_number_plate['Karadeniz'][0]} plate: {city_number_plate['Karadeniz'][1]}")  # Rize plate: 53


#? nested dictionary:
directory = {
    "Ali Veli" : "12654236",
    "Can Cani" : "565625656",
    "Jhon Joe" : {
        "Home" : "854656535",
        "Job" : "6566464646",
    }
}

print(f"John Joe'nin home phone {directory['Jhon Joe']['Home']}")  # John Joe'nin home phone 854656535


#? Değer Güncelleme (Mutable)
car_brands = {
    "Opel": "Mokka", 
    "Toyota" :"Corolla",
    "Honda" : "Civic",
    "Citroen" : "c4x",
}

car_brands["Opel"] = "Grandland"
print(car_brands)  # {'Opel': 'Grandland', 'Toyota': 'Corolla', 'Honda': 'Civic', 'Citroen': 'c4x'}
car_brands["Honda"] = ["Civic", "City"]
print(car_brands)  # {'Opel': 'Grandland', 'Toyota': 'Corolla', 'Honda': ['Civic', 'City'], 'Citroen': 'c4x'} 

#! Dictionary Metod | Dictionary Method

#? get()
# Dictionary içinden belirtilen key in value sine ulaşmamızı sağlar.
# It allows us to access the key in value specified in the Dictionary.
dictionary_1 = {
    "name" : "Samsung s20",
    "price" : 8000
}

dictionary_1_get = dictionary_1.get("name")
print(dictionary_1_get)  # Samsung s20


#? keys()
# Dictionary içinde bulunan bütün keyleri liste halinde döndürür.
# Returns all keys in Dictionary as a list.
dictionary_2 = {
    "car" : "Jeep",
    "year" : 2023 
}

dictionary_2_keys = dictionary_2.keys()
print(dictionary_2_keys)  # dict_keys(['car', 'year'])


#? values()
# Dictionary içinde bulunan bütün valueleri liste halinde döndürür.
# Returns all values in Dictionary as a list.
dictionary_3 = {
    "book" : "Mor Salkımlı Ev",
    "author" : "Halide Edip Adıvar" 
}

dictionary_3_values = dictionary_3.values()
print(dictionary_3_values)  # dict_values(['Mor Salkımlı Ev', 'Halide Edip Adıvar'])


#? items()
# Dictionary deki tüm key-value çiftlerini döndürür. Bu yöntem, döngülerde dictionary öğeleri üzerinde gezinmek için kullanışlıdır. 
# Returns all key-value pairs in Dictionary. This method is useful for navigating dictionaries in loops.
dictionary_4 = {
    "book" : "Mor Salkımlı Ev",
    "author" : "Halide Edip Adıvar",
    "car" : "Jeep",
    "year" : 2023,  
}

dictionary_4_items = dictionary_4.items()
print(dictionary_4_items)  # dict_items([('book', 'Mor Salkımlı Ev'), ('author', 'Halide Edip Adıvar'), ('car', 'Jeep'), ('year', 2023)])


#? update()
# Dictionary de olmayan bir key/value çifti eklememizi ve değerleri tekrar güncellememizi sağlar.
# It allows us to add a key-value that is not in the dictionary and to update the values again.
dictionary_5 = {
    "language" : "Python",
    "year" : 1990,
}

dictionary_5_update = dictionary_5.update({"language":"JavaScripts"})
print(dictionary_5)  # {'language': 'JavaScripts', 'year': 1990}
dictionary_5["year"] = 1995
print(dictionary_5)  # {'language': 'JavaScripts', 'year': 1995}

dictionary_5_update_2 = dictionary_5.update({"author" : "Brandan Eich"})
print(dictionary_5)  # {'language': 'JavaScripts', 'year': 1990, 'author': 'Brandan Eich'}
dictionary_5["purpose"] = "create web pages"
print(dictionary_5)  # {'language': 'JavaScripts', 'year': 1995, 'author': 'Brandan Eich', 'purpose': 'create web pages'}

#? pop()
# Key/Value silmek için kullanılır
# Used to delete Key/Value
dictionary_6 = {
    "artist" : "Leonardo Da Vinci",
    "work": "Mona Lisa",
}

dictionary_6_pop = dictionary_6.pop("work")
print(dictionary_6_pop)  # Mona Lisa
print(dictionary_6)  # {'artist': 'Leonardo Da Vinci'}


#? clear()
# Dictionary içindeki bütün key/value siler ve bize boş bir dictionary döndürür.
# It deletes all key/values in Dictionary and returns us an empty dictionary.
dictionary_7 = {
    "artist" : "Leonardo Da Vinci",
    "work": "Mona Lisa",
    "language" : "Python",
    "year" : 1990,
}

dictionary_7_clear = dictionary_7.clear()
print(dictionary_7)  # {}


#? del
# Dictionaryi bellekten kalıcı olarak siler, erişmek istersek hata verir.
# Permanently deletes the dictionary from memory, it gives an error if we want to access it.
dictionary_8 = {
    "artist" : "Leonardo Da Vinci",
    "work": "Mona Lisa",
    "language" : "Python",
    "year" : 1990,
}

del dictionary_8
# print(dictionary_8)  #! NameError: name 'dictionary_8' is not defined.


#? copy()
"""
Normal şartlarda bir dictionay'i 2 farklı değişkene atayabiliriz örneğin: 
a = {
    "artist" : "Leonardo Da Vinci",
    "work": "Mona Lisa",
}
b = a
print(a) ==> {
    "artist" : "Leonardo Da Vinci",
    "work": "Mona Lisa",
}
print(b) ==> {
    "artist" : "Leonardo Da Vinci",
    "work": "Mona Lisa",
}
şeklinde olur ama, a dictionary'sinde yaptığımız değişiklik b dictionary'sinde de gerçekleşir, çünkü bu iki değişken bellekte aynı dictionary adresine sahiptir. Bunun yerine copy() metodunu kullanmak gerekmektedir.

Normally we can assign a dictionay to 2 different variables, for example:
a = {
     "artist": "Leonardo Da Vinci",
     "work": "Mona Lisa",
}
b = a
print(a) ==> {
     "artist": "Leonardo Da Vinci",
     "work": "Mona Lisa",
}
print(b) ==> {
     "artist": "Leonardo Da Vinci",
     "work": "Mona Lisa",
}
but the change we make in dictionary a also happens in dictionary b, because these two variables have the same dictionary address in memory. Instead, it is necessary to use the copy() method.
"""
dictionary_9 = {
    "artist" : "Leonardo Da Vinci",
    "language" : "Python",
}

dictionary_9_copy = dictionary_9.copy()
print(dictionary_9_copy)  # {'artist': 'Leonardo Da Vinci', 'language': 'Python'}
dictionary_9_copy.pop("language")
print(dictionary_9_copy)  # {'artist': 'Leonardo Da Vinci'}
print(dictionary_9)  # {'artist': 'Leonardo Da Vinci', 'language': 'Python'}
