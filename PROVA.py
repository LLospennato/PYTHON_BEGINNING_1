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

#EXCEPTION event detected during execution that interrupt the flow of a program ----- TRY and EXCEPT
# it is good to catch any exception separately
# try:
#     numerator= int(input("Enter a number to divide: "))
#     denominator= int(input("Enter a number to divide by: "))
#     results = numerator/denominator  # for example impossible to divide by 0
#     # print(results)
# except ZeroDivisionError as e:
#     print(e)
#     print("You cannot divide by zero idiot ")
# # except Exception:
# #     print("Something went wrong")
# except ValueError as e:
#     print(e)
#     print("Enter only number please")
# else: #it works only if we don't have any exeption
#     print(results)
# finally:  #generally use to close files opened before
#     print("This will always execute")



#FILES DETECTION
# import os   #--> IT NEEDS TO BE IMPORTED TO WORK WITH FILES
#
# path = "C:\\Users\\loren\\OneDrive\\Desktop\\PERSONALE\\PYTHON\\folder"
#
# if os.path.exists(path):
#     print("that location exists")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is a directory")
# else:
#     print("that location doesn't exist")

#READING A FILE IN PYTHON
# path = "C:\\Users\\loren\\OneDrive\\Desktop\\PERSONALE\\PYTHON\\test.txt"
# try:
#     with open(path) as file: #this will close the file automatically
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found")
#
# print(file.closed)

#WRITING FILE IN PYTHON -----w:write; a:append

# text = "\nidiots"
#
# with open('test1.txt', 'a') as file:
#     file.write(text)

#COPYING FILES IN PYTHON

#copyfile() = copies contents of a file
#copy() = copyfile() + permission mode + destination can be a directory'
#copy2() = copy() + copies metadata (file's creation and modification times)

# import shutil

# shutil.copyfile('test1.txt','C:\\Users\\loren\\OneDrive\\Desktop\\PERSONALE\\PYTHON\copy.txt')  #two arguments a source and a destination src.dst

#MOVING FILES OR DIRECTORIES we have a source and a destination location

# import os
#
# source = "foldertry"
# destination = "C:\\Users\\loren\\OneDrive\\Desktop\\PERSONALE\\PYTHON\\foldertry"
#
# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source,destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print(source+" was not found")

#DELETING FILES

# import os
# import shutil
#
# path='empty_folder'
#
# try:
#     # os.remove(path)
#     os.rmdir(path) #to delete an empty folder
#     shutil.rmtree(path) #delete a directory containing files
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("Ypu don't have permission to delete that")
# except OSError:
#     print("you cannot delete that using that function")
# else:
#     print(path+" was deleted")


#MODULE it is a file containing python code. it may contains functions, classes, etc...
#used with a modular programming, which is to separate a program into parts

# import messages as msg

# msg.hello()
# msg.bye()

# from messages import hello,bye
# hello()
# bye()

# from messages import *  #it means import all
# hello()
# bye()

# help("modules")


#CREATION OF A BASIC GAME (sasso, carta, forbice)
# import random
# while True:
#     choices = ["rock", "paper", "scissors"]
#     player = None
#     computer = random.choice(choices)
#     while player not in choices:
#         player = input("rock, paper or scissors?: ").lower()
#
#     if player==computer:
#         print("player: ",player)
#         print("computer: ",computer)
#         print("Tie!")
#     elif player=='rock':
#         if computer=="paper":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("You lose")
#         if computer=="scissors":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("You win")
#     elif player=='scissors':
#         if computer=="paper":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("You win")
#         if computer=="rock":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("You lose")
#     elif player=='paper':
#         if computer=="scissors":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("You lose")
#         if computer=="rock":
#             print("player: ", player)
#             print("computer: ", computer)
#             print("You win")
#     play_again=input("Play again? (yes/no): ").lower()
#
#     if play_again!="yes":
#         break
# print("BYE")

#GAME QUIZ GAME

#-------------
# def new_game():
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#     call = 0
#     for key in questions:
#         print("--------------------------------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         while call==0:
#             guess = input("Enter (A, B, C, D): ")
#             guess = guess.upper()
#             if guess == "A" or guess == "B" or guess == "C" or guess == "D":
#                 call = 1
#         call = 0
#
#         guesses.append(guess) #insert the guess in the before created list
#         correct_guesses += check_answer(questions.get(key),guess) #it takes the results from questions on the same position of key
#         question_num +=1
#
#     display_score(correct_guesses, guesses)
#
# #-----------------
# def check_answer(answer, guess):
#     if answer==guess:
#         print("Correct")
#         return 1
#     else:
#         print("Wrong")
#         return 0
#
# #-------------------
# def display_score(correct_guesses, guesses):
#     print("---------------------------")
#     print("RESULTS")
#     print("---------------------------")
#     print("Answers: ", end=" ")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print() #it is used to skip a line
#
#     print("Guesses: ", end=" ")
#     for i in guesses:
#         print(i, end=" ")
#     print()
#
#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is "+str(score)+"%")
# #------------------
# def play_again():
#
#     response = input("Do you want to play again? (yes or no): ")
#     response= response.upper()
#
#     if response == "YES":
#         return True
#     else:
#         return False
#
#
#
# #we use a dictionary in order to create a quiz game
# questions={
#     "Who created python?: ": "A",
#     "What year was Python created?: ": "B",
#     "Python is tributed to which comedy group?: " : "C",
#     "Is the Earth round? :" : "A"
# }
# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#            ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]
#
#
#
# new_game()
#
# while play_again():
#     new_game()
#
# print("Bye")

#PYTHON OBJECT ORIENTED PROGRAMMING
#It is better to create the class in another file and import it in the current script

# from car import Car #from the name of the file import the class
#
# car_1 = Car("Chevy", "Corvette", 2021, "Blue") # in this way we create an object from the defined class
# car_2 = Car("Ford", "Mustang", 2022, "Red")
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)
#
# car_1.drive()
# car_2.stop()

#CLASS VARIABLES

# from car import Car
# car_1 = Car("Chevy", "Corvette", 2021, "Blue")
# car_2 = Car("Ford", "Mustang", 2022, "Red")
# #
# # car_1.wheels=2 #to change it only for car_1
# #
# # print(car_1.wheels)
# Car.wheels=2 #it changes the value of the class--- it effects all the instances of the class
# print(Car.wheels) #number of wheels for that class
#
# print(car_1.wheels)
# print(car_2.wheels)

#INHERITANCE IN PYTHON --->inherit from other classes
#Thi is better when we have many different classes with the same features
#PARENT CLASS
# class Animal:
#     alive = True
#
#     def eat(self):
#         print("This animal is eating")
#
#     def sleep(self):
#         print("This animal is sleeping")
#
# #FAMILY TREE -- they can also have their own characteristics
# class Rabbit(Animal): #This is a "children" class--> we have to pass into the parentesis the name of the other class
#     def run(self):
#         print("This rabbit is running")
#
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")
#
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# print(rabbit.alive) #they have the class variable alive even if it is empty because they inherited what is in animal
# fish.eat()
# hawk.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()

#MULTI LEVEL INHERITANCE --> a derived (child) class inherit from another derived class

# class Organism:
#     alive = True
#
# class Animal(Organism):
#
#     def eat(self):
#         print("This animal is eating")
#
# class Dog(Animal):
#     def bark(self):
#         print("This dog is barking")
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()

#MULTIPLE INHERITANCE ---> a child class is derived from more that one parent class

# class Prey:
#
#     def flee(self):
#         print("This animal flees")
#
# class Predator:
#
#     def hunt(self):
#         print("This animal is hunting")
#
# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey, Predator):  #it has access to both the classes
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.hunt()
# fish.flee()

#METHOD OVER-WRITING

# class Animal:
#
#     def eat(self):
#         print("This animal is eating")
#
# class Rabbit(Animal):
#
#     def eat(self): # to overwrite we need to define the method with the same parameters
#         print("This rabbit is eating a carrot") #now we will use this version for the eat method
# rabbit = Rabbit()
# rabbit.eat()

#METHOD CHAINING ---->calling method sequentially
#each call performs an action on the same object and return self

# class Car: #we need to return something
#     def turn_on(self):
#         print("you start the engine")
#         return self
#     def drive(self):
#         print("You drive the car")
#         return self
#     def brake(self):
#         print("You step on the brakes")
#         return self
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
#
# car = Car()

# car.turn_on().drive()
# car.drive()
# car.brake().turn_off()
# car.turn_on().drive().brake().turn_off()


#SUPER FUNCTION --> super(); it is used to give access to the methods of a parent class. It returns a temporary object
#                            of a parent class when used

# class Rectangle:  # any similarities could be placed inside the parent class in order not to repeat the same lines of code
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Rectangle):
#
#     def __init__(self, length, width):
#         super().__init__(length,width)
#     def area(self):
#         return self.length*self.width
# class Cube(Rectangle):
#     def __init__(self, length, width, height):
#         super().__init__(length,width)
#         self.height = height
#     def volume(self):
#         return self.length*self.width*self.height
#
# square = Square(3,3)
# cube = Cube (3,3,3)
#
# print(square.area())
# print(cube.volume())


#ABSTRACT CLASSES
#It preventes a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# from abc import ABC,abstractmethod  #used to prevent to create a vehicle object
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
#
# #For the child classes we need to implement all the abstract methods from the parent class
# class Car(Vehicle):
#
#     def go(self):
#         print("You drive the car")
#     def stop(self):
#         print("This car is stopped")
# class Motorcycle(Vehicle):
#
#     def go(self):
#         print("You ride the motorcycle")
#     def stop(self):
#         print("This motorcycle is stopped")
# # vehicle = Vehicle()  #we cannot create this object
# car = Car()
# motorcycle = Motorcycle()
#
# # vehicle.go()
# car.go()
# motorcycle.go()
# car.stop()
# motorcycle.stop()



#PASS OBJECTS AS ARGUMENTS

# class Car:
#
#     color = None
#
# class Motorcycle:
#
#     color = None
#
# # If we want do define a separate function it needs to be outside the class
# def change_color(vehicle, color):  #we accept a car object and a color
#     vehicle.color = color
#
# # We define the objects linked to the class
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# bike_1 = Motorcycle()
#
#
# change_color(car_1, "red")
# change_color(car_2, "white")
# change_color(car_3, "blue")
# change_color(bike_1,"black")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)

#DUCK TYPING: concept where the class of an object is less important that the methods/attributes
#             class type is not checked if minimum methods/attributes are present
#             "If it walks like a duck, and it quacks like a duck, then it must be a duck."

# class Duck:
#
#     def walk(self):
#         print("This duck is walking")
#
#     def talk(self):
#         print("This duck is qwuacking")
#
# class Chicken:
#     def walk(self):
#         print("This chicken is walking")
#     def talk(self):
#         print("This chicken is clucking")
#
# class Person():
#
#     def catch(self,duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(chicken)



#WALRUS OPERATOR :=
# It assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

#USING A WALRUS OPERATOR (in less lines)
# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)



#ASSIGN A FUNCTION TO A VARIABLE
# def hello():
#     print("Hello")
#
# print(hello) # It prints the memory address of the function in the memory
# hi = hello
# # print(hi)
# hi() # As calling the hello function

# say = print
# say("Whooooooo") # It prints, since it does the same stuff of a print function

#HIGHER ORDER FUNCTION: a function that either:
#                       1) accepts a function as an argument
#                           or
#                       2) returns a function  (in python, functions are also treated as objects)

# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
# hello(loud) #I'm passing a function as argument
# hello(quiet)
#
#
# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend
#
# divide = divisor(2) # we are returning the dividend and assign it to a variable
# print(divide(10)) # we can call a variable if it has a memory adress of a function


#LAMBDA FUNCTION: function written in 1 line using lambda keyword
#                 accepts any number of arguments, but only has one expression.
#                 (think of it as a shortcut)
#                 (useful if needed for a short period of time, throw-away)
#lambda parameters:expression  SINTAX

# def double(x):
#     return x*2
#
# print(double(5))

# double = lambda x: x*2 #lambda parameters : expression
# print(double(5))

# multiply = lambda x,y : x * y
# print(multiply(6,5))

# add= lambda x,y,z : x+y+z
# print(add(1,2,3))

# full_name=lambda first_name, last_name: first_name+" "+last_name
# print(full_name("Lorenzo","Lospennato"))

# age_check = lambda age:True if age>=18 else False
# print(age_check(17))

#SORT ITERABLES
#sort() method = used with lists
#sort() function = used with iterables
#level 1
# students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")
#
# # students.sort(reverse=True) #Reverse it only works with lists
# sorted_students = sorted(students, reverse=True)
#
#
# for i in sorted_students:
#     print(i)

#level 2 how to sort in function of name, grade or age ----list of tuples
# students =[("Squidward","F", 60),("Sandy","A",33),("Patrick","D",36),("Spongebob","B",20),("Mr.Krabs","C",78)]
# students =(("Squidward","F", 60),("Sandy","A",33),("Patrick","D",36),("Spongebob","B",20),("Mr.Krabs","C",78))
# #sorting by name
# # students.sort()
# #
# # grade = lambda grades:grades[1] #we take the second column (grades)
# # students.sort(key=grade, reverse=True) #grade is a function object via a lambda function ----key return the index of the column we need
#
# age = lambda ages:ages[2] #we take the second column (grades)
# # students.sort(key=age, reverse=True)
# sorted_students = sorted(students, key=age) #in the case of a tuple of tuples we cannot use sort directly but a function
# for i in sorted_students:
#     print(i)


#MAP FUNCTION map()
# It applies a function to each item in an iterable (list, tuple, etc.)
# map(function, iterable)

# store = [("shirt", 20.00),("pants", 25.00),("jacket",50.00),("socks",10.00)]
#
# #convert prices from dollar to euros
# # to_euros = lambda data : (data[0],data[1]*0.82) #parentesis in order to create a tuple and then we take what we want
# to_dollars = lambda data : (data[0],data[1]/0.82)
#
# # store_euros = list(map(to_euros, store))
# store_dollars = list(map(to_dollars, store))
# for i in store_dollars:
#     print(i)



#FILTER FUNCTION filter()
# It creates a collection of elements from an iterable for which a function return True
#filter(function,iterable)

friends = [("Rachel",19),("Monica",18),("Phoebe",17),("Joey",16),("Chandler",21),("Ross",20)]

