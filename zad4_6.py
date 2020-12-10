import sys
import numpy as np
if sys.version_info >= (3,):
    xrange = range

def det(M):
    M = [ list(row) for row in M ]
    n = len(M)
    res = 1.0
    if len(M) != len(M[0]):
        return "Wrong dimensions"
    else:
        for j in xrange(n-1, 0, -1):
            pivot, i = max((abs(M[k][j]), k) for k in xrange(j+1))
            pivot = M[i][j]
            if pivot == 0.0:
                return 0.0
            M[i], M[j] = M[j], M[i]
            if i != j:
                res = -res
            res *= pivot
            fact = -1.0/pivot
            for i in xrange(j):
                f = fact * M[i][j]
                for k in xrange(j):
                    M[i][k] += f * M[j][k]
        res *= M[0][0]
    return res


x = np.random.rand(2, 2)
print(x)
print(det(x))