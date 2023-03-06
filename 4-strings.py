
#! Strings

name = 'Pakize'
last_name = 'KILIÇ'
age = '24'

message = "My name is " + name + " " +last_name + ". I am " + age + " years old."

print(message)  # My name is Pakize KILIÇ. I am 24 years old.

#! String Slicing  str[start:stop:step] 
#!                           stop dahil değildir | stop is not included
#!                           step default = 1 

print(message[0])  # M
print(message[-1])  # .
print(message[-3])  # l
print(message[0:7:2])  # M ae
print(message[6:16])  # e is Pakiz
print(message[0:2])  # My
print(message[:2])  # My
print(message[5:])  # me is Pakize KILIÇ. I am 24 years old. 
print(message[-3:-1])  # ld
print(message[-4:])  # old.
print(message[:])  # My name is Pakize KILIÇ. I am 24 years old.
print(message[::-1])  # .dlo sraey 42 ma I .ÇILIK ezikaP si eman yM


#! String Format

productName = "apple"
price = 15
kg = 1.5

# #? msg = kg + " kg of " + productName + " price " + (price * kg) # TypeError: unsupported operand type(s) for +: 'float' and 'str'
msg = str(kg) + " kg of " + productName + " price " + str(price * kg) 
print(msg)  # 1.5 kg of apple price 22.5

msg2 = "{} kg of {} price {}".format(kg, productName, (price * kg))
print(msg2)  # 1.5 kg of apple price 22.5

msg3 = "{1} kg of {2} price {0}".format((price * kg), kg, productName)
print(msg3)  # 1.5 kg of apple price 22.5

msg4 = "{k} kg of {pn} price {pk}".format(pk= price*kg , k=kg, pn=productName)
print(msg4)  # 1.5 kg of apple price 22.5

#! f-string

msg5 = f"{kg} kg of {productName} price {price * kg}"
print(msg5)  # 1.5 kg of apple price 22.5