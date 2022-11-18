import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import root_finding_methods as rm

# Initialise x array
x0 = np.linspace(
    -5,
    5,
    1000,
)

# Root finding of g(x)
g_coef = [
    1,
    -3,
    -10,
    4,
    1,
]
p = np.roots(g_coef)

colors = [
    "orange",
    "blue",
    "purple",
    "green",
]

eps = 1e-10


def secant_graph():
    """Function to plot a graph using the secant method of root finding"""

    u = 0
    a = []

    while u <= len(x0) - 1:  # To stay in bound for axis 0 with size 399
        r, n = rm.sec_roots(
            rm.g,
            x0[u],
            x0[u] + 1,
            eps,
        )
        a.append(n)

        # Drawing individual lines with distinguished colours
        if abs(r - p[0]) <= eps:
            plt.vlines(
                x0[u],
                ymin=0,
                ymax=n,
                colors=colors[0],
            )
        elif abs(r - p[1]) <= eps:
            plt.vlines(
                x0[u],
                ymin=0,
                ymax=n,
                colors=colors[1],
            )
        elif abs(r - p[2]) <= eps:
            plt.vlines(
                x0[u],
                ymin=0,
                ymax=n,
                colors=colors[2],
            )
        elif abs(r - p[3]) <= eps:
            plt.vlines(
                x0[u],
                ymin=0,
                ymax=n,
                colors=colors[3],
            )
        else:
            break

        u += 1

    return a


# Change the figure size and y limits
fig = plt.figure(figsize=[10, 4])
plt.ylim([0, 30])

# Axis labelling
plt.xlabel("Starting guess, $x_0$")
plt.ylabel("Number of iterations, n")
plt.title("$g(x)$ root convergence using Secant method")

# Visual clarity
plt.rcParams.update({"font.size": 14})
plt.tight_layout()
plt.grid()

# Figure DPI
mpl.rcParams["figure.dpi"] = 300

# Plot
plt.plot(
    x0,
    secant_graph(),
    alpha=0,
)
plt.savefig(
    "secant_graph.png",
)

plt.show()
