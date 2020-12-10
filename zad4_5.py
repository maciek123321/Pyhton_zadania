import numpy as np

def mul_matrix(x, y):
    n = len(x)
    z = []
    for i in range(n):
        z.append([])
        for j in range(n):
            a = 0
            for r in range(n):
                a += x[i][r] * y[r][j]
            z[i].append(a)

    return z

x = np.random.rand(8, 8)
y = np.random.rand(8, 8)
z = mul_matrix(x, y)
print(z)


