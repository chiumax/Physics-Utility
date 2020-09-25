from math import *
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

import numbers

console = Console()

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
# "H2SO4".translate(SUB)

# function definitions
r = radians
d = degrees

g = -9.81

cosd = lambda x: cos(r(x))
sind = lambda x: sin(r(x))
tand = lambda x: tan(r(x))

atand = lambda x: d(atan(x))
acosd = lambda x: d(acos(x))
asind = lambda x: d(asin(x))

title = """\
Physics Utility v1.2
Made by ethan & max :)

REMEMBER to read the problem WORD by WORD
also, UNITS UNITS UNITS
convert them, too

Trig functions in Python use radians!
sind() = sin() in degrees
cosd() = cos() in degrees
tand() = tan() in degrees

asind() = inverse sin in degrees
acosd() = inverse cos in degrees
atand() = inverse tan in degrees
"_" = value of last expression

hypo(a, b) // a² + b² = c² - Solves hypotenuse
side(c, a) // c² - a² = b² - Solves side

quadratic(a, b, c) // quadratic equation

call `menu()` to see this again!
"""

panel = Panel(Text(title, justify="center"), border_style="green")
print(panel)
print("Physics Utility v1.0")
print("____________________")
print()


def menu():
    print(panel)


def isNumber(x):
    return isinstance(x, numbers.Number)


def hypo(a, b):
    title = """\

Hypotenuse Equation Solver
_________________________

This is what your equation looks like
      """
    print(title)
    ans = sqrt(pow(a, 2) + pow(b, 2))
    print(f"[white]{a}² + {b}² = {ans}²[/white]")
    return ans


def side(c, a):
    title = """\

Triangle Side Equation Solver
_________________________

This is what your equation looks like
      """
    print(title)
    ans = sqrt(pow(c, 2) - pow(a, 2))
    print(f"[white]{c}² - {a}² = {sqrt(pow(c,2)-pow(a,2))}²[/white]")
    return ans


def quadratic(a, b, c):
    title = """\

Quadratic Equation Solver
_________________________

This is what your equation looks like
      """
    print(title)
    print(f"[white]{a}x² + {b}x + {c} = 0[/white]")
    # discriminant
    d = pow(b, 2) - 4 * a * c

    if d < 0:
        print("This equation has no real solution")

    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    if d == 0:
        print("This equation has one solution")

    print()
    print(f"x = {x1}")
    print(f"x = {x2}")


# def oneD_solver(a=False, t=False, xi=0, xf=False, vi=0, vf=False):
#     if a==True:
#         #solve for a

#         if t!=False and vi!=False and vf!=False:
#             # vf = vi + at
#             return
#         elif xf!=False and vi != False and t != False:
#             # xf = vi * t + (1/2)*a*t^2
#             return
#         elif vf!=False and vi!=False and xf!=False:
#             # v^2=vi^2 + 2a*xf
#             return
#     elif t==True:
#         if a!= False and vi!= False and vf!= False:
#             # vf = vi +at
#             return
#         if xf!= False and vf!=False and vi!=False:
#             # xf = ((vf+vi)/2)t
#             return
#         if

#     elif xi==True:
#         #solve for xi
# # v^2=vi^2 + 2a*xf

#     elif xf == True:

#     elif vi == True:
#     elif vf == True:
#     return

# def list_utility():

# make sure that you do
# cos(r(45))
# d(acos(3/4)
