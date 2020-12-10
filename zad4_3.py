def Scalar_mul(x, y):
    if len(x) == len(y):
        z=[]
        for i in range(len(x)):
            z.append(x[i]*y[i])
        return sum(z)
    else:
        return "error"

x = [2, 9, 2, 999]
y = [4, 7, 5, 1]

print(Scalar_mul(x, y))