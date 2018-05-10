import random
from math import sqrt
from numpy import matrix


def evalPoly(coeffs, x):
    ans = 0
    for i in range(len(coeffs)):
        ans = ans + coeffs[i] * x ** i
    return ans


def printPoly(coeffs):
    polyString = ""
    for i, c in enumerate(coeffs):
        if i == 0:
            polyString += str(c)
        else:
            if c != 0:
                if c > 0:
                    polyString += " +"
                else:
                    polyString += " "
                polyString += str(c)+" * x"
                if i > 1:
                    polyString += "^"+str(i)
    return polyString


def getPartial(coeffs, index, function, x):
    h = .001
    d = [0]*len(index)
    for i in index:
        coeffs[i] += h
        d[i] = function(coeffs, x)
        coeffs[i] -= 2*h
        d[i] -= function(coeffs, x)
        coeffs[i] += h
        d[i] = d[i] / (2 * h)
    return d


def getGrad(coeffs, function, x):
    return getPartial(coeffs, range(len(coeffs)), function, x)


def errorFunction(coeffs, X, Y):
    error = 0
    for index, x in enumerate(X):
        error += (Y[index] - evalPoly(coeffs, x))**2
    return error


def magnitude(v):
    return sqrt(sum([e**2 for e in v]))


# degree of regression
n = 1
c = [random.randint(-10, 10) for r in range(n+1)]
true_coeffs = [1, -1, 1, 5, -3, 7, 2]
X = [i for i in range(10)]
y = [0] * len(X)
for i in range(len(X)):
    y[i] = evalPoly(true_coeffs, X[i]) + random.normalvariate(0, 1)
delta = .001
stepSize = 1
while stepSize > .00001:
    g = getGrad(c, lambda coeffs, x: errorFunction(coeffs, x, y), X)

    c[0] -= g[0]*delta
    c[1] -= g[1]*delta
    stepSize = delta*magnitude(g)

e = errorFunction(c, X, y)
print("Numerical:")
print(printPoly(c))


# linear regressions can be calculated exactly
if len(c) == 2:
    A = matrix([1]*len(X)+X)
    A = A.reshape(len(c), len(X)).T
    B = (A.T*A).I*A.T*matrix(y).T
    B = B.reshape(1, len(c))
    print("Exact:")
    print(printPoly(B.tolist()[0]))
