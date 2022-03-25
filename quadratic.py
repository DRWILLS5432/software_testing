# import math
from math import sqrt


def find_roots(a, b, c):
    d = b * b - 4 * a * c

    if a == 0:
        return None

    if d > 0:
        x1 = (((-b) + sqrt(d)) / (2 * a))
        x2 = (((-b) - sqrt(d)) / (2 * a))
        return x1, x2

    elif d == 0:
        x = -b / (2 * a)
        return x

    else:
        return "NO ROOTS"

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print(find_roots(a, b, c))
