#1.Built-Functions/Standard Library Functions

x=max(67,89,90,23,67,45)
print("The maximum number is",x)

y=min(67,89,90,23,67,45)
print("The minimum value is",y)

z=pow(2,3)
print("The power of 2 is",z)


#.User-Defined Functions
def greeting():
    print("Hello world")

greeting() #Calling a function

def school():
    print("My coding school is eMobilis")

school()

#Parameter and Argument
def add(num1,num2):
    print(num1+num2)

add(5,10)
add(14,13)

def student(fullname,course,gender):
    print(fullname,course,gender)

student("Bernhard Riemann","Mathematics","Male")
student("John Von Neumann","MIT","Male")
student("Otto Von Bismark","International relations","Male")
student("Johann Friedrick Gauss","Mathematics","Male")
student("Mary Mbotela","MIT","Female")

#Create a Python program that displays details of five employees at FinTech using Parameters and Arguments(fullname,email-address,age,position,salary,marriage status)

#User defined functions

#Parameter and Argument
def employee(company,fullname,email,age,position,salary,status):
    print(company,fullname,email,age,position,salary,status)

    employee("Fintech","Akelo Achieng","akeloachieng112@gmail.com",28,"Secretary","20000ksh","Single")
    employee("Fintech","Bildad Mwangi","bildadmwangi56@gmail.com",31,"Treasurer","25000ksh","Married")
    employee("Fintech","Melinda Njihia","melindanjihia24@gmail.com",25,"Lecturer","30000ksh","Single")
    employee("Fintech","Caesar Kariuki","caesarkariuki335@gmail.com",30,"Clerk","35000ksh","Married")
    employee("Fintech","Brandon Kudwoli","brandonkudwoli132@gmail.com",39,"Chairman","40000ksh","Married")



















