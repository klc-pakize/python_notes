
#!Değişken Tanımlama:
#? Geçici olarak bir veri sakladığımız alana Değişken denilebilir.

#! Değişken Tanımlama kuralları:
#  1- Türkçe karakter içermemesi tavsiye edilir.
#? 2- Sayı ile başlanmamalıdır. Harf veya _ ile başlamalıdır.
#  3- karakterler arasında boşluk olmamalıdır.
#? 4- Büyük küçük harf duyarlılığı vardır.
#  5- Keywordler değişken ismi olarak kullanılamaz. help('keywords') ile bu keywordslere ulaşabilirz

#! Variable Identification:
#? The field where we temporarily store data can be called a Variable.

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

a, b, c = 10, 20, 30
print(a)  # 10
print(b)  # 20
print(c)  # 30


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



