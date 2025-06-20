from variables import language

# While loop
number=20

while number <= 25 :
    print(number)
    number += 1

#Decrementing
count = 105
while count >= 100:
    print("Number is",count)
    count-=1

#Break and Continue
a = 20
while a <=25:
    print(a)
    if a== 23:
        break
    a += 1

counter=35
while counter<=40:
    if counter==37:
        counter+=1
        continue
    print(counter)
    counter += 1


#For Loop
languages=["Python","C++","Java","PHP"]
for lang in languages:
    print(lang)

for num in range(5):
    print(num)

for x in range(10,15):
    print(x)

for z in range(10,20,3):
    print(z)


