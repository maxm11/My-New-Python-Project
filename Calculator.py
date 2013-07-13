print ("--------------------------------------")
print (" ")

print ("Calculator Python Program")
print ("Made by Max, licensed under GPLv3")

print (" ")
print ("--------------------------------------")

num1str = raw_input ("Please enter your first number here : ")

sign = raw_input ("Please enter the operation you want to use [+ - * /]: ")

num2str = raw_input ("Please enter your second number here : ")

num1 = int (num1str)
num2 = int (num2str)
    
if sign == "+":
    ans = num1 + num2
    
if sign == "-":
    ans = num1 - num2
    
if sign == "*":
    ans = num1 * num2
    
if sign == "/":
    ans = num1 / num2
    

print ("The answer is : "), ans