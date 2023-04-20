
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