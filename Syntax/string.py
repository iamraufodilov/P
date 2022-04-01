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
