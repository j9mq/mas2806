import numpy as np
import root_finding_methods as rm

# Initialise x array
x = np.linspace(
    -5,
    5,
    1000,
)

eps = 1e-10

p = np.roots(rm.p)


def method3(f, xd, xu, eps):

    while abs(xu - xd) > eps:

        xs = xu - (rm.f(xu) * ((xu - xd) / (rm.f(xu) - rm.f(xd))))

        if (rm.f(xu) * rm.f(xs)) > 0:
            xu = xs
        elif (rm.f(xd) * rm.f(xs)) > 0:
            xd = xs
        else:
            break

    return xs


m3 = method3(rm.f, 1.5, 2.0, eps)
print("Method 3 export = {}".format(m3))

r, n = rm.sec_roots(
    lambda x: x**5 - 2 * x**4 - 10 * x**3 + 18 * x**2 + 10 * x - 9,
    1.5,
    2.0,
    1e-10,
)

print("Root found at {} after {} iterations using Secant. \n".format(r,n))