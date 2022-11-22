import numpy as np

""" Defined values """

# Coefficients of each element of f(x)
p = [
    1,
    -2,
    -10,
    18,
    10,
    -9,
]

# Find roots of f(x)
r = np.roots(p)

x = np.linspace(-5, 5, 1000)
eps = 1e-10


def f(x):
    return x**5 - 2 * x**4 - 10 * x**3 + 18 * x**2 + 10 * x - 9


def dfdx(x):
    "Derivative of f(x)"
    return 5 * x**4 - 8 * x**3 - 30 * x**2 + 36 * x + 10


""" Newton-Rapson Method """


def newraph(f, dfdx, x0, eps):

    x = x0
    n = 0

    while abs(f(x)) > eps:
        x = x - (f(x) / dfdx(x))
        n += 1
    return x, n


""" Secant method """


def sec_roots(f, x0, x1, eps):

    # Initialise an array of our starting guesses
    x = [x0, x1]
    iterations = 0
    a = 2

    while abs(f(x[a - 1])) > eps:
        x_tmp = x[a - 1] - (
            f(x[a - 1]) * (x[a - 1] - x[a - 2]) / (f(x[a - 1]) - f(x[a - 2]))
        )

        # Adds the next value to the array
        x.append(x_tmp)

        # Increase iteration counter and onto next value in the sequence
        iterations += 1
        a += 1

    lastvalue = len(x) - 1

    return (
        x[lastvalue],
        iterations,
    )


#%%

import root_finding_methods as rm

x_0 = 1
eps = 1e-10

r, n = rm.newraph(
    lambda x: x**5 - 2 * x**4 - 10 * x**3 + 18 * x**2 + 10 * x - 9,
    lambda x: 5 * x**4 - 8 * x**3 - 30 * x**2 + 36 * x + 10,
    1.5,
    1e-10,
)

# print("Root found at {} after {} iterations using Newton Raphson. \n".format(r,n))

r, n = rm.sec_roots(
    lambda x: x**5 - 2 * x**4 - 10 * x**3 + 18 * x**2 + 10 * x - 9,
    1.3,
    1.7,
    1e-10,
)

# print("Root found at {} after {} iterations using Secant. \n".format(r,n))
