from math import sqrt

def quadratic(a,b,c):
    delta = (b*b)-(4*a*c)
    if delta >= 0:
        x1 = ((-b-sqrt(delta))/(2*a))
        x2 = ((-b+sqrt(delta))/(2*a))
        return x1, x2
    else:
        return "No real roots"

if __name__ == '__main__':
    a = int(input("Insert a: "))
    b = int(input("Insert b: "))
    c = int(input("Insert c: "))
    print(quadratic(a, b, c))


