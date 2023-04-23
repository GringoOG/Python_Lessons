
txt = "   prdelačka"
txt.strip() # vymaže whitespace na začátku
txt.upper()

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits) # add list items to set

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["year"] = 2020

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red" # add

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model") #remove

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear() #remove all

i = 1
while i < 6:
  if i == 3:
    break
  i += 1  #loop till 3



i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
print(i) #In the loop, when i is 3, jump directly to the next iteration.


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #loop through items



def my_function(*kids):
  print("The youngest child is " + kids[2]) # If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition



def my_function(**kid):
  print("His last name is " + kid["lname"]) # If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition



x = lambda a:a # Create a lambda function that takes one parameter (a) and returns it.


class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)  # Use the p1 object to print the value of x:


class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()        #We have used the Student class to create an object named x., What is the correct syntax to execute the printname method of the object x?


import mymodule as mx #If you want to refer to a module by using a different name, you can create an alias.


dir() #The dir() function returns all properties and methods of the specified object, without the values. This function will return all the properties and methods, even built-in properties which are default for all object.


from mymodule import person1 #  syntax of importing only the person1 dictionary of the "mymodule" module


str="there are no traffic JamS Along The extra mile."

#Type your answer here.
str = str.capitalize()

print(str)


str="There are no traffic jams along the extra mile."
#  Type your code here.

# ans_1=str.startswith("A")
print(ans_1)

# ans_1= str.endswith(".")
# ans_1=str.find("m")

def stutter(word):
	 return word[0:2] + '... ' + word[0:2] + '... ' + word + '?' #1st 2 letters and ..


def distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False

print(distinct([1, 5, 7, 9]))
print(distinct([2, 4, 5, 5, 7, 9]))


import random
char_list = ["a","e","i","o","u"]
random.shuffle(char_list)
print("".join(char_list))


def remove_nums(int_list):
  position = 3 - 1
  idx = 0
  len_list = len(int_list)
  while len_list > 0:
    idx = (position + idx) % len_list
    print(int_list.pop(idx))
    len_list -= 1


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
remove_nums(nums)