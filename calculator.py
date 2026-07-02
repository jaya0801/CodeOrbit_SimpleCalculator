#calculaor
#menu
print("1.Add")
print("2.Subtraction")
print("3.Multiplication")
print("4.Dicision")
print("5.Modulus")
print("6.Floor Division")
print("7.Exponent")
while True:
 try:
     #user input
  choice=int(input("Enter the 1 to 7 choices:"))
  num1=int(input("Enter the First Number :"))
  num2=int(input("Enter the Second Number:"))
 
    #function

  def add(num1,num2):
   return num1+num2
   
  def substraction(num1,num2):
   return num1-num2
  def multiplication(num1,num2):
   return num1*num2
  def division(num1,num2):
   return num1/num2
  def modulus(num1,num2):
   return num1%num2
  def floorDivision (num1,num2):
     return num1//num2
  def exponent(num1,num2):   
    return num1**num2
    #checking condition
  if choice==1:
   print("Result:",add(num1,num2))
  elif choice==2:
   print("Result:", substraction(num1,num2))

  elif choice==3:
    print( "Result:",multiplication(num1,num2))
  elif choice==4:
    print("Result:", division(num1,num2))
  elif choice==5:
    print("Result:", modulus(num1,num2))
  elif choice==6:
    print("Result:", floorDivision(num1,num2))
  elif choice==7:
    print("Result:",exponent(num1,num2))
  else:
    print("Please choose correct choice")
     #handle error
 except ZeroDivisionError:
    print("Cannot divide by zero ,please enter correctly")
 except ValueError :
    print("Please enter valid number")
 finally:
    print("Thanking you")
