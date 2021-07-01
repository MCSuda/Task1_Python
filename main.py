import datetime

name = input("Tell me Your name: ")
age = int(input("Tell me Your age: "))

date = datetime.datetime.now()
year = (date.year - age) + 100

print("Hello " + name + " You will be 100 in " + str(year))
