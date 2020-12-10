from numpy import random
n = 50
x = random.randint(100, size=(n))

def Bubble_sort(y):
    for i in range(n-1):
        for j in range(n - i - 1):
            if y[j] < y[j + 1]:
                y[j], y[j + 1] = y[j + 1], y[j]
    return y

def Verify(x,y):
    for i in range(n-1):
        if x[n-1] == y[n-1]:
            return True
        else:
            return False

a = sorted(x, reverse=True)
b = Bubble_sort(x)
print(Verify(a,b))