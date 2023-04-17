class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name #actual attribute of object - I need pass it in
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
#this is class - just overview, what student data type is

    def on_honnor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False