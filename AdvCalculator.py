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
prenum1 = raw_input (":")
oper = raw_input (":")
prenum2 = raw_input (":")

num1 = int(prenum1)
num2 = int(prenum2)

if oper == "+":
	ans = num1 + num2

elif oper == "-":
	ans = num1 - num2

elif oper == "*":
	ans = num1 * num2

elif oper == "/":
	ans = num1 / num2
    
elif oper == ">":
    if num1 >= num2:
        ans = "Yes, " + prenum1 + " is > " + prenum2
    else:
        ans = "No, " + prenum1 + " is NOT > " + prenum2
        
elif oper == "<":
    if num1 <= num2:
        ans = "Yes, " + prenum1 + " is < " + prenum2
    else:
        ans = "No, " + prenum1 + " is NOT < " + prenum2

else:
    ans = "INVALID OPERATOR"
    
print ("-------------------------------------")
print (":"), ans
