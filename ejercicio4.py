num1 = int(input("Numero uno:"))
num2 = int(input("Numero dos:"))
num3 = int(input("Numero tres:"))

if num1 > num2  and num1 > num3:
    print ("El numero mayor es :",num1)
    
elif num2 > num1 and num2 > num3:
    print("El numero mayor es :", num2)
    
else:
    print("El numero mayor es:", num3)
