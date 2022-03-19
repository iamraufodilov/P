#variable can be overwritten
a=12
a=13
print(a)
# declare vriable type with function
b=str(1)
print(b)
print(type(b))
c=float(1)
print(c)
print(type(c))
c=12
print(c)
print(type(c))
#variable name
name = 12
#assign multi variables
x,y,z=12,13,14
print('\n',x,'\n',y,'\n',z)
#multi variable to one walue
x=y=z=7
print('\n',x,'\n',y,'\n',z)
#unpack collection
footballer = ['Messi', 'Ronaldo', 'Dembele']
x,y,z = footballer
print('\n',x,'\n',y,'\n',z)
#output mulivariable in print
x,y,z=10,11,12
print(x,y,z)
#use + to output multivaiable
x,y,z="I ","love ","Python"
print(x+y+z)
#out two type variable
x,y ="One", 1
print(x,y)
#global variables
x = "I AM FROMGLOBAL BITCH"
def my_function():
    print("This word from Global", x)
my_function()
#global and local
x = "I am global"
def my_function():
    x = "I am local"
    print("Our variable is: ", x)
my_function()
print("What we will see:", x)
#global keyword
def my_function():
    global x
    x = "Now finally I am also Global"
    print(x)
my_function()
print("What we will see: ", x)
#to change gloobal wariable inside function
x = "Global best"
def my_function():
    global x
    x = "Local best"
    print(x)
my_function()
print("What we will see: ", x)
