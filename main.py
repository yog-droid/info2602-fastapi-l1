# x = 10
# print(x)
# x = 23
# print(x)

# #y = None
# #print(y)

# y = 2

# z = (x+y)/x + 2
# print(z)

# name = "Bethany"
# nameType = type(name)
# print(nameType)

# age = 24
# typeofage = type(age)
# print(typeofage)

# height = 6.5
# heightType = type(height)
# print(heightType)

# hasDate = False
# hasDateType = type(hasDate)
# print(hasDateType)

# comp = 3 + 4j
# compType = type(comp)
# print(compType)

# message = f'Hi my name is {name} I am {age} years old'
# print(message)

# intHeight = int(height)
# print(intHeight)

# name = input("What is your name? ")
# print(name)

# if 3 > 5:
#     print("3 is more")
# else:
#     print("3 is less")

# mark = input("Enter mark: ")
# mark = int(mark)
# if mark > 70:
#     print("A")
# elif mark > 60:
#     print("B")
# elif mark > 50:
#     print("C")
# else:
#     print("F")

# i = 1
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("This is run when the loop condition is no longer met")

# list = ["bob", "sally", "john"]
# for j in list:
#     print(j)

#     for i in range (0, 10, 2): #0 is start, 10 is end, 2 is iteration incrementation
#         print(i)

# def add(a, b):
#     return a + b

# def printPerson(name, age, height):
#     print(name, age, height)

#     printPerson(age=24, name="Bethany", height=5)

# #default arguments are used when they are not given in the function call
# def sayHello(fname, lname='Smith'):
#     print('Hello '+fname + ' ' + lname)

# sayHello('John')

# sayHello('Bill', 'Young')

# # functions can return multiple values
# def multiReturnFunc(a,b):
#     return a+b, a-b, a*b, a/b

# # You can assign multiple variables to the values being returned by the function
# numSum, numDiff, numMult, numDiv = multiReturnFunc(10,5) 
# print(numSum, numDiff, numMult, numDiv)



# list = ['item1', 'item2', 'item3']
# list2 = [12, 33, 45, 58, 23]

# print(list)
# # negative indexing can access elements starting from the end
# print(list2[-1])

# # select a subset of a list
# print(list2[2:4])

# # gets the length of a list
# print(len(list2))

# #add items to list
# list.append('item4')

# #remove item from list
# item4 = list.pop()

# #copy list
# list3 = list2.copy()

# num = [1,2,3,4]
# doubled = [n*2 for n in num]
# print(doubled) # [ 2, 4, 6, 8]
# odd = [ n for n in num if n%2 == 1]
# print(odd) # [ 1, 3]

# # unpacking a list, lets you create variables from items in the list
# num = [ 1, 2, 3, 4]
# [first, second, *rest] = num
# print(first)
# print(second)
# print(rest)
# # joining lists
# num2 = [5, 6]
# num3 = num + num2
# print(num3) # [1, 2, 3, 4, 5, 6]

from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

### New Function
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: # select only the students with a given meal preference
              filtered_students.append(student) # add match student to the result
        return filtered_students
    return data
### End of new function

@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: # Only return the student if the ID matches
      return student

@app.get('/stats')
async def get_stats(dictStat= {"Chicken": 0,
                               "Computer Science (Major)": 0,
                                "Computer Science (Special)": 0,
                                "Fish": 0,
                                "Information Technology (Major)": 0,
                                "Information Technology (Special)": 0,
                                "Vegetable": 0}):
  
    for students in data: 
        if students['pref'] in dictStat:
            dictStat[students['pref']] += 1

        if students['programme'] in dictStat:
            dictStat[students['programme']] += 1

    return dictStat

@app.get('/add/{a}/{b}')
async def add_num(a: int, b: int):
    return a + b

@app.get('/subtract/{a}/{b}')
async def subtract_num(a: int, b: int):
    return a - b

@app.get('/multiply/{a}/{b}')
async def multiply_num(a: int, b: int):
    return a * b

@app.get('/divide/{a}/{b}')
async def divide_num(a: int, b: int):
    if b == 0:
        return "Unable to divide by zero"
    return a / b

