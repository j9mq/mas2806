import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import root_finding_methods as rm

# Initialise x array for axis purposes
x = np.linspace(-5, 5, 1000)

# Initialise variables for scatter markers
markers = np.zeros(
    5,
)
colors = [
    "orange",
    "blue",
    "purple",
    "green",
    "yellow",
]

# Finding roots of f(x)
p = np.roots(rm.p)

# Setting y axis to -100 <= y <= 100 and adjusting figure size
fig = plt.figure(figsize=[10, 4])
plt.ylim(
    [
        -100,
        100,
    ]
)

# Line plot
plt.plot(x, rm.f(x))

# Scatter plot
plt.scatter(
    p,
    markers,
    c=colors,
    marker="o",
    s=500,
    zorder=3,
)

# Axis labelling
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title(
    "Newton-Raphson convergence for f(x) = $x^5 - 2x^4 - 10x^3 + 18x^2 + 10x - 9$"
)

# Visual clarity
plt.rcParams.update({"font.size": 13})
plt.tight_layout()
plt.grid()

# Figure DPI
mpl.rcParams["figure.dpi"] = 300

plt.savefig(
    "root_graph.png",
)
plt.show()
