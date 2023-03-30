
#! if : if bloğu, belirli bir koşulun True olması durumunda çalışacak olan kod bloğudur.
# syntax:
#        if condition:    ====> #? condition şart anlamına gelir, 
#           body                #? condition == True ise body kısmı çalışır

#! if : The if block is the code block that will run if a certain condition is True.
# syntax:
#       if condition:     ====> #? If condition == True, body part works
#           body            

x = int(input("number: "))
if x % 2 == 0:
    print("The number is even")
print("The program has come to an end")


#! else : else bloğu, tüm önceki koşullar False olduğunda çalışacak olan son bir alternatif kod bloğudur.
#! else : The else block is a final alternative code block that will run when all previous conditions are False.
# syntax:
#       else:
#           body    

number = int(input("number: "))

if number > 0:
    print("Number is positive")

else:
    print("Number is negative")


#! elif: elif bloğu, bir if bloğundan sonra kullanılan ve if bloğundaki koşulun False olduğu durumlarda ek bir koşul testi yapmak için kullanılan bir kontrol yapısıdır.
# syntax:
#        elif condition:    ====> #? condition şart anlamına gelir, 
#           body                #? condition == True ise body kısmı çalışır


#! elif: The elif block is a control structure used after an if block to perform an additional condition test when the condition in the if block is False.
# syntax:
#       elif condition:     ====> #? elif condition == True, body part works
#           body 

number1 = int(input("number: "))
number2 = int(input("number: "))
number3 = int(input("number: "))

if (number1 > number2) and (number1 > number3):
    print(f"biggest number {number1}")

elif (number2 > number1) and (number2 > number3):
    print(f"biggest number {number2}")

else:
    print(f"biggest number {number3}")



#? İçiçe Koşullar | Nested Condition:

name_group = ["Ali", "Veli", "Selin"]
name = input("name: ")

if name in name_group:
    if name == "Ali":
        print("Ali is happy")
    
    elif name == "Selin":
        print("Selin is happy")

    else:
        print("Veli is happy")
else:
    print("This name is not on the list")


#? Ternary Condition:
z = input('x = 2, Y/n: ')
x = 2 if z == 'Y' else 0
print(x)  
