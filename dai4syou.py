f(x) = x * 2

result = f(2)


def f(x):
    return x * 2


result = f(2)
print(result)


def f(x):
    return x + 1


z = f(4)

if z == 5
    print("z is 5")
else:
    print("z is not 5")


def f():
    result = f()
    print(result)

def f(x,y,z):
    return x + y + z

result = f(1,2,3)
print(result)

def f():
    z = 1 + 1

result = f()
print(result)

len("Monty")

len("Python")

str(100)

int("1")

float(100)


int("110")
int(20.54)
float("16.4")
float(99)

int("Prince")

age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("you are young!")
else:
    print("Wow,you are old")


def even_old(x):
    if x % 2 == 0:
        print("偶数")
    else:
        print("奇数")

even_odd(2)
even_odd(3)

n = input("type a number:")
n = int(n)
if n % 2 ==0:
    print("n is even.")
else:
    print("n is odd")

n = input("type a number:")
n = int(n)
if n % 2 ==0:
    print("n is even.")
else:
    print("n is odd")


n = input("type a number:")
n = int(n)
if n % 2 ==0:
    print("n is even.")
else:
    print("n is odd")


def even_odd():
    n = input("type number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even.)
    else:
        print("n is odd.")

    even_odd()
    even_odd()
    even_odd()

def f(x==2):
    return x ** x

print(f())
print(f(4)

def add_it(x,y=10)):
    return x + y

result = add_it(2))
print(result)

X = 1
y = 2
z = 3

def f():

    X = 1
    y = 2
    z = 3

    print(x)
    print(y)
    print(z)

f()

if x > 100:
    print("x is > 100")


x = 100

def f():
    global x
    x += 1
    print(x)
f()

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
print(a / b)

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
print(a / b)


a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZerodivisionError:
    print("b cannot be zero")


try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    try:
        print(a / b)
    except (ZerodivisionError,ValueError):
        print("Invalid input")

try:
    10 / 0
    c = "I will never get defined."
except ZeroDivisionError:
    print(c)

def add(x, y):
    """
    Returns x + y.
    :param x: int.
    :param y: int.
    :return: int sum of x and y.
    """
    return x + y

x = 100
print(x)

print(100)