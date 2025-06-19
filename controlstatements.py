#Program1

age=int(input("How old are you:"))

if age > 18:
    print("You are a voter")
else:
    print("Your not a voter")

#Program 2
temperature=float(input("Enter current room temperature eg 23.0:"))

if temperature>25.0:
    print("It is too hot")

elif temperature<25.0:
    print("It is too cold")

else:
    print("Normal temperature")

print()


#Program3
first=int(input("Enter firstnumber:"))
second=int(input("Enter secondnumber:"))
third=int(input("Enter thirdnumber:"))

if first>second and first > third:
    print(first," is the largest number")

elif second>first and second>third:
    print(second,"is the largest number")

else:
    print(third,"is the largest number")


#Program4
age=float(input("Enter your age"))

if age==18:
    print("is a voter")
elif age>=18:
    print("is a voter")
else:
    print("not a voter")









