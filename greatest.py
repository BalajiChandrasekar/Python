num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))
 
if (num1 > num2) and (num1 > num3):
   large = num1
elif (num2 > num1) and (num2 > num3):
   large = num2
else:
   large = num3
 
print("The largest number is",large)
