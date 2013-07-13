print ("--------------------------------------")
print (" ")

print ("Advanced Quick Calculator")
print ("By Max M, licenced under GPLv3")

print (" ")
print ("--------------------------------------")

statement = raw_input ("Please enter your mathematical statement [3 3 plus minus times divide]: ")

strnum1 = statement[:1]
print ("strnum1 : " + strnum1)
#num1 = int (strnum1)

strnum2 = statement[:4]
print ("strnum2 : " + strnum2)
#num2 = int (strnum2)

operation = statement[5:11]
print ("operation : " + operation)
#if operation == "+":
#	ans = num1 + num2

#if operation == "-":
#	ans = num1 - num2

#if operation == "*":
#	ans = num1 * num2

#if operation == "/":
#	ans = num1 / num2

#print ("The answer is : "), ans