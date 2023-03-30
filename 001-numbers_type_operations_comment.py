
#! İki tip sayı türü vardır.
#? 1- Integer (int) = Tam sayıları ifade eder.
#  2- Float (float) = Ondalıklı sayıları ifade eder.

#! There are two types of numbers.
#? 1- Integer (int) = Expresses integers.
#  2- Float (float) = Expresses decimal numbers.

#! Tip Kontrolü:
# type() içine yazılan her şeyin tipini döndürür.

#! Type Check:
# Returns the type of everything typed in type() .

type(3)  # <class 'int'>
type(3.0)  # <class 'float'>


#! Temel İşlemler:
#? + : Toplama İşlemi
# - : Çıkarma İşlemi
#? / : Bölme İşlemi
# * : Çaprma İşlemi
#? ** : Üssü İşlemi
# % : Mod İşlemi
#? // : Tam Bölme İşlemi

#! Basic Operations:
#? + : Addition Operation
# - : Subtraction
#? / : Division
# * : Multiplication
#? ** : Base Operation
# % : Mod Operation
#? // : Complete Division

#! Not: Bölme işleminin sonucu her zaman float.
#! Not: İşlem önceliği parantez, bölme, çarpma, toplama, çıkarmadır.
#! Note: The result of division is always float.
#! Note: Operation priority is parentheses, division, multiplication, addition, subtraction.

3 + 3  # 6 type(3 + 3) <class 'int'> 
3.0 + 3  # 6.0 type(3.0 + 3) <class 'float'>
4 - 1  # 3 type(4 - 1) <class 'int'>
4 - 1.0  # 3.0 type(4 - 1.0) <class 'float'>
10 / 3  # 3.3333333333333335 type(10 / 3) <class 'float'>
10 / 5  # 2.0 type(10 / 5) <class 'float'>
2 ** 3  # 8 type(2 ** 3) <class 'int'>
2 ** 3.0  # 8.0 type(2 ** 3.0) <class 'float'>
10.0 % 2  # 0.0 tpye(10.0 % 2) <class 'float'>
10 % 2  # 0 type(10 % 2) <class 'int'>
10 // 3 # 3 type(10 // 3) <class 'int'>
10.0 // 3  # 3.0 type(10.0 // 3) <class 'float'>

#! Not: Bir işlemde herhangi bir sayının türü float ise, işlemin sonucu her zaman float olacaktır.
#! Note: If the type of any number is float in an operation, the result of the operation will always be float.


#! Yorum Satırı:
"""
- Yorum satırı eklemek için '#' satır bu işaret ile başlamalıdır. Satır içi yorumlarda # işaretinden önce 2 boşlup # işaretinden sonra 1 boşluk bırakılmalıdır.
- Çok uzun bir yazıyı yoruma almak isetsek başına ve sonun 3 adet " işareti eklemeliyiz.
"""

#! Comment Line:
"""
- To add a comment line, the '#' line must start with this sign. Inline comments must have 2 spaces before the # sign and 1 space after the # sign.
- If we want to comment a very long article, we should add 3 "" signs at the beginning and at the end.
"""