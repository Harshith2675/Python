# Functions:
'''def greet_user():
    print('Hi Harshith!! ')
    print('Welcome America..')


print('Start..')
greet_user()
print('Finish')
'''

#Parameters:
'''def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome USA..')


print('Start....')
greet_user('Harshith','Sinhyana')
greet_user('Pranay','Brundha')
print('finish')'''


#Keyword Arguments
'''def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome USA..')


print('Start....')
greet_user(last_name = 'Harshith',first_name='Sinhyana')
greet_user(last_name='Pranay',first_name='Brundha')
print('finish')'''

'''# print Duplicate Characters.
word = input("Enter a word: ")
unique = ""

for Character in word:
  if Character not in unique:
      unique += Character

print(unique)

for Character in unique:
  if(word.count(Character) > 1):
      print(Character, end = " ")'''

'''#Fibonacci series using Functions:
def fibonacci_series(values):
      num1, num2 = 0, 1
      for i in range(1, values+1, +1):
        print(num1 , end=" ")
        num3 = num1 + num2
        num1 = num2
        num2 = num3

#drive code
values = int(input("Enter the number of values: "))
fibonacci_series(values)'''

'''#Return Statements.
def square(number):
    return number * number

res = square(6)
print(res)'''

''' OOPS
#Exceptions..
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0!!")
except ValueError:
    print("Invalid..")
'''

'''#Classes
class Point:
    def draw(self):
        print("Draw a circle")

    def move(self):
        print("Move Forward")

Point1 = Point()
Point1.x = 20
Point1.y = 40
print(Point1.x)
Point1.draw()


Point2 = Point()
Point2.x = "Harshith"
Point2.y = "Pranay"
print(Point2.x)
Point2.move()'''

#Constructor..
'''class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print("Draw a circle")

    def move(self): 
        print("Move Forward")

Point1 = Point(10,20)
Point1.x = 20
Point1.y = 40 # Updating the x and y values....
print(Point1.x)
print(Point1.y)
Point1.move()
Point1.draw()'''

'''#Exercise for constructor..
class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f'Hi,I am {self.name}')

    

Harshith = Person('Chinnu')
Harshith.talk()
'''

'''#Inheritance..
class Mammal:
    def walk(self):
        print("Walking ")

class Dog(Mammal):
    def bark(self):
        print("Barking")

class Cat(Mammal):
    pass

dog = Dog()
dog.walk()
dog.bark()
'''

'''#Random Values.
import random

class Dice:
    def roll(self):
        first = random.randint(1 ,6)
        second = random.randint(1 ,6)
        third = random.randint(1 ,6)
        return (first,second,third)

dice = Dice()
print(dice.roll()) ''' 
