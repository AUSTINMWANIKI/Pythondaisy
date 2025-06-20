class Student:
    #Propeties/Attributes
    name="Eliud"
    gender="male"
    age=34

    def study(self):
        print("Student is studying")

    def movement(self):
        print("Student is walking")

student1 = Student() #Creating an object
student1.movement()
print(student1.name)


student2=Student()
student2.age()
print(student2.name)


