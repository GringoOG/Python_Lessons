
# open("Jméno souboru", "operace")
# r - read, w - change the file, a - append on the end of the file, r+ - read and writee

employee_file = open("textovka.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

print(employee_file.readable())
print(employee_file.read())
print(employee_file.readline)  # read 1. line
print(employee_file.readline)   # read 2. line
print(employee_file.readlines()[1]) #index of what to read

