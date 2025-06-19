
courses=["FullStack","Datascience","CyberSecurity"]
print(courses)

#Accesing an element
print(courses[2])

#Looping through an array
for course in courses:
    print(course)

#Adding a new element
courses.append("UI/UX")
print(courses)

#Removing an element
courses.remove("DataScience")
print(courses)