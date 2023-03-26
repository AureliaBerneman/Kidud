import math
from scipy.optimize import minimize_scalar

BITS = 24


def func(x):
    return abs(x - (math.sqrt(1+2*BITS) / 2))


def main():
    x = minimize_scalar(func).x
    small = math.floor(x)
    big = math.ceil(x)
    maximum = min([func(small), func(big)])
    if maximum == func(small):
        print("\u03B1 = ", small)
    if maximum == func(big):
        print("\u03B1 = ", big)


if __name__ == "__main__":
    main()
