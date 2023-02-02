# VARIABLES
import math

#first_name = 'Lorenzo'
#last_name = 'Lospennato'
#full_name = first_name +" " + last_name
#print ("Hello " +full_name)
#print (type(full_name))

#age = 22
#age += 1
#print ("your age is " +str(age))
#print(type(age))


#height = 250.5
#print("your height is " +str(height) +" cm")
#print(type(height))

#human = True  #with "" it is a string
#print("Are you a human? " +str(human) )
#print(type(human))


#MULTIPLE ASSIGNMENT

#name = "Lorenzo"
#age = 22
#attractive = True

#name, age, attractive = "Lorenzo", 22, True

#print(name)
#print(age)
#print(attractive)

# STRING METHODS

#name = "lorenzo"
#name_1="112231"

#print(len(name))
#print(name.find("e"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name_1.isdigit())
#print(name.isalpha()) #if the string contains only alphabetical letters
#print(name.count("o"))
#print(name.replace("o", "a"))
#print(name*3)

#TYPE CASTING
#x=1 #int
#y=2.0 #float
#z="3" #str

#x=str(x)


#print("X is " +x) #without a string it is not possible
#print("Y is "+str(y))
#print(z*3)

#ACCEPT USER INPUT
##name = input("what is your name?: ")
#age = int(input("how old are you?: "))
#height = float(input("how tall are you?: "))
#age=age+1
#print("Hello " +name + " your age is " +str(age) +" you are " +str(height) + " cm")

#FUNCTIONS FOR NUMBERS

pi= 3.14
x=2
y=3.2
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(max(pi,x,y))


#STRING SLICING  [start:stop:step]

#name = "Lorenzo Giacomo"

#first_name= name[:7:1]
#last_name = name [8:15]
#reversed_name= name[::-1]
#print(reversed_name)


#website_1 = "http://google.com"
#website_2= "http://wikipedia.com"

#slice = slice(7,-4,1)
#print(website_1[slice])
#print(website_2[slice])

#IF STATEMENT

age=int(input("how old are you?: "))

if age >= 18:
    print("You are an adult")
elif age<0:
    print("you haven't been born yet")
else:
    print("you are a child")



