
"""
#strings are arrays
a = "I am actually array"
print("there has to be: I",a[0],"there has to be white space", a[1])
#check certain phrase from string
my_string = "hello my name is rauf odilov"
print("rauf" in my_string)
for i in my_string.split(' '):
    if i == "rauf":
        print("We found your request")
    break
a, b =30, 20
c, d = a*b, a+b
print(c, d)
# multiplication and summation function
def multisum(item1, item2):
    multi_result = item1 * item2
    sum_result = item1 + item2
    if multi_result >= 1000:
        return multi_result
    else:
        return sum_result

a, b = 150, 250 
result = multisum(a, b)
print(result)

# print previous currrent sum
def iterate_number(item):
    for i in range(item):
        if i == 0:
            print("Current number is: {}, previous number is: {}, sum: {}".format(i,i,i))
        else:
            print("Current number is: {}, previous number is: {}, sum: {}".format(i,i-1,i+(i-1)))
number = input("Please enter the number")
iterate_number(int(number))

previous_num = 0
for i in range(10):
    print("Current number is {}, previous number is: {}, sum of their number is: {}".format(i, previous_num, i+previous_num))
    previous_num = i
# string even position
def my_function(item):
    for i in item:
        if item.index(i)%2==0:
            print("Our result is: ", i)
        else:
            pass
mystr = "raufodilov"
my_function(mystr)
#remove n characters from string
def myfunk(item, key):
    print(item[key:])

mystr="hellomynamerauf"
number=4
myfunk(mystr, number)
def listfirstlast(item):
    if item[0]==item[-1]:
        return True
    else:
        return False
list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,1]
print(listfirstlast(list1))
print(listfirstlast(list2))
#divisible by 5
def divfive(item):
    newlist = list(i for i in item if i%5==0)
    return newlist
mylist = [12,40,45,55,67,89]
print(divfive(mylist))
#find substring
def findsubstr(item):
    counter = 0
    for i in item.split(' '):
        if i == "rauf":
            counter +=1
        else:
            pass
    return counter

mystr = "rauf the best programmer, because he is rauf"
print(findsubstr(mystr))
result = mystr.count("rauf")
print(result)
#print(pattern
def printpattern(item):
    for i in range(1, item+1):
        for j in range(i):
            print(str(i), end=" ")
        print("\n")
number = 5
printpattern(number)
#check palindrome number
def findpalindrom(item):
    mystr = str(item)
    palstr = mystr[::-1]
    if mystr==palstr:
        return "Yes this number is Palendrom"
    else:
        return "Sorry, this number is not palendrom"
entered_number = input("Enter number")
print(findpalindrom(entered_number))
#create list from two list
def createlist(item1, item2):
    newlist1 = [i for i in item1 if i%2==0]
    newlist2 = [i for i in item2 if i%2!=0]
    newlist1 += newlist2
    return newlist1
num1 = [1,2,3,4,5,6,7]
num2 = [12,13,4,15,16]
print(createlist(num1, num2))
# extract digits
def extractdig(item):
    stringmy = ""
    givenstr = str(item)
    for i in givenstr[::-1]:
        stringmy += i
        stringmy += ' '

    return stringmy

number = 123456
print(extractdig(number))
# print multiplication
for i in range(1,11):
    for j in range(1, 11):
        print(i*j, end=' ')

    print("\n")
# print over pyramid
number = 5
while number>0:
    for i in range(number):
        print("*", end=" ")
        
    print("\n")
    number -=1
# exponent fucntion
def exponent(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result
print(exponent(5,4))
#take input and multiply
checker = True
while checker:
    print("Please enter two input numbers and we calculate it")
    num1 = int(input("Your first number is: "))
    num2 = int(input("Your second number is: "))
    result = int(num1*num2)
    print("This is calculation result of your numbers: ", result)
    signal = input("To exit enter \" X \"")
    if signal == "X":
        checker = False
    else: pass
#format float
fnum = 45.6789
print('%.2f' %fnum)
# accept float list
cheker = 5
mylist = []
while cheker > 0:
    a = input("Enter float number: ")
    mylist.append(a)
    cheker -= 1

print(mylist)
#copy content file
txt = \"""line1,
    line2,
    line3,
    line4,
    line5,
    line6
    \"""
with open('old_file.txt', 'w') as f:
    for line in txt:
        f.writelines(line)

with open('old_file.txt', 'r') as f:
    lines = f.readlines()

with open('new_file.txt', 'w') as f:
    count = 0
    for line in lines:
        if count ==4:
            continue
        else:
            f.write(line)
        count +=1

with open('new_file.txt', 'r') as f:
    for i in f:
        print(i)
# input multiple string
str1, str2, str3 = input("Enter three name").split()
print("First: {}, second: {}, third: {}".format(str1, str2, str3))

with open('new_file.txt', 'r') as f:
    lines = f.readlines()
    print(lines[2])

"""
"""
def function(key, *arg):
    print(key)
    for i in arg:
        print(i)
    return 
function("Rauf", [1,2,3,4,5,6,7,8,9])

# lambda function
my_lambda = lambda x, y: x**y

result = my_lambda(2,4)
print(result)

def say_hello(item):
    print("Welcome to our model", item)

with open("mynewfile", 'w') as f:
    f.write("This is great file in this location")
    f.close()

with open("mynewfile", 'r') as f:
    result = f.read()
    print("this is our result: ", result)

import os
os.remove("mynewfile")

from os.path import exists
file_exists = exists("mynewfile")
print(file_exists)

rr = os.getcwd()
print(rr)

#exception handling
try:
    with open("nynewfile", 'r') as f:
        lines = f.readline()
        print("Our result is here: ", lines)

except IOError:
    print("We could not find such file \n Sorry for that!")
else:
    print("The lines successfully readed from the file")
    f.close()

"""
# create class

class Myclass:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_funk(self):
        print("This is function from class and here you can find car: {}, and here its price is written price: {}".format(self.name, self.price))

obj1 = Myclass("Zara", 1235)
obj1.print_funk()

# Inheritance
class Parent:
    Atrr = 100
    def __init__(self):
        print("THis is parent class constructor")
    
    def parent_Method(self):
        print("This METHOD is from parent class")

    def setAtrr(self, item):
        Parent.Atrr = item

    def getAtrr(self):
        print("This is atribute from parent class", Parent.Atrr)

class Child(Parent):
    def __init__(self):
        print("This is child class constructor")

    def child_Method(self):
        print("This METHOD is from child class")

obj = Child()
obj.setAtrr(120)
obj.getAtrr()

# data hiding 
class Datahiding:
    __secretresult = 0

    def secretcount(self):
        self.__secretresult +=1
        print(__secretreult)

obj = Datahiding()
obj.secretcount()