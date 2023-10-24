def add(num1,num2):
   return num1+num2
def subtract(num1,num2):
   return num1-num2
def multiplication(num1,num2):
   return num1*num2
def division(num1,num2):
   return num1/num2
print("please select operation -\n"  "1.ADDITION\n" "2.SUBTRACTION\n" "3.MULTIPLICATION\n" "4.DIVISION\n")
select=int(input("select operation 1,2,3,4:"))
number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
if select==1:
   print(number1,"+",number2,"=",add(number1,number2))
elif select==2:
   print(number1,"_",number2,"=",subtract(number1,number2))
elif select==3:
   print(number1,"*",number2,"=",multiplication(number1,number2))
elif select==4:
   print(number1,"/",number2,"=",division(number1,number2))
else:
   print("invalidinput")
