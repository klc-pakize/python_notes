
#! DICTIONARY : Sınırsız item(öğe) topluluğudur.
#  key: value olarak oluşturulur.
#? key'ler yalnızca tuple gibi immutable(değişmez) değerleri alabilir, value'ler her şeyi alabilir.

#? Oluşturmak:
# 1- {} ==> dict_1 = {"a": 1, "b": 2, "c": 3}  ==> dict_1 = {'a': 1, 'b': 2, 'c': 3}
# 2- dict() ==> dict_2 = dict(a=1, b=2, c=3)  ==> dict_2 = dict(a=1, b=2, c=3)

#! DICTIONARY : It is an unlimited collection of items.
#  It is created as key: value.
#? Keys can only take immutable values such as tuples, values can take anything.

#? To create:# 
# 1- {} ==> dict_1 = {"a": 1, "b": 2, "c": 3}  ==> dict_1 = {'a': 1, 'b': 2, 'c': 3}
# 2- dict() ==> dict_2 = dict(a=1, b=2, c=3)  ==> dict_2 = dict(a=1, b=2, c=3)


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

