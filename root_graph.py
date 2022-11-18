import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import root_finding_methods as rm

# Initialise x array for axis purposes
x = np.linspace(-5, 5, 1000)

# Initialise variables for scatter markers
markers = np.zeros(4,)
colors = [
    "orange",
    "blue",
    "purple",
    "green",
]

# Finding roots of g(x)
g_coef = [
    1,
    -3,
    -10,
    4,
    1,
]
p = np.roots(g_coef)

# Setting y axis to -100 <= y <= 100 and adjusting figure size
fig = plt.figure(figsize=[10, 4])
plt.ylim(
    [
        -100,
        100,
    ]
)

# Line plot
plt.plot(x, rm.g(x))

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
plt.ylabel("$g(x)$")
plt.title("Newton-Raphson convergence for g(x) = $x^4 - 3x^3 - 10x^2 + 4x + 1$")

# Visual clarity
plt.rcParams.update({"font.size": 14})
plt.tight_layout()
plt.grid()

# Figure DPI
mpl.rcParams["figure.dpi"] = 300

plt.savefig(
    "root_graph.png",
)
plt.show()
