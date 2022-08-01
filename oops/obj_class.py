# Basics: Python used namemangling to alter private varaibles.
# Mangled name of private variable = _classname__privatemenbervariablename


class student:
    #public member variables
    student_name="stname"
    student_age="stage"
    #private member variables
    __student_grades="stgrades" # name will be mangled as "_student__student_grades"
    # Constructor of the class
    def __init__(self,name,age):
        print("Here is the constructor call")
        # by default class members are public in python
        self.student_name = name
        self.student_age = age
        #self.__student_grades = grades #this will be unaccesible. No member varible
    def getgrades(self):
        return self.__student_grades
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(dir(student)) # to display all the attributes of class
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#creating object
st1 = student("satish", 28)
print(st1.student_name)
print(st1.student_age)
#print(st1.__student_grades) #since name is mangled, it will show error student object has no attribute '__student_grades' 
print(st1._student__student_grades) # will print stgrades
print(st1.getgrades()) #varifying with function call
st1._student__student_grades = "newgrades" # in python, updating of private variables is possible by using mangled name
print(st1._student__student_grades) # will print newgrades
print(st1.getgrades()) #varifying with function call. Private variable is updated.

