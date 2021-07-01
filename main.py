import datetime

name = input("Tell me Your name: ")
age = int(input("Tell me Your age: "))
num = int(input("How many messages: "))

date = datetime.datetime.now()
year = (date.year - age) + 100

while num > 0:
    print("Hello " + name + " You will be 100 years old in " + str(year))
    num = num - 1
