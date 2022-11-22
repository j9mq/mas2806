import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import root_finding_methods as rm

# Initialise x array
x = np.linspace(
    -5,
    5,
    1000,
)

# Root finding of f(x)
p = np.roots(rm.p)

colors = [
    "orange",
    "blue",
    "purple",
    "green",
    "yellow",
]

eps = 1e-10


def new_raph_graph():
    """Function to plot a graph using Newton's of root finding"""

    u = 0
    a = []

    while u <= len(x) - 1:  # To stay in bound for axis 0 with size n-1
        r, n = rm.newraph(
            rm.f,
            rm.dfdx,
            x[u],
            eps,
        )
        a.append(n)

        # Drawing individual lines with distinguished colours
        if abs(r - p[0]) <= eps:
            plt.vlines(
                x[u],
                ymin=0,
                ymax=n,
                colors=colors[0],
            )
        elif abs(r - p[1]) <= eps:
            plt.vlines(
                x[u],
                ymin=0,
                ymax=n,
                colors=colors[1],
            )
        elif abs(r - p[2]) <= eps:
            plt.vlines(
                x[u],
                ymin=0,
                ymax=n,
                colors=colors[2],
            )
        elif abs(r - p[3]) <= eps:
            plt.vlines(
                x[u],
                ymin=0,
                ymax=n,
                colors=colors[3],
            )
        elif abs(r - p[4]) <= eps:
            plt.vlines(
                x[u],
                ymin=0,
                ymax=n,
                colors=colors[4],
            )
        else:
            break

        u += 1

    return a


# Change the figure size and y limits
fig = plt.figure(figsize=[12, 4])
plt.ylim([0, 35])

# Axis labelling
plt.xlabel("Starting guess, $x_0$")
plt.ylabel("Number of iterations, n")
plt.title("$f(x)$ root convergence using Newton-Raphson method")

# Visual clarity
plt.rcParams.update({"font.size": 14})
plt.tight_layout()
plt.grid()

# Figure DPI
mpl.rcParams["figure.dpi"] = 300

# Plot
plt.plot(
    x,
    new_raph_graph(),
    alpha=0,
)
plt.savefig(
    "newton_graph.png",
)

plt.show()
