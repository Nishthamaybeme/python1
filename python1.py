# note :if something written in #as a comment under a statement that means it is written for that statement information about any statement is under or just after the statement 
print("nishtha goyal")
print('o----')
print(' ||||')
#'' means defining a string
#python executes line by line 
print('*' * 10)
#here we are multiplying a string with number 10
# this results in 10 astricks 
#inline 6 it will evaluate the code that is in btw paranthesis ,our expression will produce 10 astericks 
# draw heart and ball as hw ????????????????????
price=10 
#price is the label to access the value in this box named price has a 10 
print('price')
#only price gives the v alue of price 
# while#price in quotes says the string and prints it 
# when we store 10 in memory it will be converted in to binary then will be saved
price=20
print(price)
# it executes line by line first it saves 10 then it saves 20 in the same name price so it has a new value of price and prnts 20 
# integers are whole numbers in programming without decimals
rating=4.9
# these are floating no 
name="nish"#string
is_published=False
# it is a boolean value 
# we use underscore to use multiple words 
# python is a case sensitive language when defining variables(name,is_published,rating,price)we should use lower case but 
# for False and True these are special keywords in the language which have uppercase 


#there is an exercise below suggesting name age and if its new or old patient and ive answered correctly 
name="John"
age=20
patient_new=True


# now,
# how to receive inputs
name=input("what is your name ? ")
# inbuilt function in python 
# it means we are calling 
#it will print this string and wait for user to imput the value 
print('HI '+ name)
# we combined a string with another string 
# exercise
color=input("what color do u like? ")
print(name + " likes " + color)
#dont forget to give spacing inside the quotation 

birth=input('birth year: ')
print(type(birth))
age= 2024-int(birth)
print(type(age))
print (age)
#error as we subtracted int and string
#we used int before birth to convert it into integer from string
weight=input("what is ur weight in pounds?")
weight=int(weight)
kilo=weight*0.453592
print(kilo )
course="Python"
print(course)
course='"python" for beginners'
print(course)
course="'pyhton' for beginners"
print(course)
# now if we want to print python but with quotes it will generate error so use a single quotes inside the double quotes now when we need to add double quotes inside we add single quotes outside 
# now we want to write a huge length of text
# we will use triple quotes
course='''hi 
kohn 
is it our first email '''
print(course)
course='Python for Beginners'
       #01234567891011121314....
       #     -14-13-12-11-10-9-8-7-6-5-4-3-2-1
       #square
#negati barcekets working
# -ve 1 will give u last character as it assumes 0 as the index of first letter p

print(course[-13])
print(course[0:3])
# it iwll print 0 1 2 pyt not 3 it excludes the last letter
print(course[0:])
#print the whole 
#*************************shift + alt+ down key for copying down********ctrl + enter for changing to next line ****************
print(course[1:])
# it exempts the p (first letter)
print(course[:5])

#it will assume 0 as the start index and print pytho
nother=course[:]
# this clone the whole string [:]
print(nother)
name ='jennifer'
print(name[1:-1])

first='john'
last='smith'
#formatted strings
message=first + ' [' + last +'] is a coder'
msg=f'{first} [{last}] is a coder'
# formatted string f'' -prefix {content} the things in between the braces are degining placeholders for the variables 
#prefix your string with f and use curly braces to dynamically insert values in your string 
print(msg)
course='python for beginners'
print(len(course))
#helps if user need a limited characters 
# general purpose function
print(course.upper())
print(course)
#this doesnt change or modify our old string it creates a new string and returns it 
# we refer a function as method
print(course.lower())
# find a chaaracter or sequence of character
print(course.find('for'))
#for begins at 7 th index
# find is case sensitive 
# if u pass upper case p it will give -1 
# method to replace a characyer
print(course.replace('beginners','begin'))
#it also case senssitive 
print(course)
#if the string contains a particular word?
print('python' in course)#it is a boolean exp 
print('Python' in course)#it is a boolean exp 
print(course.title())
#it capatalises the first alphabt of all the words 
# It considers any non-alphabetic character as a word boundary, so "hello-world" would become "Hello-World".
# It does not handle certain edge cases well, such as proper handling of apostrophes in words (e.g., "o'clock" would become "O'Clock" instead of "O'clock").
# it is case senstive 
# in operator makes it a boolean value 
text = "hello, world! it's a wonderful day."
title_text = text.title()
print(title_text) 
 # Output: "Hello, World! It'S A Wonderful Day."
print(10/3)#floating output 
print(10//3)#int poutput
print(10%3)#gives remainder
print(10**4)#10^4
x=10
x=x+3
x-=3 
x=10+3*2#bodmas outputs 16
print(x)
# operator precedence from top to bottom below:
# paranthesis
# exponentiation 2**3
# multiply or divide 
# add or subtract
x=10+3*2**2#22

x=(10+3)*4-3#first we will solve paranthesis 13 then multiply 13*4 then subt 3 49 is ans 
print(x)
x=2.5#2(floor value)
print(round(x))
#it gives the roundoff of the function
x=-2.5
print(abs(x))#it makes every result postive even if  a fucntion is negative 
import math 
print(math.ceil(2.9))#gave roundoff 
print(math.floor(2.9))#gave roundoff in floor value 
import webbrowser
link="https://docs.python.org/3/library/math.html"
# webbrowser.open(link) 
# use the code above to read all math fucntions 
is_hot=False
is_cold=False
if is_hot:
    print("it's a hot day")
    print("its very hot")
    #when we add enter after colon it indents our print statemnt below is_hot so it comes under the if bracket when we enter shift + tab after it the indentation removes and the fourth line starts from left pnly which isnot under the if statemnet just like{ curly braces in c }indentaion acts like curly braces
elif is_cold:
    print("its cold")
else:
    print("enjoy ur day")# default statment 
 # exericise
price = 1000000
good_cred=True
if good_cred:
    down=(10*price)/100
    
else:
      down=(20*price)/100
print(f"Down payment:${down}")
# logical operators 
high_cred=False
high_inc=False
if high_cred and high_inc:
     print("loan eligible")

# and=both true
# or = at least one true
# not= make a statement false
 
good_cred=True
crimi_rec=True
if good_cred and not crimi_rec:
    print("loan allow")#nothing will be printed since not operator will turn the true to false and operator wont work since one is true and other is turned false by the not operator 
    temp=30
#== compare
#!= compare unequal
if temp>30:
    print("it hot")
else:
    print("not hot")
    
name="pikachu"
if len(name) <3:
    print("name atlleast 3 character")
elif len(name)>50:
    print("name can be max 50 character")
print("name looks good")
weight=int(input("enter your weight:"))
# weight=input("enter your weight:")
unit=input("enter unit:(L)bs or (K)g:")
if unit.upper()=="L":
#     weight=0.45*int(weight) 
    weight=0.45*weight
    print(f"youre {weight} kg")
else:
    weight=int(weight)/0.45
    print(f"youre {weight} pounds")
#rating myself 9/10 since i wasnt able to use upper since i forgot the braces after it is used as variable.upper()
#  while loops
i=1
while i<=5:
    print(i)
    i=i+1
print("done")
    
#*************guess game ***************
# # Guess:1
# Guess:2
# Guess:3
# sorry u failed
secret=9
count=0#noo of guesses
while count<3:
    guess=int(input("guess the number:"))
    if secret==guess:
        print("u won")
        
    count=3 

print("you failed")


# # >help
# # start - to start the Car
# # stop  to stop the car 
# # quit- to exit 
# # >asd
# # i dont understand that 
# # >start 
# # car started ready to go 
# # >stop 
# # car stop
# # >quit
# # quit the game
help='''start-to start the Car
stop-to stop the car 
quit-to exit'''
bar=""
started=False
while True:
   bar=input(">")
   if bar.upper()=="HELP":
       print(help)
   elif bar.upper()=="START":
               if started:
                       print("car already started")
               else:
                       started=True
                       print("Car started ....Ready to Go.....")
               
   elif bar.upper()=="STOP":
                 if not started:
                         print("car is already stopped")
                 else:
                         started=False
                         print("Car Stopped .......")
                 
   elif bar.upper()=="QUIT" :
           break 
   else: 
         print("i cant understand you ")   


for item in 'python':
    print(item)



for item in [1,2,3,4]:
        print(item)
for i in range(5, 10,2):#5 to 10 and 2 steps forward
      print(i)

tot=0
prices=[10,20,30]
for each_price in prices:
      tot+=each_price
print(tot)


# nested loop 
for x in range(4):#it prints 0 to 3
    for y in range(3):
        print(f'({x},{y})')


        number=[10,2,5,7,4]
# for each_number in number:
#    print('x'* each_number)
# number[0]=2
# print(number)
x=number[0]
for i in number:
    if i>x:
        x=i
        print('looping')
   
print(x)
    
print(matrix[0][1])#1 st row and 2 nd column (0 1 2 columns and 0 1 2 rows
matrix[0][1]=20
print(matrix[0][1])

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]#2d list each item has another list
for row in matrix:
    for item in row:
       
        print(item)
    print('newline')        


    numbers=[5,3,2,1,4,5]
# numbers.append(20)
# print(numbers)
#[5, 3, 2, 1, 4, 5, 20]
# numbers.insert(0,20)--0 is the index and 20 is the item we added 
# print(numbers)
# numbers.remove(x) -- removes the no x from the list
# numbers.clear()-- clears the list
# numbers.pop() -- pops out the last no top element of stack
# print(numbers.index(5))--it shows the first appearnce of that number in the list index of that number that is 0 in this case is output 
# if any no that is not in the list it will show value error 
# print(numbers.index(50))--
# ValueError: 50 is not in list
# print(50 in numbers)--this method generates a boolean value and not an error safer than index method 
# False is the output in this case 
# print(numbers.count(5))--counts ooccurence of 5 output is 2here
# numbers.sort()
# numbers2=numbers.copy()
# numbers.append(10)

# print(numbers2)
# unique=[]
# for number in numbers:
#     if number not in unique:-- not in is an operator 
#         unique.append(number)

# # removes multiple same no 
# print(unique)
# numbers=(1,2,3)
# # ( for tuple)
# numbers[0]=20
# TypeError: 'tuple' object does not support item assignment
# # print(numbers[0])
# coordinates=(0,2,3)
# x=coordinates[0]
# y=coordinates[1]
# z=coordinates[2]
# x*y*z
# x,y,z = coordinates --can be used in both list and tuple and is called unpacking 
# --this is same as step no 35 36 37 
# print(y)

# dictionary in pyhton
# customers={
#     "name": "nishtha goyal ",
#     "age": 20,
#     # each word should be unique 
#     "is verified": True
# }
# print(customers["name"])
# print(customers["Name"])--error 
# print(customers["birthday"])--KeyError
# print(customers.get("brithfdate"))-- wont run an error and will say none 
# # # print(customers.get("birthdate","january"))-- instead of getting none we got january as output of brthdate
# # customers["name"]="john"
# # # customers["birthdate"]="january 19 "--we can add new elements to our dictionary at any time 
# # print(customers["name"])
# # we cam see output as nishthagoyal first and john second since we have assgined name another value 
# phone=input("phone: ")
# digits_mapping={
#     '1':"one",
#     "2":"two",
#     "3":"three"
# }
# output=""
# for ch in phone:
#    output+= digits_mapping.get(ch,"!") +" "

    

# print(output)
# message=input(">")
# words=message.split(' ')
# emojis={
#     "ho:)": "😊",
#     ":(": "😔"
# }
# output=""
# for word in words:
#   output+=  emojis.get(word,word)+" "
# # good morning :)
# print(output)
# 2:30

# functions to better organize our code
# greet_user()--python dont knnow this function sicne it si written below
# def greet_user():
#     # defining a func is used by def keyword
#     print("hi there")
#     print("welcome aborad")

#     # two line break after declaring a funciton
#     #exectuion start from below 
# print("start")
# greet_user()
# print("finish")

def greet_user(name,last_name):
    # defining a func is used by def keyword
    print(f"hi {name} {last_name}")
    # -- f is used for formatted string
    print("welcome aborad")


print("start")
# greet_user("john")-- postional argument,arguments is the value supplied to the function and name is the parameter (placeholder to receive information)and argument is the actual information supplied in those placeholders 
greet_user("mary","smith")
print("finsh")


# # positional arguments is that there psotion matters
# # keyword arguments
# def greet_user(name,last_name):
  
#     print(f"hi {name} {last_name}")#position is defined according to this 
#     print("welcome aborad")

# print("start")
# # greet_user("john",last_name="smith") use keyword arguments after psoitional arguments
  #this is a keyword argument its postion doesnt matter
# calc_cost(total=50,ship=5,discount=0.1) power of keyword arguments in numerical values

# def square(number):
#     # print( number*number)-- this is executed
# #it returns values--return or else without return it will return none 



# print(square(4))


def emoji_converter(message):
    words=message.split(' ')
    emojis={
        ":)": "😊",
        ":(": "😔"
    }
    output=""
    for word in words:
        output+=emojis.get(word,word)+ " "
    return output


message=input(">")
print(emoji_converter(message))


try:
    age=int(input("age: "))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("Invalid input")
except ValueError:
    print('ivalid input')

    #comments good comments are those which explains why and how and not what 
class PointCards:
    
#pascal naming convention for classes 
# inclasses we dont use underscore we just capatalise the first letter of every word
    def move(self) :
        print("move")
    def draw(self):
      print('pink')  
      view=2+3  
      print(view)       


point1=PointCards()
point1.x=10
point1.y=20
print(point1.z)



class Person:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def talk(self):
        print(f"Hi, I am {self.name} ")

bob=Person("bob",40)
nish=Person("nishtha","ggg")
print(bob.health)
nish.talk()

#inheritance 
class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("bark")

 

class Cat(Mammal): 
   pass
 

dog1=Dog()
dog1.walk()
dog1.bark()
#converter.py
def lbs_to_kg(weight):
    return weight*0.45


def kg_to_lbs(weight):
    return weight/0.45


import converters
from converters import kg_to_lbs  
kg_to_lbs(100)

print(converters.kg_to_lbs(70))
# utils.py
def find_max(numbers):
     maxm=numbers[0]
     for number in numbers:
        if number>max:
            maxm = number 
     return maxm

    

from utils import find_max

numbers=[12,23,4,4]
maxm=find_max(numbers)
print(maxm)
# packages?first way
import ecomerce.shipping
ecomerce.shipping.calculate_shipping()

#packages two ways 
from ecomerce.shipping import calculate_shipping
# for exapmlple

calculate_shipping()

import random 
# for i in range(3):

#     print(random.randint(12,20))
# members=["","mosh"]
# leader=random.choice(members)
# print(leader)

class Dice:
    def row(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second
#return a tuple we dont need to add apranthesis


dice=Dice()
print(dice.row())

from pathlib import Path

path=Path()
# print(path.mkdir())
# print(path.rmdir())
for file in path.glob('*'):
    print(file)
