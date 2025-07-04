from oop import student1


class Subject:
    def _init_(self,name,points):
        self.__name = name
    #Public attribute
        self.__points=points
     #Private attribute(encapsulated)

    #Getter method to access private attribute__name
    def get_name(self):
        return self.__name

    #Setter method to get private attribute__name
    def set_name(self,new_name):
        self.__name=new_name

    #Getter method for points
    def get_type(self):
        return self.__points

    #Setter method for type
    def set_type(self,new_points):
        if new_points >80:
            self.__points=new_points
        else:
            print("Points are low")

#Create a subject
    s1= Subject ("English",69)

#Accessing private variables (using getter)
    print("Name:",s1.get_name())


#Accessing private attribute (using getter)
    print("Points",s1.get_points())


#Trying to set points using setter
    s1.set_points(74)
    print("Updated points",s1.get_points)

#Trying to access private attribute (will fail)
#print(p._points) #Uncommenting this line will raise an AttributeError






