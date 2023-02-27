import math

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def isqrt(x):
   math.sqrt(x)

def log(x, y):
    return math.log(x, y)
  
def power(x, y):
    if y<0:
      raise ValueError('0 cannot be raised to a negative power')
    else:
      return x ** y
      return x ** y

def percent(x, y):
       return (x / y) * 100
       return (x / y) * 100

def Acircle(x):
  pi = 3.14159
  return pi * (x ** 2)

def nth_root(x, y):
    answer = x**(1/y)
    return answer

def Atriangle(x, y):
  return (x*y)/2

def end():
   print("Thanks for using this calculator")
   exit(0)

def combine1(x,y,z,a):
  return (x + y) - (z + a)

def combine2(x,y,z,a):
  return (x + y) * (z + a)

def combine3(x,y,z,a):
  return (x + y) / (z + a)