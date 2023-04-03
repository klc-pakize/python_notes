
#!Değişken Tanımlama:
#? Geçici olarak bir veri sakladığımız alana Değişken denilebilir.

#  Değişkenlerin belirli bir türle bildirilmesi gerekmez ve hatta ayarlandıktan sonra türü değiştirebilirler.
x = 4       # x type = int
print(x)  # 4
x = "Sally" # x type = str
print(x)  # "Sally"

#? Bir değişkenin veri tipini belirtmek istiyorsanız, bu Casting ile yapılabilir.
x = str(3)    # x will be '3'
print(type(x))  # <class 'str'>
y = int(3)    # y will be 3
print(type(y))  # <class 'int'>
z = float(3)  # z will be 3.0
print(type(z))  # <class 'float'>

#! Değişken Tanımlama kuralları:
#  1- Türkçe karakter içermemesi tavsiye edilir.
#? 2- Sayı ile başlanmamalıdır. Harf veya _ ile başlamalıdır.
#  3- karakterler arasında boşluk olmamalıdır.
#? 4- Büyük küçük harf duyarlılığı vardır.
#  5- Keywordler değişken ismi olarak kullanılamaz. help('keywords') ile bu keywordslere ulaşabilirz

#! Variable Identification:
#? The field where we temporarily store data can be called a Variable.
# Variables don't need to be declared with a specific type, and they can even change the type once set.
#? If you want to specify the data type of a variable, this can be done with casting.

#! Variable Declaration rules:
#  1- It is recommended not to contain Turkish characters.
#? 2- It should not start with a number. It must start with a letter or _.
#  3- There should be no spaces between characters.
#? 4- It is case sensitive.
#  5- Keywords cannot be used as variable names. We can access these keywords with help('keywords')

number = 1  # ==> ✔️

# 1number = 1 ==> ✖️

# 1 = b ==> ✖️

# İstanbul = 34 ==> ✖️

# number two = 2 ==> ✖️

# number@ = 3 ==> ✖️

# number-four = 4 ==> ✖️

number_five = 5  # ==> ✔️

# for = 6  # ==> ✖️

#? Python, bir satırda birden çok değişkene değer atamanıza izin verir: | Python allows you to assign values to multiple variables in one line:
#! Not: Değişken sayısının değer sayısıyla eşleştiğinden emin olun, aksi takdirde bir hata alırsınız. | Note: Make sure the variable count matches the value count, otherwise you'll get an error.
a, b, c = 10, 20, 30
print(a)  # 10
print(b)  # 20
print(c)  # 30

#? Aynı değeri tek bir satırda birden çok değişkene atayabilirsiniz : | You can assign the same value to multiple variables in a single line:
x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange


#! Değişken Çıktısı | Output Variables
#? Python print() işlevi genellikle değişkenleri çıktısını görüntülemek için kullanılır. | The Python print() function is often used to display the output of variables.
x = "Python is awesome"
print(x)  # Python is awesome

# İşlevde print(), virgülle ayırarak birden çok değişken çıktısı alırsınız: | In the function print() you output multiple variables separated by commas:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  # Python is 100

#? Birden fazla değişkenin çıktısını almak için operatörü de kullanabilirsiniz +: | You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  # Python is awesome

# İşlevde print(), bir diziyi ve bir sayıyı operatörle birleştirmeye çalıştığınızda + , Python size bir hata verecektir:
# In the function print() , when you try to concatenate an array and a number with the operator + , Python will give you an error:
x = 5
y = "John"
# print(x + y)

#? İşlevde birden çok değişken çıktısı almanın en iyi yolu, print() bunları farklı veri türlerini bile destekleyen virgüllerle ayırmaktır:
#? The best way to output multiple variables in the function print() is to separate them with commas, which even supports different data types:
x = 5
y = "John"
print(x, y)


"""
Neden Değişken Kullanmalıyız?
Bir senaryo düşünelim, bir e-ticaret sitemiz var ve ürünleri aldığımız fiyata ek olarak biraz kar elde etmek için fiyatı yükselteceğiz:
"""
"""
Why Should We Use Variables?
Let's imagine a scenario, we have an e-commerce site and we will raise the price to get some profit in addition to the price we bought the products:
"""

print(500 + (500 * 0.18))  # 590.0

"""
Şimdi toptancıdan aldığımız 500 fiyatına zam geldi ve bizde bu tarz çok ürün var ve birden fazla yerde geçmektedir. Hepsini tek tek hesaplamamız gerekecek. Bu ürünlerin fiyatlarını bir değişkene atayıp bu değişken adı ile formül ticaretini yaparsak kendimizi daha az tekrar ederiz ve zaman kazanırız vb. tasarruf ederiz.
"""
"""
Now, the price of 500 we bought from the wholesaler has increased, and we have many such products and they are in more than one place. We will have to calculate them one by one. If we assign the prices of these products to a variable and trade formulas with that variable name, we will repeat ourselves less and save time, etc. we save.
"""

productA = 800
profit = 0.18
print(productA + (productA * profit))  # 944.0



