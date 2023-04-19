
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