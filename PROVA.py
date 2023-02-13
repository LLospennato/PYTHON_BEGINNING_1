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
# It creates a collection of elements from an iterable for which a function return True----->it takes all the elements that
# respect the function's condition--- research all the results that meet the condition
#filter(function,iterable)

# friends = [("Rachel",19),("Monica",18),("Phoebe",17),("Joey",16),("Chandler",21),("Ross",20)]
#
# #create another list with friends bigger than 18
# age = lambda data:data[1]>= 18 #function to get all the friends bigger than 18
#
# drinking_buddies = list(filter(age, friends)) #filter function and iterable and cast it back to a list
#
# for i in drinking_buddies:
#     print(i)

#REDUCE FUNCTION
#reduce() apply a function to an iterable and reduce it to a single cumulative value. It performs function on first two
# elements and repeats process until 1 value remains
#reduce(function, iterable)

# import functools
# # letters = ["H","E", "L", "L", "O"] #reduce it to a single cumulative value
# #
# # word = functools.reduce(lambda x,y: x+y,letters) #HE, HEL, HELL, HELLO untile only one value remains
# # print(word)
#
# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x,y: x*y,factorial) #5*4--- 5*4*3----- etc.
# print(result)



#LIST COMPREHENSION = a way to create a new list with less syntax, can mimic certain lambda functions, easier to read
#                   list = [expression for item in iterable]
#                   list = [expression for item in iterable if conditions]
#                   list = [expression if/else for item in iterable] with if else the for is after

# squares = [] #create an empty list
# for i in range(1,11):
#     squares.append (i*i)
# print(squares)

#using a list comprehension
# squares = [i * i for i in range(1,11)]
# print(squares)


# students = [100,90,80,70,60,50,40,30,0]
#
# # passed_students = list(filter(lambda x:x>=60, students))
#
# #using list comprehension
# passed_students = [i if i>=60 else "FAILED" for i in students]
#
# print(passed_students)


#DICTIONARY COMPREHENSION = create dictionaries using an expression; can replace for loops and certain lambda functions

#dictionary = {key : expression for (key,value) in iterable}

# cities_in_F = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
#
# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)

#-----------------------------------------------------------------------------------
#dictionary = {key : expression for (key,value) in iterable if conditional}

# weather = {'New York':"Snowing", 'Boston':"sunny", 'Los Angeles':"sunny", 'Chicago':"cloudy"}
#
# sunny_weather = {key : value for (key,value) in weather.items() if value=="sunny"}
#
# print(sunny_weather)

# -------------------------------------------------------------------------------------
# dictionary = {key : (if/else) for (key,value) in iterable}

# cities = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
# decs_cities = {key : ("WARM" if value >=40 else "COLD") for (key,value) in cities.items()}
# print(decs_cities)

#------------------------------------------------------------------------------------------
#dictionary = {key : function(value) for (key,value) in iterable}

# def check_temp(value):
#     if value >=70:
#         return "HOT"
#     elif 69>= value >=40:
#         return "WARM"
#     else:
#         return "COLD"
#
# cities = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago':50}
# decs_cities = {key : check_temp(value) for (key,value) in cities.items()} #we have called a function defined above
# print(decs_cities)


#ZIP FUNCTION
#zip(*iterable) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                 creates a zip object with paired elements stored in tuples for each element

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")

# users =list(zip(usernames,passwords))
#
# print(type(users))
#
# for i in users:
#     print(i)

#we can use more than 2 iterables
# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")
# login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]
#
# users = zip(usernames,passwords,login_date)
#
# for i in users:
#     print(i)


#if __name__ == '__main__'
#1. Module can be run as a standalone program
#2. Module can be imported and used by other modules


# def hello():
#     print("HELLO")
#
#
# if __name__ == '__main__':
#     hello()


#TIME AND DATES

# import time
#
# # print(time.ctime(0))  # it converts a time expressed in seconds since epoch to a readable string
# #                       epoch = when your computer thinks time began (reference point)
#
# # print(time.time()) #return current seconds since epoch
#
# # print(time.ctime(time.time())) #convert that amounts of second into readable day and time
#
# # time_object = time.localtime()
# # time_object = time.gmtime()
# # # print(time_object)
# # #to convert it into something readable
# # local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) #format depends on different directives
# # print(local_time) #it prints the current time
#
# # time_string = "20 April, 2020"
# # time_object = time.strptime(time_string, "%d %B, %Y")
# # print(time_object) #we have a time object with all these keywords filled in with the data given
#
# #(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# # time_string = time.asctime(time_tuple) #ASCTIME it converts tuples representation in time and day in readable string
# time_string = time.mktime(time_tuple) #MKTIME converts in seconds since epoch
# print(time_string)



#THREAD = a flow execution. Like a separate order of instructions. However each thread takes a turn running to achieve concurrency.
#   GIL (global interpreter lock), allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program or task that spends most of its time waiting for internal events-- use multiprocessing
# io bound = program or task that spends most of its time waiting for external events (user input..)
#
# import threading
# import time
#
# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")
# def drink_coffe():
#     time.sleep(4)
#     print("You drink coffe")
# def study():
#     time.sleep(5)
#     print("You finish studying")
#
# x = threading.Thread(target=eat_breakfast, args=())
# x.start()
#
# y = threading.Thread(target=drink_coffe, args=())
# y.start()
#
# z = threading.Thread(target=study, args=())
# z.start()

#the main thread has to wait for the syncronization of x,y,z and then move on
# x.join()
# y.join()
# z.join()


#we are running these tasks sequentially and not concurrently (in this way)
# eat_breakfast()
# drink_coffe()
# study()


# print(threading.active_count())
# print(threading.enumerate())  # print the list of the threads
# print(time.perf_counter())


#DAEMON THREAD = a thread that runs in the background, not important for program to run
#               your program will not wait for daemon threads to complete before exiting
#               non-daemon threads cannot normally be killed, stay alive until task is complete


# import threading
# import time
#
# def timer():
#     print()
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for: ", +count, " seconds")
#
# x = threading.Thread(target=timer,daemon=True)
# x.start
#
# x.setDaemon(True)
# print(x.isDaemon())
#
# answer = input("Do you wish to exit?")



#MULTIPROCESSING = running tasks in parallel on different cpu cores; better for cpu bound tasks

# from multiprocessing import Process, cpu_count
# import time
#
#
# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
#
# def main():
#     print(cpu_count()) #maximum of processes that I can run simultaneously
#
#     a = Process(target=counter, args=(250000000,))
#     b = Process(target=counter, args=(250000000,))
#     c = Process(target=counter, args=(250000000,))
#     d = Process(target=counter, args=(250000000,))
#
#     a.start()
#     b.start()
#     c.start()
#     d.start()
#
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     print("finished in: ", time.perf_counter(), "seconds")
#
# if __name__ == '__main__':
#     main()


#GRAPHICAL INTERFACE

from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

# window = Tk() #instantiate an instanvr of a window
# window.geometry("420x420") #change the dimension of the window
# window.title("First GUI program")

# icon = PhotoImage(file='Jpg_fototessera.jpg') #create a photo image that will be used as a 'logo' of the window
# window.iconphoto(True, icon) #to change the 'logo'
# window.config(background="#5cfcff") #change color of background (could take the value from google)
#
#
# window.mainloop() #to desplay a window, lister to events

#CREATE LABELS = area widgets that holds text and/or an image within a window

# window = Tk()
#
# photo = PhotoImage(file = 'C:\\sers\\loren\\OneDrive\\Desktop\\POLIMI\\MODELLISTICA DELLE MACCHINE E DEGLI IMPIANTI ELETTRICI\\RELAZIONE & IMMAGINI\\Logo_Politecnico_Milano.png')
#
# label = Label(window,text="Hello World",font=('Arial',40,'bold'),fg='#00FF00', bg='black',relief=RAISED,bd=10,padx=20,pady=20,compound='bottom')
# #parentesis are the constructor of the label; inside the parentesis the container is passed --foreground and background of the text ---
# # --> bord to the text ---> compound where to set the picture
# label.pack() #how to add the label to the window ---> pack function
# # label.place(x=0, y=0) #in the top left corner
# # label.place(x=100, y=100)
#
# window.mainloop()


#CREATE BUTTONS

# count = 0
# def click():
#     global count
#     count += 1
#     print(count)
#
#
# window = Tk()
#
# photo = PhotoImage(file='img.png')
#
# button = Button(window,
#                 text="Click me!",
#                 command=click,
#                 font=("Comic Sans", 30),
#                 fg="#00FF00",
#                 bg="black",
#                 activeforeground="#00FF00",
#                 activebackground="black",
#                 state=ACTIVE,
#                 image=photo,
#                 compound='bottom')
# button.pack()
#
#
# window.mainloop()


# ENTRY WIDGET
# from tkinter import *
#
# def submit():
#     username = entry.get() #it takes what we write in the entry
#     print("Hello " +username)
#     entry.config(state=DISABLED)
#
# def delete():
#     entry.delete(0,END)
#
# def backspace():
#     entry.delete(len(entry.get())-1, END)
#
# window = Tk()
#
#
# entry = Entry(window,
#               font=("Arial",50),
#               fg="#00FF00",
#               bg="black",
#               show="*") #always state where we are placing the entry ---> in the window
# entry.insert(0,'Spongebob ')
# entry.pack(side=LEFT)
#
# submit_button = Button(window,text="submit", command=submit)
# submit_button.pack(side=RIGHT)
# delete_button = Button(window,text="delete", command=delete)
# delete_button.pack(side=RIGHT)
# backspace_button = Button(window,text="backspace", command=backspace)
# backspace_button.pack(side=RIGHT)
# window.mainloop()



#CUSTOMIZE CHECK BUTTON

# from tkinter import *
#
# def display():
#     if(x.get() == 1):
#         print("You agree")
#     else:
#         print("you don't agree")
#
# window = Tk()
#
# x = IntVar()
#
# photo = PhotoImage(file='img.png')
# check_button = Checkbutton(window,
#                            text="I agree to something",
#                            variable=x,
#                            onvalue=1,  #if boolean True and change IntVar in BooleanVar and if statement
#                            offvalue=0,
#                            command=display,
#                            font=('Arial', 20),
#                            fg='#00FF00',
#                            bg='black',
#                            activeforeground='#00FF00',
#                            activebackground='black',
#                            padx=25,
#                            pady=10,
#                            image=photo,
#                            compound='left')
# check_button.pack()
#
# window.mainloop()


#CREATRE RADIOBUTTON = you can only select one from a group

# from tkinter import *
#
# food = ["pizza", "hamburger", "hotdog"]
#
# def order():
#     if (x.get()==0):
#         print("you ordered pizza")
#     elif (x.get()==1):
#         print("you ordered hamburger")
#     elif (x.get() == 2):
#         print("you ordered hotdog")
#     else:
#         print("huh?")
#
# window = Tk()
#
# pizzaImage = PhotoImage(file='img_1.png')
# burgerImage = PhotoImage(file='img_2.png')
# hotdogImage = PhotoImage(file='img_3.png')
# foodImages = [pizzaImage,burgerImage,hotdogImage]
# x=IntVar()
#
# for index in range(len(food)):
#     radiobutton = Radiobutton(window, text=food[index], #add text to radio buttons
#                               variable=x, #groups radiobuttons together if they share the same variables
#                               value=index, #assigns each radiobutton a different value
#                               padx=25, #adds padding on x axis
#                               font=("Impact", 50),
#                               # image=foodImages[index], #adds images to radiobuttons
#                               compound='left',
#                               indicatoron=0, #eliminate circle indicators
#                               command=order, #set command of radiobutton to function
#                               )
#     radiobutton.pack(anchor=W)
#
# window.mainloop()


#CREATE A SLIDING SCALE IN PYTHON

# from tkinter import *
#
# def submit():
#     print("The temperature is " +str(scale.get())+" degrees C")
#
# window = Tk()
#
# hotimage = PhotoImage(file='img_4.png')
# hotLabel = Label(image=hotimage)
# hotLabel.pack()
#
# scale = Scale(window,
#               from_=0,
#               to=100,
#               length=600,
#               orient=VERTICAL, #orientation of the scale
#              font=("Consolas",20),
#               tickinterval=10,#it sets numeric intervals to the scale
#               # showvalue = 0 , #it hides the current value
#               resolution= 5, #increment of slider
#               troughcolor='#69EAFF', #it changes the color of the bar
#               fg='#FF1C00',
#               bg='black')
# scale.set(((scale['from']-scale['to'])/2)+scale['to']) #it brings the value to half of the scale
#
# scale.pack()
#
# coldimage = PhotoImage(file='img_5.png')
# coldLabel = Label(image=coldimage)
# coldLabel.pack()
#
# button = Button(window, text='submit', command=submit)
# button.pack()
# window.mainloop()


#CREATE A LISTBOX = a listing of selectable text items within it's own container (for example an online menu)

# def submit():
#
#     food = []
#
#     for index in listbox.curselection():
#         food.insert(index,listbox.get(index))
#
#     print("you have ordered: ")
#     for index in food:
#         print(index)
#     #print(listbox.get(listbox.curselection()))
#
# def add():
#     listbox.insert(listbox.size(),entryBox.get())
#     listbox.config(height=listbox.size())  #it adjusts the size of the list
#
# def delete():
#     # listbox.delete(listbox.curselection())
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)
#
#     listbox.config(height=listbox.size())
# from tkinter import *
#
# window = Tk()
#
# listbox = Listbox(window,
#                   bg="#f7ffde",
#                   font=("Constantia",35),
#                   width=12,
#                   selectmode=MULTIPLE, #need to be added if we want to select multiple items
#                   )
# listbox.pack()
#
#
# listbox.insert(1,"pizza")
# listbox.insert(2,"pasta")
# listbox.insert(3,"garlic bread")
# listbox.insert(4,"soup")
# listbox.insert(5,"salad")
#
# listbox.config(height=listbox.size())
#
# entryBox = Entry(window)
# entryBox.pack()
#
#
# submitButton = Button(window,text="submit", command=submit)
# submitButton.pack()
#
# addButton = Button(window,text="add", command=add)
# addButton.pack()
#
# deleteButton = Button(window,text="delete", command=delete)
# deleteButton.pack()
#
# window.mainloop()


#HOW TO CREATE MESSAGE BOXES IN PYTHON

from tkinter import *
from tkinter import messagebox #import messagebox library
# def click():
    # messagebox.showinfo(title='This is an info message box',message='You are a person')
    # while(True):
    #     messagebox.showwarning(title='Warning', message='You have a virus')
    # messagebox.showerror(title='Error', message='Something went wrong')
    # if messagebox.askokcancel(title='Ask ok cancel', message='Do you want to do the thing?'):
    #     print("You did the thing")
    # else:
    #     print("You canceled the thing")
    # messagebox.askretrycancel(title='ask retry cancel', message='Do you want to retry the thing?')
    # if messagebox.askyesno(title='ask yes or no', message='Do you like cakes?'): #it returns booleans
    #     print("I like cake too")
    # else:
    #     print("Why do you don't like cakes?")
    # answer = messagebox.askquestion(title='ask question', message='Do you like pie?')
    # if(answer == "yes"):
    #     print("I like pie too")
    # else:
    #     print("You don't like pie")
#     answer = messagebox.askyesnocancel(title='yes, no or cancel', message='Do you like to code?',icon='error') #icon:warning, info, error
#     if (answer==True):
#         print("You like to code")
#     elif (answer==False):
#         print("Why don't you like coding?")
#     else:
#         print("You have dodged the question")
#
# window = Tk()
#
# button = Button(window, command=click, text="click me")
# button.pack()
#
# window.mainloop()




#COLOR CHOOSER MODULE

# from tkinter import *
# from tkinter import colorchooser #submodule
#
# def click():
#     color = colorchooser.askcolor() #you can select the color you want
#     # print(color)
#     colorHex = color[1]
#     # print(colorHex)
#     window.config(bg=colorHex) #it will change the background color
#
#
# window = Tk()
#
# window.geometry("420x420")
#
# button = Button(text="click me", command=click)
# button.pack()
#
# window.mainloop()



#CREATE TEXT AREA
#text widget = functions like a text area, you can enter a multiple lines of text

# from tkinter import *
# def submit():
#     input = text.get("1.0",END) #1.0 is the first line
#     print(input)
#
# window = Tk()
#
# text = Text(window,
#             bg="light yellow",
#             font=("Ink Free",25),
#             height=8, #amount of characters that this is tall
#             width=20, #amount of characters that this is long
#             padx=20,
#             pady=20,
#             fg="purple")
# text.pack()
#
# button = Button(window,text="submit", command=submit)
# button.pack()
# window.mainloop()



#FILE DIALOG ---> open and read the content


# from tkinter import *
# from tkinter import filedialog
#
# def openFile():
#    filepath =  filedialog.askopenfilename() #it returns the file path
#    file = open(filepath,'r')
#    print(file.read())
#    file.close()
#
#
#
# window = Tk()
#
# button = Button(text="Open", command=openFile)
# button.pack()
#
# window.mainloop()



#SAVE FILE IN THE COMPUTER


# from tkinter import *
# from tkinter import filedialog
#
# def saveFile():
#     file = filedialog.asksaveasfile(#initialdir="", if we want to open with the path directly from here
#                                     defaultextension='.txt',
#                                     filetypes=[     #it adds the type of file for which you can save the file
#                                         ("Text file", ".txt"),
#                                         ("HTML file", ".html"),
#                                         ("All file", ".*"),
#                                     ])
#
#     if file is None: #to add so as if we don't click where to save the file it works (we must have to select something)
#         return
#     # filetext = str(text.get("1.0",END))
#     filetext = input("Enters some test") #if we want to add the text from the command window
#     file.write(filetext)
#     file.close()
#
# window = Tk()
#
# button = Button(text='save', command=saveFile)
# button.pack()
#
# text = Text(window)
# text.pack()
#
# window.mainloop()


#CREATE A MENU BAR

# from tkinter import*
#
# def openFile():
#     print("File has been opened")
# def saveFile():
#     print("File has been saved")
# def cut():
#     print("you cut some text")
# def copy():
#     print("you copied some text")
# def paste():
#     print("you pasted some text")
# window = Tk()
#
# saveImage = PhotoImage(file="img_6.png")
#
# menubar = Menu(window)
# window.config(menu=menubar)
#
# fileMenu = Menu(menubar, tearoff=0,font=("MV Boli",15)) #tearoff = 0 it gets rid of the line on the drop down menu
# menubar.add_cascade(label="File",menu=fileMenu) #this will give us a drop down menu
# fileMenu.add_command(label="Open",command=openFile)
# fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
# fileMenu.add_separator() #it adds a separator
# fileMenu.add_command(label="Exit",command=quit) #pressing exit it closes the window (quit)
#
# editMenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Edit",menu=editMenu)
# editMenu.add_command(label="Cut",command=cut)
# editMenu.add_command(label="Copy",command=copy)
# editMenu.add_command(label="Paste",command=paste)
#
# window.mainloop()


#FRAMES = a rectangular container to group and hold widgets

# from tkinter import *
#
# window = Tk()
#
# frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
# # frame.pack(side=BOTTOM)
# frame.place(x=100, y=100)
#
#
# Button(frame, text="W", font=("Consolas",25),width=3).pack(side=TOP)  #since we added the buttons to the frame and not to the window
# #                                                                       they are all contained in one frame
# Button(frame, text="A", font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame, text="S", font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame, text="D", font=("Consolas",25),width=3).pack(side=LEFT)
#
#
# window.mainloop()


#CREATE NEW WINDOWS

# from tkinter import *
#
# def create_window():
#     # new_window = Toplevel()  #Toplevel() = new window 'on top' of other windows. Linked to a 'bottom' window (if bottom closed alsi the top one)
#     new_window = Tk()   #new independent window
#     old_window.destroy()    #this will close out old window when we press create new window
#
# old_window = Tk()
#
# Button(old_window,text="Create new window", command=create_window).pack()
#
# old_window.mainloop()



#CREATE SEPARATE TABS

# from tkinter import *
# from tkinter import ttk #it gives us access to many widgets
#
# window = Tk()
#
# notebook = ttk.Notebook(window)  #widget that manages a collection of windows/displays
#
# tab1 = Frame(notebook) #new frame for tab1
# tab2 = Frame(notebook)
#
# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2,text="Tab 2")
# notebook.pack(expand=True, fill="both") #it expands to fill any space not otherwise used; fill = fille space on x and y axis
#
# Label(tab1,text="Hello , this is tab 1",width=50, height=25).pack()
# Label(tab2,text="Hello , this is tab 2",width=50, height=25).pack()
#
# window.mainloop()


#GRID GEOMETRY MANAGER
#grid() = it organizes widgets in a table/like structure in a parent

# from tkinter import *
#
# window = Tk()
#
# titleLabel = Label(window,text="Enter your info", font=("Arial",25)).grid(row=0,column=0,columnspan=2)
#
# firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0) #we use grid rather than pack otherwise it would have placed the two one above the other
# firstNameEntry = Entry(window).grid(row=1,column=1)
#
# lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
# lasttNameEntry = Entry(window).grid(row=2,column=1)
#
# emailLabel = Label(window,text="Email: ",bg="blue",width=30).grid(row=3,column=0)
# emailEntry = Entry(window).grid(row=3,column=1)
#
# submitButton = Button(window,text="Submit").grid(row=4, column=0,columnspan=2) #columnspan=2 it will be between the two columns that we have
#
# window.mainloop()



#CREATE A PROGRESS BAR

# from tkinter import*
# from tkinter.ttk import*
# import time
#
# def start():
#     tasks = 10
#     x = 0
#     while (x<tasks):
#         time.sleep(1)
#         bar['value']+=10
#         x += 1
#         percent.set(str(int((x/tasks)*100))+"%")
#         text.set(str(x)+"/"+str(tasks)+" tasks completed")
#         window.update_idletasks() #after each iteration we have to update the window
#
# window = Tk()
#
# percent = StringVar()
# text = StringVar()
#
# bar = Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)
#
# percentLabel = Label(window,textvariable=percent).pack()
# taskLabel = Label(window,textvariable=text).pack()
#
# button = Button(window, text="download", command=start).pack()
#
# window.mainloop()



#CANVAS WIDGETS TO DRAW SHAPES

# from tkinter import *
#
# window = Tk()
#
# canvas = Canvas(window,height=500,width=500)
# canvas.create_line(0,0, 500,500, fill="blue",width=5) #(x,y) start , (x,y) end
# canvas.create_line(0,500, 500,0, fill="red",width=5)
# canvas.create_rectangle(50,50,250,250, fill="purple")
#we can also provides to the polygon a list of points
# points = [250,0,500,500,0,500]
# canvas.create_polygon(points, fill="yellow",outline="black",width=5)
# canvas.create_arc(0,0,500,500,fill="green",style=PIESLICE,start=270,extent=180)
# canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
# canvas.create_oval(190,190,310,310,fill="white",width=10)
# canvas.pack()
#
# window.mainloop()



#CREATE KEY EVENTS

# from tkinter import *
#
# def doSomething(event):
    # print("You pressed: " +event.keysym)
#     label.config(text=event.keysym)
# window = Tk()
#
# window.bind("<Key>", doSomething) #event (when in the keybord you press that stuff you perform the function), function
#
# label = Label(window,font=("Helvetica",100))
# label.pack()
#
# window.mainloop()



#MOUSE EVENTS

# from tkinter import *
#
# def doSomething(event):
#     print("Mouse coordinates: " + str(event.x) +","+str(event.y))
#
# window = Tk()

# window.bind("<Button-1>",doSomething)  #event, function   button-1 left side -2 scroll wheel -3 right
# window.bind("<ButtonRelease>",doSomething)
# window.bind("<Enter>",doSomething) #when I enter the window
# window.bind("<Leave>",doSomething)
# window.bind("<Motion>",doSomething) #where the mouse moved
# window.mainloop()



#HOW TO DRAG AND DROPS WIDGETS

# from tkinter import *
#
# def drag_start(event):
#     widget = event.widget #it is used in order to deal with more labels
#     #we are saving the coordinates of where we click within the label
#     widget.startX = event.x
#     widget.startY = event.y
#
# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x  #label.winfo_x -> it will get the top left x coordinate of our label of the window
#     #                                              where we are in; label.startX ->place where we clicked the label; event.x where we begin dragging
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y) #it replaces the label
#
#
# window = Tk()
#
# label = Label(window,bg="red", width=10, height=5)
# label.place(x=0,y=0)
#
# label2 = Label(window,bg="blue", width=10, height=5)
# label2.place(x=100,y=100)
#
# label.bind("<Button-1>", drag_start)
# label.bind("<B1-Motion>", drag_motion)
#
# label2.bind("<Button-1>", drag_start)
# label2.bind("<B1-Motion>", drag_motion)
#
# window.mainloop()



#HOW TO MOVE IMAGES

from tkinter import *

# --------------------------------------------------------------
#1 move a image within a window
# def move_up(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()-10)
# def move_down(event):
#     label.place(x=label.winfo_x(),y=label.winfo_y()+10)
# def move_left(event):
#     label.place(x=label.winfo_x()-10,y=label.winfo_y())
# def move_right(event):
#     label.place(x=label.winfo_x()+10,y=label.winfo_y())


# window = Tk()
# window.geometry("500x500")
#
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)
#
#
# myimage = PhotoImage(file='img_8.png')
# label = Label(window,image=myimage,)
# label.place(x=0,y=0)
#
#
#
# window.mainloop()


# ---------------------------------------------------
#2 move images on a canvas

# from tkinter import *
#
# def move_up(event):
#      canvas.move(myimage,0,-10) #name of the canvas + move function (image we want to use, amount of pixels we want to move X, Y)
# def move_down(event):
#      canvas.move(myimage,0,10)
# def move_left(event):
#      canvas.move(myimage,-10,0)
# def move_right(event):
#     canvas.move(myimage,10,0)
#
#
# window = Tk()
#
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)
#
# canvas = Canvas(window,width=500,height=500)
# canvas.pack()
#
# photoimage = PhotoImage(file='img_8.png')
# myimage = canvas.create_image(0,0,image=photoimage,anchor=NW) #anchor to fix the fact the image is not all visible
#
# window.mainloop()




#HOW CREATE 2D ANIMATIONS -->animate an image an a canvas

# from tkinter import *
# import time
# #constants
# WIDTH = 500
# HEIGHT= 500
# xVELOCITY = 3
# yVELOCITY = 2
#
# window = Tk()
#
# canvas = Canvas(window, width=WIDTH, height=HEIGHT)
# canvas.pack()
#
# #if we want the background we have to add it before everything
# background_photo = PhotoImage(file='img_7.png')
# background = canvas.create_image(0,0, image=background_photo,anchor=NW)
#
# photo_image = PhotoImage(file='img_8.png')
# my_image = canvas.create_image(0,0, image=photo_image,anchor=NW)
#
# image_width = photo_image.width()
# image_height = photo_image.height()
#
# while True:
#     coordinates = canvas.coords(my_image)
#     print(coordinates)
#     if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#         xVELOCITY = -xVELOCITY
#     if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
#         yVELOCITY = -yVELOCITY
#     canvas.move(my_image, xVELOCITY,yVELOCITY) #but it will disappear
#     window.update()
#     time.sleep(0.01) #il sleeps for 0.01s
#
#
#
# window.mainloop()



#HOW TO ANIMATE MULTIPLE OBJECTS

# from tkinter import *
# from Ball import *
# import time
#
# window = Tk()
#
# WIDTH = 500
# HEIGHT = 500
#
# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()
#
# volley_ball = Ball(canvas,0,0,100,1,1,"white")
# tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
# basket_ball = Ball(canvas,0,0,125,8,7,"orange")
# while True:
#     volley_ball.move()
#     tennis_ball.move()
#     basket_ball.move()
#     window.update()
#     time.sleep(0.01)
#
# window.mainloop()



#HOW TO CREATE A CLOCK PROGRAM IN PYTHON

# from tkinter import *
# from time import *
#
# def update():
#     time_string = strftime("%I:%M:%S %p")  #to return the current time
#     time_label.config(text=time_string)
#
#     day_string = strftime("%A")  # to return the current time
#     day_label.config(text=day_string)
#
#     date_string = strftime("%B %d, %Y")  # to return the current time
#     date_label.config(text=date_string)
#
#     window.after(1000,update) #to update the function (milliseconds, recursive function)
#
# window = Tk()
#
# time_label =Label(window,font=("Arial",50),fg="#00FF00",bg="black")
# time_label.pack()
# day_label =Label(window,font=("Ink free",25))
# day_label.pack()
# date_label =Label(window,font=("Ink free",30))
# date_label.pack()
# update()
#
# window.mainloop()


#RUN PY FILE USING THE COMMAND PROMPT

print("Hello world")

name = input("What's your name?: ")

print("Hello "+name)
