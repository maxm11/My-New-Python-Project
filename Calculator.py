print ("--------------------------------------")
print (" ")

print ("Calculator Python Program")
print ("Made by Max, licensed under GPLv3")

print (" ")
print ("--------------------------------------")

num1 = raw_input ("Please enter your first number here : ")

sign = raw_input ("Please enter the operation you want to use [+ - * /]: ")

num2 = raw_input ("Please enter your second number here : ")

def calculation( num1, num2, sign)
{
    ans = 0
    
    if sign == "+":
        num1 + num2 = ans
    
    if sign == "-":
        num1 - num2 = ans
    
    if sign == "*":
        num1 * num2 = ans
    
    if sign == "/":
        num1 / num2 = ans
    
    return ans
}

print ("The answer is : " + ans)