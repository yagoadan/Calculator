import Library.Functions
import Library.ASCII
import time


def userchoice():
 time.sleep(4)
 print(Library.ASCII.instructions)
 choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/exit): ")
 print (" ")
 
 if choice == '1':
   print("Number of terms?")
   print("number(1) + number(2)")
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(" ")

 elif choice == '2':
   print("number(1) - number(2)")
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(" ")

 elif choice == '3':
   print("number(1) x number(2)")
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(" ")

 elif choice == '4':
   print("number(1) divided by number(2)")
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(" ")

 elif choice == '5':
   print("number(1) Base(2)")
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(" ")

 elif choice == '6':
   print("number(1), number(2) = power")
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(" ")

 elif choice == '7':
   print("number(1) = numerator, number(2) = denominator")
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(" ")
  
 elif choice == '8':
   print("number (1) = number want to root, number (2) = root")
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number:"))
   print(" ")

 elif choice == '9':
   choice2 = input('triangle /circle/ rectangle ')
   print(" ")
   if choice2 == 'triangle':
      print("Base, Height")
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
   elif choice2 == "circle":
      print("Radius")
      num1 = float(input("Enter first number: "))
      print(" ")

 elif choice == '10':
   print(Library.ASCII.math1)
   choice3 = input('(1/2/3/4): ')
   print(" ")
   if choice3 == "1":
      print("Add and then subtract")
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      num3 = float(input("Enter third number: "))
      num4 = float(input("Enter fourth number: "))
    
   elif choice3 == "2" :
      print("Add and then multiply")
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      num3 = float(input("Enter third number: "))
      num4 = float(input("Enter fourth number: "))
      print(" ")

   elif choice3 == "3":
      print("Add and then divide")
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      num3 = float(input("Enter third number: "))
      num4 = float(input("Enter fourth number: "))
      print(" ")

 elif choice == "exit":
    Library.Functions.end()
      
 else:
   print("Invalid input")
 
 print("Calculation")  
 if choice == '1':
   print(num1,"+",num2,"=", Library.Functions.add(num1,num2))

 elif choice == '2':
   print(num1,"-",num2,"=", Library.Functions.subtract(num1,num2))

 elif choice == '3':
   print(num1,"x",num2,"=", Library.Functions.multiply(num1,num2))

 elif choice == '4':
   print(num1,"÷",num2,"=", Library.Functions.divide(num1,num2))

 elif choice == '5':
   print ("Log",num2, num1, "=", Library.Functions.log(num1,num2))

 elif choice == '6':
   print (num1, "^",num2, "=", Library.Functions.power(num1,num2))

 elif choice == "7":
   print (num1, "/",num2, "*", 100, "=", Library.Functions.percent(num1,num2), "%")

 elif choice == '8':
   print ( num2,"√", num1, "=", Library.Functions.nth_root(num1,num2))

 elif choice == '9':
   if choice2 == 'triangle':
    print ("(", num1, "x", num2, ")","/", 2, "=", Library.Functions.Atriangle(num1,num2))
   elif choice2 == "circle":
    print ("π", "x", num1, "^", 2, "=", Library.Functions.Acircle(num1))
    
 elif choice == '10':
    if choice3 == '1':
      print("(", num1, "+", num2, ")", "-", "(", num3, "+", num4, ")", "=", Library.Functions.combine1(num1,num2,num3,num4))
    elif choice3 == '2':
      print("(", num1, "+", num2, ")", "x", "(", num3, "+", num4, ")", "=", Library.Functions.combine2(num1,num2,num3,num4))
    elif choice3 == '3':
      print("(", num1, "+", num2, ")", "/", "(", num3, "+", num4, ")", "=", Library.Functions.combine3(num1,num2,num3,num4)) 
 elif choice == "exit":
    Library.Functions.end()
    
 else:
   print("Invalid input")

