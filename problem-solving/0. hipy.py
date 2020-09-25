import math

def quadratic(a,b,c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2

while True:
    # pay attention here
    # because the data type of varialbes are unkown
    # therefore, we shouldn't noly write input()
    # we should code like "int(input)"
    
    a = int(input("plz input a:"))
    b = int(input("plz input b:"))
    c = int(input("plz input c:"))
    print(quadratic(a,b,c))


