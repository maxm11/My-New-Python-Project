print ("--------------------------------------")
print (" ")

print ("Advanced Quick Calculator")
print ("By Max M, licenced under GPLv3")

print (" ")
print ("--------------------------------------")
print (" ")

print ("The format to use this is as follows.")
print ("1234")
print ("+ - * /")
print ("1234")

print (" ")
print ("--------------------------------------")

##Start of the Number entering system
print ("Please enter in the format shown above.")
num1 = raw_input (":")
oper = raw_input (":")
num2 = raw_input (":")


if oper == "+":
	ans = num1 + num2

if oper == "-":
	ans = num1 - num2

if oper == "*":
	ans = num1 * num2

if oper == "/":
	ans = num1 / num2

print ("The answer is : "), ans