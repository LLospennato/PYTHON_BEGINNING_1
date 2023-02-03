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

# pi= 3.14
# x=2
# y=3.2
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

#age=int(input("how old are you?: "))

#if age == 100:
 #   print("you are a century old")
#elif age >= 18:
 #   print("You are an adult")
#elif age<0:
 #   print("you haven't been born yet")
#else:
 #   print("you are a child")

#LOGICAL OPERATOR

# temp = int(input("What is the temperature outside?: "))
#
# if temp>=0 and temp <=30:
#     print("the temperature in good today!")
# elif temp<0:
#     print("you will freeze!")
# elif not(temp >=0 and temp <=30 or temp<0 ):
#     print ("it's really hot today")

# LOOPS
# WHILE LOOP

# name = ""
#
# while len(name)==0:
#     name=input("enter your name: ")
#
# print("hello " +name)

# FOR LOOP
# import time
# for i in range(10):
#     print(i+1)

# for i in range(50,100+1,2):
#     print(i)

# for i in "Lorenzo":
#     print(i)

# for seconds in range(10,0,-1):
#     print (seconds)
#     time.sleep(1)
# print("happy new year")

# NEESTED LOOPS one loop inside another one

# rows=int(input("how many rows?: "))
# columns=int(input("how many columns?: "))
# symbol=input("enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# LOOP CONTROL STATEMENTS
# BREAK: used to terminate the loop entirely
# CONTINUE: skips to the next iteration of the loop
# PASS: does nothing, acts as a placeholder

# while True:
#     name = input("enter your name: ")
#     if name != "":
#         break

# phone_number="123-456-7890"

# for i in phone_number:
#     if i== "-":
#         continue
#     print(i, end="")

# for i in range (1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)


# LISTS used to store multiple variables

# food = ["pizza", "hamburgers", "hotdog", "spaghetti"]
#
# food[0]="sushi"

# print(food[0])

# FUNCTIONS FOR LISTS
# food.append("ice cream")
# food.remove("hotdog")
# food.pop()
# food.insert(0,"cake")
# food.sort()
# food.clear()


# for x in food:
#     print(x)

# 2D lists
#
# drinks = ["coffe", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
#
# food = [drinks, dinner, dessert]
#
# print(food[0][2]) 2 sets of square brackets to have access on the value on the original list

# TUPLE collection which is ordered and unchangeable; used to group together related date

# student = ("Lorenzo", 22, "male")
#
# print(student.count("Lorenzo"))
# print(student.index("male"))
# # print all the elements
# for i in student:
#     print(i)
#
# if "Lorenzo" in student:
#     print("Lorenzo is here")

# SET collection which is unordered, unindexed. No duplicate values

# utensils = {"fork", "spoon", "knife", "knife", "knife"}  #only one
# dishes = {"bowl", "plate", "cup",  "knife"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes) #add elements of dishes to utensils
# dinner_table = utensils.union(dishes) #create a new set with the union of the two
# print(utensils.difference(dishes)) #check what the first set has different from the second one
# print(dishes.difference(utensils))
# print(utensils.intersection(dishes)) #what they have in common

# for x in dinner_table:
#     print(x)


# DICTIONARY is a changeable, unordered collection of unique key:value pairs. It's fast because they use hashing, allow to
#access a value quickly

# capitals = {'USA':'Washington DC', 'India':'New Dehli', 'China':'Beijing', 'Russia':'Moscow'}

# print(capitals['Russia'])
# print(capitals.get('Germany')) # if there is not the key
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items()) #print both keys and values
# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'}) #it changes the value of USA
# capitals.pop('China') #remove
# capitals.clear()
# for key,value in capitals.items():
#     print(key, value)



#INDEX OPERATOR [] It gives access to a sequence's element (sts, lists, tuples)

# name = "lorenzo Lospennato!"
#
# # if (name[0].islower()):
# #     name = name.capitalize()
# first_name = name[0:7].upper()
# last_name = name[8:].lower()
# last_character = name[-1]
# print(first_name)
# print(last_name)
# print(last_character)


# FUNCTIONS

# def hello(first_name, last_name, age): # def + name + parentesis at the end ----- if there is inside a parameter call it in the definition
#     print("hello " +first_name+" "+last_name+" you are "+str(age)+ " years old")
#     print("have a nice day")
#
# hello("Lorenzo", "Lospennato", 21) # recall it with the name and the parentesis

#RETURN STATEMENT ---functions send python values/objects back to the caller; these values/objects are known as the function's
#                    return value

# def multiply(number1, number2):
#     # results=number1*number2
#     # return results
#     return number1*number2
# x=multiply(6,8)
# print(x)

#KEYWORD ARGUMENT arguments preceded by ad identifier when we pass them to a function; the order of the arguments doesen't matter,
#                 unlike positional arguments python knows the names of the arguments that our function receives

# def hello(first,middle,last): #order of the arguments matter
#     print("hello "+first+" "+middle+" "+last)
#
# hello(last="Lorenzo", middle="Giorgio", first="Lospennato") #we can use keyword arguments

#NESTED FUNCTIONS CALLS

# num=float(num)
# num=abs(num)
# num=round(num)
# print(num)
# print(round(abs(float(input("Enter a whole positive number: "))))) #it does the same thing

#SCOPE the region that a variable is recognized
#
# name = "Lorenzo"  # global scope--- it is possible to have a global and local variable with the same name
# def display_name():
#     name = "Lorenzo" # Local scope, only available inside the function, if you call it outside the function it doesn't work
#     print(name)
#
# display_name()
# print(name)

#*ARGS parameter that will pack all arguments into a tuple

# def add(*stuff):
#     sum = 0
#     # stuff[0]=0 #not possible it does not support item assignment
#     stuff = list(stuff) #a list can be changeable
#     stuff[0]=0 # now it is possible to change
#     for i in stuff:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5,6))

#**kwargs parameter that will pack all arguments into a dictionary
#         useful so that a function can accept a varying amount of keyword arguments

# def hello(**names):
#     # print("Hello "+ kwargs['first'] +" " + kwargs['last']+)
#     print("hello", end=" ")
#     for key,value in names.items():
#         print(value, end=" ")
#
#
# hello(title="Mister", first="Lorenzo", middle="Giacomo", last="Lospennato")

#FORMAT METHOD IN PYTHON it is optional and it gives users more control when displaying output

# animal = "cow"
# item = "moon"
# #
# # # print("The " +animal +" jumper over the " +item )
# # #better do to so
# # print("The {1} jumped over the {0}".format("moon","cow"))
# # print("The {animal} jumped over the {item}".format(item="moon",animal="cow"))
#
# text = "The {} jumper over the {}"
# print(text.format(animal,item))

# name = "Lorenzo"
# # print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}, nice to meet you".format(name)) #add some space after that parameter
# print("Hello, my name is {:<10}, nice to meet you".format(name)) #space after the parameter
# print("Hello, my name is {:>10}, nice to meet you".format(name))  #space before the parameter
# print("Hello, my name is {:^10}, nice to meet you".format(name)) #it centers the space (half left and half right)

# number = 3.14159
# print("The number pi is {:.2f}".format(number)) #only the first do digit the dot

# number = 1000
# print("The number pi is {:,}".format(number)) #add a coma to all 1000 places
# print("The number pi is {:b}".format(number)) #write it in binary
# print("The number pi is {:o}".format(number)) #octal number
# print("The number pi is {:X}".format(number)) #hexabecimal
# print("The number pi is {:,}".format(number))
# print("The number pi is {:E}".format(number)) #scientific notation

#RANDOM generate random

# import random
#
# x = random.randint(1,6)
# y = random.random() # it generates a random between 0 and 1
# mylist=['rock', 'paper', 'scissors']
# z = random.choice(mylist)
#
# cards=[1,2,3,4,5,6,7,8,9,"J", "Q", "K", "A"]
# #shuffle the desk
# random.shuffle(cards)
# print(cards)

#EXCEPTION event detected during execution that interrupt the flow of a program

try:
    numerator= int(input("Enter a number to divide: "))
    denominator= int(input("Enter a number to divide by: "))
    results = numerator/denominator  # for example impossible to divide by 0
    print(results)
except Exception:
    print("Something went wrong")




