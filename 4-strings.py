
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
 