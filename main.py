# # Slice
# website1 = "https://google.com"

# slice = slice(8, -4)

# print(website1[slice])



# # Logical Operators
# temp = int(input("What is the temperature outside?: "))

# # put not in front of temp, and surrond the line with ()
# if temp >= 0 and temp <= 30:
#     print("the temperatuire is good today")
# elif temp < 0 or temp > 30:
#     print("The temperature is bad today")



# # While Loops
# name = ""

# while len(name) == 0:
#     name = input("Enter Your Name: ")

# print("Hello " +name)



# # For Loops
# for i in range(50, 100+1,2):
#     print(i)

# for i in "Cats Cool":
#     print(i)

# import time

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")



# # Nested Loops
# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()



# # Loop Control Statements
# # Break ends a loop
# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# # continue skips to the next iteration of the loop
# phone_number = "123-456-7890"

# for i in phone_number:
#     if i =="-":
#         continue
#     # adding ,end="" makes it so it goes on one line
#     print(i, end="")

# # pass does nothing, it acts as a passholder
# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)



# # Lists
# # it starts with 0 not 1
# food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

# food[0] = "sushi"

# # print(food[0])

# food.append("ice cream")
# food.remove("hogdog")
# # removes the last item
# food.pop()
# food.insert(0, "cake")
# # sorts the list alphabetical
# food.sort()
# food.clear()

# for x in food:
#     print(x)



# # 2D Lists
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]

# food = [drinks, dinner, dessert]

# print(food[0][0])



# # Tuple
# student = ("Cat",21,"male")

# print(student.count("Cat"))
# print(student.index("male"))

# for x in student:
#     print(x)

# if "Cat" in student:
#     print("Cat is here")



# # Set
# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}

# # utensils.add("napkin")
# # utensils.remove("fork")
# # utensils.clear()
# # utensils.update(dishes)
# # dinner_table = utensils.union(dishes)

# # for x in dinner_table:
# #     print(x)

# # print(utensils.difference(dishes))
# # print(utensils.intersection(dishes))



# # Dictionaries
# capitals = {'USA':'Washington DC',
#             'India':'New Dehli',
#             'China':'Beijing',
#             'Russia':'Moscow'}

# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# # print(capitals['Russia'])
# # print(capitals['Germany'])
# # # a safe was to check if something is in your Dictionaries
# # print(capitals.get('Germany'))
# # print(capitals.keys())
# # print(capitals.values())
# # print(capitals.items())

# for key,value in capitals.items():
#     print(key, value)



# # Index Operator
# name = "cat Cool!"

# # if(name[0].islower()):
# #     name = name.capitalize()

# first_name = name[:3].upper()
# last_name = name[4:].lower()
# last_character = name[-1]

# print(first_name)
# print(last_name)
# print(last_character)



# # functions
# def hello(first_name,last_name, year):
#     print("Hello World!")
#     print("The date is "+str(year))
#     print("My name is "+first_name+" "+last_name)

# hello("Cat","Cool",2023)



# # Return Statement
# def multiply(number1,number2):
#     return number1 * number2

# x = multiply(6,8)

# print(x)



# # Keyword Arguments
# def hello(first,middle,last):
#     print("Hello "+first+" "+middle+" "+last)

# hello(last="Cool",middle="Epic",first="Cat")



# # Nested Function Calls
# # num = input("Enter a whole positive number: ")
# # num = float(num)
# # num = abs(num)
# # num = round(num)
# # print(num)

# print((round(abs(float(input("Enter a whole positive number: "))))))



# # Variable Scope
# # load order: Local, Enclosing, Global, Built-in
# name = "Cat"

# def display_name():
#     name = "Cool"
#     print(name)

# display_name()
# print(name)



# # Args
# # The most important thing is the *
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(1,2,3))



# # Kwargs
# # The most important thing is the **
# def hello(**kwargs):
#     # print("Hello "+kwargs['first']+" "+kwargs['last'])
#     print("Hello ",end="")
#     for key,value in kwargs.items():
#         print(value,end="")

# hello(title="Mr.", first="Cat ",middle="Epic ",last="Cool")



# # String Format
# animal = "cow"
# item = "moon"

# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(item, animal))
# print("The {animal} jumped over the {item}".format(item="moon", animal="cow"))

# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# name = "cat"
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))

# number = 1000
# print("The number pi is {:.2f}".format(number))
# print("The number pi is {:,}".format(number))
# print("The number pi is {:b}".format(number))
# print("The number pi is {:o}".format(number))
# print("The number pi is {:x}".format(number))
# print("The number pi is {:e}".format(number))



# # Random Numbers
# import random

# x = random.randint(1,6)
# y = random.random()

# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)

# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

# random.shuffle(cards)

# print(cards)



# # Exception Handing?
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers please")
# except Exception as e:
#     print(e)
#     print("something went wrong :(")
# else:
#     print(result)
# finally:
#     print("This will always exacute")



# # File Detection
# import os

# path = "C:\\Users\\Sebastian Gillis\\Desktop\\CodeBro.txt"

# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
# else:
#     print("That location doesn't exist!")



# # Read A File In Python
# # with open('test.txt') as file:
# #     print(file.read())

# # print(file.closed)

# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found")



# # Writing A File
# text="Yooooooo\nThis is some text\nHave a good one"

# with open('text1.txt','w') as file:
#     file.write(text)



# # Copy A File
# import shutil

# shutil.copyfile('text1.txt','copy.txt') 



# # Move A File
# import os

# source = "copy.txt"
# destination = "C:\\Users\\Sebastian Gillis\\Desktop\\copy.txt"

# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source,destination)
#         print(source+ "was moved")
# except FileNotFoundError:
#     print(source+" was not found")



# # Delete A File
# import os

# path = 'test.txt'

# try:
#     os.remove(path)
# except FileExistsError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that")
# else:
#     print(path+" was deleted")



# # Modules
# # from messages import hello,bye
# # from messages import *
# import messages as msg

# msg.hello()
# msg.bye()

# # help("modules")



# # Object Oriented Programming OOP And Class Variables
# from car import Car

# car_1 = Car("Chevy","Corvette",2021,"blue")
# car_2 = Car("Ford","Mustang",2022,"red")

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

# Car.wheels = 2

# car_1.drive()
# car_2.stop()
# print(car_1.wheels)



# # Inheritance
# class animal:
#     alive = True

#     def eat(self):
#         print("This animal is eating")

#     def sleep(self):
#         print("This animal is sleeping")

# class Rabbit(animal):
#     def run(self):
#         print("This rabbit is running")
# class Fish(animal):
#     def swim(self):
#         print("This fish is swimming")
# class Hawk(animal):
#     def fly(self):
#         print("This hawk is flying")

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# # print(rabbit.alive)
# # fish.eat()
# # hawk.sleep()

# rabbit.run()
# fish.swim()
# hawk.fly()



# # Multilevel Inheritance
# class Organism:

#     alive = True

# class Animal(Organism):

#     def eat(self):
#         print("This animal is eating")

# class Cat(Animal):

#     def meow(self):
#         print("This cat is meowing")

# cat = Cat()
# print(cat.alive)
# cat.eat()
# cat.meow()



# # Multiple Inheritance
# class Prey:

#     def flee(self):
#         print("This animal flees")

# class Predator:

#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()



# # Method Overriding
# class Animal:

#     def eat(self):
#         print("This animal is eating")

# class Rabbit(Animal):
    
#     def eat(self):
#         print("This rabbit is eating a carrot")

# rabbit = Rabbit()
# rabbit.eat()



# #  Method Chaining
# class Car:

#     def turn_on(self):
#         print("You start the engine")
#         # return self is what allows you to method call
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

# car = Car()

# # You can have it go onto the next line with a \
# car.turn_on()\
# .drive().brake().turn_off()



# # Super Function
# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

# class Square(Rectangle):

#     def __init__(self, length, width):
#         # The super part is from the parent class Rectangle
#         super().__init__(length, width)

#     def area(self):
#         return self.length*self.width

# class Cube(Rectangle):

#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height
    
#     def volume(self):
#         return self.length*self.width*self.height

# square = Square(3, 3)
# cube = Cube(3, 3, 3)

# print(square.area())
# print(cube.volume())



# # Abstract Classes
# from abc import ABC, abstractclassmethod

# class Vehicle(ABC):

#     @abstractclassmethod
#     def go(self):
#         pass

#     @abstractclassmethod
#     def stop(self):
#         pass

# class Car(Vehicle):

#     def go(self):
#         print("You drive the car")
    
#     def stop(self):
#         print("This car is stopped")

# class Motorcycle(Vehicle):

#     def go(self):
#         print("You ride the motorcycle")

#     def stop(self):
#         print("This motorcycle is stopped")

# # vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()

# # vehicle.go()
# car.go()
# motorcycle.go()
# car.stop()
# motorcycle.stop()



# # Object As Arguments
# class Car:

#     color = None

# class Motorcycle:

#     color = None

# def change_color(car, color):

#     car.color = color

# car_1 = Car()
# car_2 = Car()
# car_3 = Car()

# bike1 = Motorcycle()

# change_color(car_1,"red")
# change_color(car_2,"white")
# change_color(car_3,"blue")

# change_color(bike1,"black")

# print(car_1.color)
# print(car_2.color)
# print(car_3.color)

# print(bike1.color)



# # Duck Typing
# class Duck:
#     def walk(self):
#         print("This duck is walking")
    
#     def talk(self):
#         print("This duck is qwuacking")

# class Chicken:

#     def walk(self):
#         print("This chicken is walking")
    
#     def talk(self):
#         print("This chicken is clucking")

# class Person():

#     def catch(self, duck):

#         duck.walk()
#         duck.talk()
#         print("You cought the critter")

# duck = Duck()
# chicken = Chicken()
# person = Person()

# person.catch(chicken)



# # Walrus Operator
# # happy = True
# # print(happy)

# # print(happy := True)

# # foods = list()
# # while True:
# #     food = input("what food do you like?: ")
# #     if food == "quit":
# #         break
# #     foods.append(food)

# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)



# # Functions To Variables
# def hello():
#     print("Hello")

# # This shows where this function is stored in my computer's memory
# # Its displayed in hexadecimal
# print(hello)

# say = print
# say("This works!")



# # Higher Order Functions
# # def loud(text):
# #     return text.upper()

# # def quiet(text):
# #     return text.lower()

# # def hello(func):
# #     text = func("Hello")
# #     print(text)

# # hello(loud)
# # hello(quiet)

# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend

# divide = divisor(2)
# print(divide(10))



# #  Lambda Functions
# # def double(x):
# #     return x * 2

# # print(double(5))

# double = lambda x:x * 2
# multiply = lambda x, y: x * y
# add = lambda x, y, z: x + y + z
# full_name = lambda first_name, last_name: first_name + last_name
# age_check = lambda age:True if age >= 18 else False

# print(double(5))
# print(multiply(5,6))
# print(add(5,6,7))
# print(full_name("Cat", "Cool"))
# print(age_check(18))



# # # Sort
# # students = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")

# # # sort sorts only lists, alphabetically eg tuples don't work
# # # students.sort(reverse=True)

# # # If you make it a function you can add tiples
# # sorted_students = sorted(students, reverse=True)

# # for i in students:
# #     print(i)


# students = [
#     ("Squidward", "F", 50),
#     ("Sandy", "A", 33),
#     ("Patrick", "D", 36),
#     ("Spongebob", "B", 20),
#     ("Mr.Krabs", "C", 78)
# ]

# grade = lambda grades: grades[1]
# students.sort(key=grade, reverse=True)

# for i in students:
#     print(i)



# # Map Function
# # A map is made up of a function, and a iterable, The function in the example below is to_euro, and the iterable is the tuple
# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)
# ]

# # This is USD to Euro its 1 USD to every 0.95 Euro
# to_euro = lambda data: (data[0], data[1] * 0.95)
# to_dollars = lambda data: (data[0], data[1] / 0.95)

# store_euros = list(map(to_euro, store))

# for i in store_euros:
#     print(i)



# # Filter Function
# friends = [
#     ("Rachel",19),
#     ("Monica",18),
#     ("Phoebe",17),
#     ("Joey",16),
#     ("Chandler",21),
#     ("Ross",20),
# ]

# age = lambda data: data[1] >= 18

# drinking_buddies = list(filter(age, friends))

# for i in drinking_buddies:
#     print(i)



# # Reduce Function
# import functools

# # letters = ["H","E","L","L","O"]
# # word = functools.reduce(lambda x, y: x + y,letters)
# # print(word)

# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x, y: x * y, factorial)
# print(result)



# # List Comprehension
# # This creates a list of the numbers 1 through 10 with the numbers squared
# squares = []                #create an empty list
# # for i in range(1,11):       #create a for loop
# #     squares.append(i * i)   #define what each loop iteration should do
# # print(squares)

# # list = [expression for item in iterable]
# squares = [i * i for i in range(1,11)]
# print(squares)


# students = [100,90,80,70,60,50,40,30,0]

# # passed_students = list(filter(lambda x: x >= 60, students))

# # passed_students = [i for i in students if i >= 60]

# passed_students = [i if i >= 60 else "Failed" for i in students]

# print(passed_students)



# # Dictionary Comprehension
# cities_in_F = {
#     'New York': 32,
#     'Boston':75,
#     'Los Angeles':100,
#     'Chicago':50
# }

# # desc_citties = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities_in_F.items()}
# # print(desc_citties)

# def check_temp(value):
#     if value >= 70:
#         return "Hot"
#     elif 69>= value >= 40:
#         return "Warm"
#     else:
#         return "Cold"

# desc_citties = {key: check_temp(value) for (key,value) in cities_in_F.items()}
# print(desc_citties)

# cites_in_C = {key: round((value-32) * (5 / 9)) for (key,value) in cities_in_F.items()}
# print(cites_in_C)

# weather = {
#     'New York':"snowing",
#     'Boston':"sunny",
#     'Los Angeles':"sunny",
#     'Chicago':"cloudy"
# }
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)



# # Zip Function
# usernames = ["Cat", "Epic", "Cool"]
# passwords = ("password", "abc123", "guest")
# login_date = ["1/1/2023", "1/2/2023", "1/3/2023"]

# # users = zip(usernames, passwords)
# # users = list(zip(usernames, passwords))
# # users = dict(zip(usernames, passwords))
# users = zip(usernames, passwords, login_date)

# # for i in users:
# #     print(i)

# # for key,value in users.items():
# #     print(key +" : " + value)

# for i in users:
#     print(i)



# # # if __name__=='__main__'
# # if __name__=='__main__':
# #     print("running this module directly")
# # else:
# #     print("running other module indirectly")

# def hello():
#     print("Hello!")



# # Time Module
# import time

# # print(time.ctime(0)) # Its expressed in seconds, also its starting from epoch or when your computer thinks time began

# # # print(time.time())
# # print(time.ctime(time.time()))

# # # time_object = time.gmtime() # Universal Time
# # time_object = time.localtime()                                  # This are the iterables tm_year=2023, tm_mon=3, tm_mday=1, tm_hour=11, tm_min=10, tm_sec=42, tm_wday=2, tm_yday=60, tm_isdst=0
# # print(time_object)                                              # The iterables mean year, month, day, hour, minute, seconds, day of the week, day of the year, daylight savings hour
# # local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)    # strftime, requires a format, and time object, Python time docs here https://docs.python.org/3/library/time.html
# # print(local_time)

# # time_string = "20 April, 2023"
# # time_object = time.strptime(time_string,"%d %B, %Y")
# # print(time_object)

# time_tuple = (2023, 4, 20, 4, 20, 0, 0, 0, 0)
# # time_string = time.asctime(time_tuple)
# time_string = time.mktime(time_tuple)       # mktime displays it in seconds from the epoch of your computer
# print(time_string)



# # Threading
# import threading
# import time

# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")

# def drink_coffee():
#     time.sleep(4)
#     print("You drink coffee")

# def study():
#     time.sleep(5)
#     print("You finish studying")

# x = threading.Thread(target=eat_breakfast, args=())
# x.start()

# y = threading.Thread(target=drink_coffee, args=())
# y.start()

# z = threading.Thread(target=study, args=())
# z.start()

# x.join()    # These are joined into the main Thread
# y.join()
# z.join()

# # eat_breakfast()
# # drink_coffee()
# # study()

# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())      # This shows how long it takes the main thread to finish creating 3 different threads



# # Daemon Threads
# import threading
# import time

# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("Loggedin for: ",count, "seconds")

# x = threading.Thread(target=timer, daemon=True)
# x.start()

# # If a thread is already running you can't change it mid way through
# # x.setDaemon(True)
# print(x.isDaemon())

# answer = input("Do you wish to exit?")



# # Multiprocessing
# from multiprocessing import Process, cpu_count
# import time

# def counter(num):
#     count = 0
#     while count < num:
#         count += 1

# def main():

#     print(cpu_count)
    
#     a = Process(target=counter, args=(250000000,))
#     b = Process(target=counter, args=(250000000,))
#     c = Process(target=counter, args=(250000000,))
#     d = Process(target=counter, args=(250000000,))

#     a.start()
#     b.start()
#     c.start()
#     d.start()

#     a.join()
#     b.join()
#     c.join()
#     d.join()

#     print("Finished in:",time.perf_counter(),"seconds")

# if __name__ == '__main__':
#     main()



# # GUI Windows
# from tkinter import *

# # widgets = GUI elements: buttons, textboxes, labels, images
# # windows = serves as a container to hold or contain these widgets

# window = Tk()                           # instantiate an instance of a window, not yet displaying it
# window.geometry("420x420")              # This decides the size of the window
# window.title("First GUI Program")       # This sets the title of the window

# icon = PhotoImage(file='logo.png')
# window.iconphoto(True, icon)

# window.config(background="#5cfcff")     # This changes the windows background color

# window.mainloop()                       # This is displaying the window, and place it on our screen, while listening for events



# # Labels
# from tkinter import *

# # label = an area widget that holds text and/or an image within a window

# window = Tk()
# window.geometry("420x420") 
# window.title("Labels") 

# photo = PhotoImage(file='logo.png')

# label = Label(window,
#               text="Hello World",
#               font=('Arial',40,'bold'),
#               fg='#00FF00',
#               bg='black',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#               image=photo,
#               compound='bottom')

# label.pack()  # places it at the top middle
# # label.place(x=100,y=100) # places it at cords of your choice

# window.mainloop()



# # Buttons
# from tkinter import *

# count = 0

# def click():
#     global count
#     count += 1
#     print(count)

# window = Tk()
# window.geometry("420x420") 
# window.title("Button") 

# photo = PhotoImage(file="logo.png")

# button = Button(window,
#                 text="Click Me!",
#                 command=click,
#                 font=("Comic Sans",30),
#                 fg="#00FF00",
#                 bg="black",
#                 activeforeground="#00FF00",
#                 activebackground="black",
#                 state=ACTIVE,             # State is how the button works, the button is active by default
#                 image=photo,
#                 compound="bottom")
# button.pack()

# window.mainloop()



# # Entrybox
# from tkinter import *

# def submit():
#     username = entry.get()
#     print("Hello "+username)
#     entry.config(state=DISABLED)

# def delete():
#     entry.delete(0, END)

# def backspace():
#     entry.delete(len(entry.get())-1, END)

# window = Tk()
# # window.geometry("420x420") 
# window.title("Entrybox") 

# entry = Entry(window,
#               font=("Arial",50),
#               fg="#00FF00",
#               bg="black",
#               show="*")

# # entry.insert(0,'Type Your Username')
# entry.pack(side=LEFT)

# submit_button = Button(window,text="Submit",command=submit)
# submit_button.pack(side=RIGHT)

# delete_button = Button(window,text="Delete",command=delete)
# delete_button.pack(side=RIGHT)

# backspace_button = Button(window,text="Backspace",command=backspace)
# backspace_button.pack(side=RIGHT)

# window.mainloop()



# # Checkbox
# from tkinter import *

# def display():
#     if(x.get() == 1):
#         print("you agree")
#     else:
#         print("You don't agree")

# window = Tk()
# # window.geometry("420x420") 
# window.title("CheckBox") 

# x = IntVar()

# photo = PhotoImage(file='logo.png')

# check_button = Checkbutton(window,
#                            text="I agree to something",
#                            variable=x,
#                            onvalue=1,
#                            offvalue=0,
#                            command=display,
#                            font=('Arial',20),
#                            fg='#00FF00',
#                            bg='black',
#                            activeforeground='#00FF00',
#                            activebackground='black',
#                            padx=25,
#                            pady=10,
#                            image=photo,
#                            compound="left")

# check_button.pack()

# window.mainloop()



# # Radio Button
# from tkinter import *

# food = ["pizza","hamburger","hotdog"]

# def order():
#     if(x.get()==0):     # x is the veriable stored in the radiobuttons
#         print("You ordered pizza!")  
#     elif(x.get()==1):
#         print("You ordered a hamburger!")   
#     elif(x.get()==2):
#         print("You ordered a hotdog!")
#     else:
#         print("huh")

# window = Tk()
# # window.geometry("420x420") 
# window.title("Radio Buttons") 

# pizzaImage = PhotoImage(file="images\\pizza.png")
# burgerImage = PhotoImage(file="images\\burger.png")
# hotdogImage = PhotoImage(file="images\\hotdog.png")

# foodImages = [pizzaImage,burgerImage,hotdogImage]

# x = IntVar()

# for index in range(len(food)):
#     radiobutton = Radiobutton(window,
#                               text=food[index],     # adds text to radio buttons
#                               variable=x,           # groups radiobuttons together if they share the same variable
#                               value=index,          # this assigns each radiobutton a different value
#                               padx=25,
#                               font=("Impact",50),
#                               image=foodImages[index],
#                               compound='left',      # adds image and text 
#                               indicatoron=0,        # removes the radiobuttons, and replaces them with push buttons
#                               width=375,
#                               command=order)        
#     radiobutton.pack(anchor=W)    #You can also add W without the ''

# window.mainloop()



# # Scale
# from tkinter import *

# def submit():
#     print("The temperature is: "+str(scale.get())+" degrees °C")

# window = Tk()
# # window.geometry("420x420") 
# window.title("Scale") 

# hotImage = PhotoImage(file='images\\burger.png')
# hotLabel = Label(image=hotImage)
# hotLabel.pack()

# scale = Scale(window,
#               from_=100,
#               to=0,
#               length=600,
#               orient=VERTICAL,      # orientation of scale
#               font=('Consolas',20),
#               tickinterval=10,      #adds numbers beside the scale
#               showvalue=0,          # hide current value
#               resolution= 5,        # increases the rate in which the scale goes up
#               troughcolor='#69EAFF',# This sets the color of the sliding bar
#               fg='#FF1C00',
#               bg='#111111')
# scale.set(((scale['from']-scale['to'])/2)+scale['to'])    # scale.set(num) sets the starting point, this math makes the starting point always in the middle
# scale.pack()

# coldImage = PhotoImage(file='images\\hotdog.png')
# coldLabel = Label(image=coldImage)
# coldLabel.pack()

# button = Button(window,
#                 text='submit',
#                 command=submit)
# button.pack()

# window.mainloop()



# # Listbox
# from tkinter import *

# food = ["pizza","pasta","garlic bread","soup","salad"]

# def submit():
#     # print("You have ordered: ")
#     # print(listbox.get(listbox.curselection()))    # This works for submitting one item at a time

#     food_submit = []

#     for index in listbox.curselection():
#         food_submit.insert(index,listbox.get(index))
    
#     print("You have ordered: ")
#     for index in food_submit:
#         print(index)

# def add():
#     listbox.insert(listbox.size(),entryBox.get())
#     listbox.config(height=listbox.size())           # This changes the listbox size to fit the new item

# def delete():
#     # listbox.delete(listbox.curselection())        # This works for deleting one item at a time
#     # listbox.config(height=listbox.size()) 

#     for index in reversed(listbox.curselection()):  # This has to be reversed as the index changes when you delete something
#         listbox.delete(index)
#     listbox.config(height=listbox.size()) 

# window = Tk()
# # window.geometry("420x420") 
# window.title("Listbox") 

# listbox = Listbox(window,
#                   bg="#f7ffde",
#                   font=("Constantia",35),
#                   width=12,
#                   selectbackground='#f54251',     # I changed the text highlight color
#                   selectmode=MULTIPLE)
# listbox.pack()

# for i in range(len(food)):      # I added a list, and loop instead of typing it out 5 times over like he did
#     listbox.insert(i,food[i])

# listbox.config(height=listbox.size())

# entryBox = Entry(window)
# entryBox.pack()

# submitButton = Button(window,
#                       text="submit",
#                       command=submit)
# submitButton.pack()

# addButton = Button(window,
#                       text="add",
#                       command=add)
# addButton.pack()

# deleteButton = Button(window,
#                       text="delete",
#                       command=delete)
# deleteButton.pack()

# window.mainloop()



# # Messagebox
# from tkinter import *
# from tkinter import messagebox # submodule

# def click():
#     # messagebox.showinfo(title='This is an info message box',message='You are a person')

#     # while(True):
#         # messagebox.showwarning(title='Warning',message='You have a VIRUS!!!')             # This is how to make an uncloseable popup
#     # messagebox.showerror(title='ERROR!',message='Something went wrong :(')

    
#     # if messagebox.askokcancel(title='ask of cancel',message='Do you want to do the thing'):
#     #     print('You did a thing')
#     # else:
#     #     print('You canceled a thing! :(')

#     # if messagebox.askretrycancel(title='ask of cancel',message='Do you want retry the thing'):
#     #     print('You retried a thing')
#     # else:
#     #     print('You canceled a thing! :(')

#     # if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
#     #     print('I like cake too')
#     # else:
#     #     print('Why do you not like cake')

#     # answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
#     # if(answer == 'yes'):
#     #     print('I like pie too')
#     # else:
#     #     print('Why do you not like pie too')

#     answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?',icon='error') # icon lets you set the icon
#     if(answer==True):
#         print("You like to code")
#     elif(answer==False):
#         print("Then why are you coding")
#     else:
#         print("You have dodged the question")

# window = Tk()
# # window.geometry("420x420") 
# window.title("Messagebox") 

# button = Button(window,
#                 command=click,
#                 text='click me')
# button.pack()

# window.mainloop()



# # Colorchooser
# from tkinter import *
# from tkinter import colorchooser # submodule

# def click():
#     # color = colorchooser.askcolor()
#     # print(color)
#     # colorHex = color[1]
#     # window.config(bg=colorHex)
#     # print(colorHex)

#     window.config(bg=colorchooser.askcolor()[1])

# window = Tk()
# window.geometry("420x420") 
# window.title("colorchooser") 

# button = Button(text='click me',command=click)
# button.pack()

# window.mainloop()



# # Text Area, Text Widget
# from tkinter import *

# def submit():
#     input = text.get("1.0",END)
#     print(input)

# window = Tk()
# # window.geometry("420x420") 
# window.title("Text Area") 

# text = Text(window,
#             bg='light yellow',
#             font=("Ink Free",25),
#             height=8,
#             width=20,
#             padx=20,
#             pady=20,
#             fg='purple')
# text.pack()

# button = Button(window,
#                 text='submit',
#                 command=submit)
# button.pack()

# window.mainloop()



# # Open A File
# from tkinter import *
# from tkinter import filedialog

# def openFile():
#     filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Sebastian Gillis\\Documents\\Coding\\GitHub Repo\\Python Bro Code",
#                                           title="Open File okay?",
#                                           filetypes=(("text files","*.txt"),
#                                           ("all files","*.*")))
#     file = open(filepath,'r')
#     print(file.read())
#     file.close()

# window = Tk()
# # window.geometry("420x420") 
# window.title("Open A File") 

# button = Button(text="Open",
#                 command=openFile)
# button.pack()

# window.mainloop()



# # Save A File
# from tkinter import *
# from tkinter import filedialog

# def saveFile():
#     file = filedialog.asksaveasfile(initialdir="C:\\Users\\Sebastian Gillis\\Documents\\Coding\\GitHub Repo\\Python Bro Code",
#                                     defaultextension='.txt',
#                                     filetypes=[
#                                         ("Text File",".txt"),
#                                         ("HTML File",".html"),
#                                         ("All Files",".*")
#                                     ])
#     if file is None:
#         return
#     filetext = str(text.get(1.0,END))
#     # filetext = input("Enter some text I guess")
#     file.write(filetext)
#     file.close()

# window = Tk()
# # window.geometry("420x420") 
# window.title("Open A File") 

# button = Button(text='save',
#                 command=saveFile)
# button.pack()

# text = Text(window)
# text.pack()

# window.mainloop()



# # Menu Bar
# from tkinter import *

# def openFile():
#     print("FIle has been opened")

# def saveFile():
#     print("FIle has been saved")

# def cut():
#     print("You cut some text!")

# def copy():
#     print("You copied some text!")

# def paste():
#     print("You pasted some text!")


# window = Tk()
# # window.geometry("420x420") 
# window.title("Menu Bar") 

# openImage = PhotoImage(file="logo.png")

# menubar = Menu(window)
# window.config(menu=menubar)

# fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="file",menu=fileMenu)
# fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
# fileMenu.add_command(label="Save",command=saveFile)
# fileMenu.add_separator()
# fileMenu.add_command(label="Exit",command=quit)

# editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="Edit",menu=editMenu)
# editMenu.add_command(label="Cut",command=cut)
# editMenu.add_command(label="Copy",command=copy)
# editMenu.add_command(label="Paste",command=paste)

# window.mainloop()



# # Frames
# from tkinter import *

# window = Tk()
# window.geometry("420x420") 
# window.title("Frames") 

# frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
# # frame.pack(side=BOTTOM)
# frame.place(x=100,y=100)

# Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
# Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

# window.mainloop()



# #  New Windows
# from tkinter import *

# def create_window():
#     new_window = Tk()   # you can also use TopLevel(), this is a new window ontop of the other window and if the old window is closed, the new one will too 
#     window.destroy()                    # Tk() is a new window all together

# window = Tk()
# # window.geometry("420x420") 
# window.title("New Windows") 

# Button(window,text="create new window",command=create_window).pack()

# window.mainloop()



# #  Window Tabs
# from tkinter import *
# from tkinter import ttk

# window = Tk()
# # window.geometry("420x420") 
# window.title("Window Tabs") 

# notebook = ttk.Notebook(window)     # This is a widdget that manges a collection of windows/displays

# tab1 = Frame(notebook)
# tab2 = Frame(notebook)

# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2,text="Tab 2")
# notebook.pack(expand=True,fill="both")          # This is will fill space not otherwise used, Fill will fill space on x and y axis

# Label(tab1,text="Hello, This is tab1",width=50,height=25).pack()
# Label(tab2,text="Hello, This is tab2",width=50,height=25).pack()

# window.mainloop()



# # Grid Manager
# from tkinter import *

# window = Tk()
# window.geometry("420x420") 
# window.title("Grid") 

# titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

# firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
# firstNameEntry = Entry(window).grid(row=1,column=1)

# lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
# lastNameEntry = Entry(window).grid(row=2,column=1)

# emailLabel = Label(window,text="email: ",bg="blue",width=30).grid(row=3,column=0)
# emailEntry = Entry(window).grid(row=3,column=1)

# submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

# window.mainloop()



# # Progress Bar
# from tkinter import *
# from tkinter.ttk import *
# import time

# def start():
#     GB = 100
#     download = 0
#     speed = 1
#     while(download<GB):
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download+=speed
#         percent.set(str(int((download/GB)+100))+"%")
#         text.set(str(download)+"/"+str(GB)+" GB completed")
#         window.update_idletasks

# window = Tk()
# # window.geometry("420x420") 
# window.title("Progress Bar") 

# percent = StringVar()
# text = StringVar()

# bar = Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)

# percentLabel = Label(window,textvariable=percent).pack()
# taskLabel = Label(window,textvariable=text).pack()

# button = Button(window,text="download",command=start).pack()

# window.mainloop()



# # Canvas
# from tkinter import *

# window = Tk()
# # window.geometry("420x420") 
# window.title("New Windows") 

# canvas = Canvas(window,height=500,width=500)
# # canvas.create_line(0,0,500,500,fill="blue",width=5)
# # canvas.create_line(0,500,500,0,fill="red",width=5)
# # canvas.create_rectangle(50,50,250,250,fill="purple")

# # points = [250,0,500,500,0,500]
# # canvas.create_polygon(points,fill="yellow",outline="black",width=5)

# # canvas.create_arc(0,0,500,500,fill="green",style=PIESLICE,start=0,extent=180)

# canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
# canvas.create_oval(190,190,310,310,fill="white",width=10)
# canvas.create_oval(220,220,280,280,width=1)

# canvas.pack()

# window.mainloop()



# # Keyboard Events
# from tkinter import *

# def doSomething(event):
#     # print("You pressed " + event.keysym)
#     label.config(text=event.keysym)

# window = Tk()
# # window.geometry("420x420") 
# window.title("Keyboard Events") 

# window.bind("<Key>",doSomething)    # <Return> for enter, <Key> for any key

# label = Label(window,font=("Helvetica",100))
# label.pack()

# window.mainloop()



# # Mouse Events
# from tkinter import *

# def doSomething(event):
#     print("You did something! " + str(event.x) + ", " + str(event.y))

# window = Tk()
# # window.geometry("420x420") 
# window.title("Mouse Events") 

# # window.bind("<Button-1>",doSomething)         # <Button-1> is left click, <Button-2> is clicking on the scroll wheel, <Button-3> is a right mouse click
# # window.bind("<ButtonRelease>",doSomething)
# # window.bind("<Enter>",doSomething)            # When you mouse enters the window, it will begin the function
# # window.bind("<Leave",doSomething)
# window.bind("<Motion>",doSomething)

# window.mainloop()



# # Drag and Drop
# from tkinter import *

# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y

# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)

# window = Tk()
# window.geometry("420x420") 
# window.title("Drag and Drop") 

# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)

# label2 = Label(window,bg="blue",width=10,height=5)
# label2.place(x=100,y=100)

# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)

# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)


# window.mainloop()



# # Move Images w/ keys
# from tkinter import *

# def move_up(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()-10)

# def move_down(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()+10)

# def move_left(event):
#     label.place(x=label.winfo_x()-10, y=label.winfo_y())

# def move_right(event):
#     label.place(x=label.winfo_x()+10, y=label.winfo_y())

# window = Tk()
# window.geometry("500x500") 
# window.title("Move Images w/ keys") 

# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)

# # Arrow keys
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)

# myimage = PhotoImage(file="images\\racing.png")
# label = Label(window,image=myimage)
# label.place(x=0,y=0)

# window.mainloop()



# # Move Images on a Canvas
# from tkinter import *

# def move_up(event):
#     canvas.move(myimage,0,-10)

# def move_down(event):
#     canvas.move(myimage,0,10)

# def move_left(event):
#     canvas.move(myimage,-10,0)

# def move_right(event):
#     canvas.move(myimage,10,0)


# window = Tk()
# # window.geometry("420x420") 
# window.title("Move Images on a Canvas") 

# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)

# # Arrow keys
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)

# canvas = Canvas(window,width=500,height=500)
# canvas.pack()

# photoImage = PhotoImage(file="images\\racing.png")
# myimage = canvas.create_image(0,0,image=photoImage,anchor=NW)

# window.mainloop()



# # Animations
# from tkinter import *
# import time

# WIDTH = 500
# HEIGHT = 500

# xVelocity = 3
# yVelocity = 2

# window = Tk()
# # window.geometry("420x420") 
# window.title("Animations") 

# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# background_image = PhotoImage(file="logo.png")
# background = canvas.create_image(0,0,image=background_image,anchor=NW)

# photoImage = PhotoImage(file="images\\racing.png")
# myimage = canvas.create_image(0,0,image=photoImage,anchor=NW)

# image_width = photoImage.width()
# image_height = photoImage.height()

# while True:     # if your running a game, you may use: while running
#     coordinates = canvas.coords(myimage)
#     print(coordinates)
#     if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#         xVelocity = -xVelocity
#     if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
#         yVelocity = -yVelocity
#     canvas.move(myimage,xVelocity,yVelocity)
#     window.update()
#     time.sleep(0.01)

# window.mainloop()



# # Multiple Animations
# from tkinter import *
# from ball import *
# import time

# window = Tk()
# # window.geometry("420x420") 
# window.title("Multiple Animations") 

# WIDTH = 500
# HEIGHT = 500

# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# # canvas,x,y,diameter,xVelocity,yVelocity,color
# volley_ball = Ball(canvas,0,0,100,1,1,"white")
# tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
# basket_ball = Ball(canvas,0,0,125,8,7,"orange")

# while True:
#     volley_ball.move()
#     tennis_ball.move()
#     basket_ball.move()
#     window.update()
#     time.sleep(0.01)

# window.mainloop()



# # Clock
# from tkinter import *
# from time import *

# def update():
#     time_string = strftime("%I:%M:%S %p")
#     time_label.config(text=time_string)

#     day_string = strftime("%A")
#     day_label.config(text=day_string)

#     date_string = strftime("%B %d, %Y")
#     date_label.config(text=date_string)

#     # You could use time_label.after(1000,update) too update just one
#     window.after(1000,update)

# window = Tk()
# # window.geometry("420x420") 
# window.title("Clock") 

# time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
# time_label.pack()

# day_label = Label(window,font=("Ink Free",25))
# day_label.pack()

# date_label = Label(window,font=("Ink Free",30))
# date_label.pack()

# update()

# window.mainloop()



# # Send An Email
# import smtplib

# sender = 'sender@gmail.com'
# receiver = 'receiver@gmail.com'
# password = 'password'
# subject = 'Python email test'
# body = 'I wrote an email'

# message = f"""From: First Last{sender}
# To: First Last{receiver}
# subject: {subject}\n
# {body}
# """

# # 587 is the default mail submission number
# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()

# try:
#     server.login(sender,password)
#     print("Logged in...")
#     server.sendmail(sender, receiver, message)
#     print("Email has been sent")

# except smtplib.SMTPAuthenticationError:
#     print("unable to sign in")



# Python File With Command Prompt