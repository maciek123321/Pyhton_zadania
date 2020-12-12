import numpy as np

def add_matrix(x,y):
    z = []
    n = len(x)
    if ((len(x) != len(y)) and (len(x[0]) != len(y[0]))):
        return "Wrong dimensions"
    else:
        for i in range(n):
            z.append([])
            for j in range(n):
                z[i].append(x[i][j]+y[i][j])
        return z


if __name__ == '__main__':
    x = np.random.rand(128, 128)
    y = np.random.rand(128, 128)
    z = add_matrix(x, y)
    print(z)