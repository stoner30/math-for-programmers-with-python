from tools.vectors import *
from tools.draw3d import *
from tools.colors import *

# 练习3.3
print(add((4, 0, 3), (-1, 0, 1)))

draw3d(
    Arrow3D((4, 0, 3), color=red),
    Arrow3D((-1, 0, 1), color=blue),
    Arrow3D((3, 0, 4), (4, 0, 3), color=blue),
    Arrow3D((-1, 0, 1), (3, 0, 4), color=red),
    Arrow3D((3, 0, 4), color=purple)
)

# 练习3.5
from math import sin, cos, pi

vs = [(sin(pi * t / 6), cos(pi * t / 6), 1.0 / 3) for t in range(0, 24)]
running_sum = (0, 0, 0)
arrows = []
for v in vs:
    next_sum = add(running_sum, v)
    arrows.append(Arrow3D(next_sum, running_sum))
    running_sum = next_sum
print(running_sum)
draw3d(*arrows)

# 练习3.7
u, v = (1, -1, -1), (0, 0, 2)
draw3d(
    Points3D(u, color=blue),
    Points3D(v, color=red),
    Points3D(add(u, scale(0.5, subtract(v, u))), color=purple)
)
