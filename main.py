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



# 