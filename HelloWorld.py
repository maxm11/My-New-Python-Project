print ("--------------------------------------")
print (" ")

print ("Hello!")
print ("Welcome to Max's Tinkering Enviroment for Python!")
print ("This was coded in Cloud9 Ide, a new cloud IDE.")

print (" ")
print ("--------------------------------------")
print (" ")

print ("Just to get familiar with my good looking users...")

print (" ")
print ("--------------------------------------")
print (" ")

##Name Input
rawname = raw_input("What is your name? : ")
name = str(rawname)
print (" ")

##Using Name String
print (name + ", you have the best name I have ever heard!")

print (" ")
print ("--------------------------------------")
print (" ")

##Gender Input
print ("Are you a gentleman, or a fine lady?")
gender = raw_input("Enter 1 if you are a gentleman or Enter 2 if you are a lady [1-2]: ")

print (" ")

if gender == "1":
	print ("Ok, " + name + " if you're looks were rated 1-10, would be a eww 1, or a devistatingly hansome 10?")
elif gender == "2":
	print ("Ok, " + name + " if you're looks were rated 1-10, would be a eww 1, or a gorgeously beautiful 10?")
else:
	print ("Ok, " + name + " unfortunatly, you are a genderless potato, would you rate your self, 1 - 10")

print (" ")

##Rated Number System
number = raw_input("Enter Number [1-10]: ")

print (" ")
print ("--------------------------------------")
print (" ")

##Flaterring Response
if gender == "1":
	
	if number == "10":
		print ("I agree!!")
	else:
		print ("Why a " + number + ", I think you're a 10!")

elif gender == "2":

	if number == "10":
		print ("I agree!!")
	else:
		print ("Why a " + number + ", I think you're a 10!")

else:
	if number == "1":
		print ("I agree, you are an ugly genderless potato.")
	else:
		print ("Not, " + number + ", you are a 1, you ugly potato.")
		
print (" ")
print ("--------------------------------------")
print (" ")

##Room to Add MOAR!!
## Ending
print ("That's all I do.")

print (" ")
print ("--------------------------------------")
print (" ")

##Farewells
if gender == "1":
	print("Good Bye, my good man.")
elif gender == "2":
	print ("Toodles, my fine lady")
else:
	print("Goodbye, genderless potato...")

print (" ")
print ("--------------------------------------")