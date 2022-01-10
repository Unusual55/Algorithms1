import math
from math import *


def main():
    x = 1237
    y = 3564
    b = 10
    m = 2
    ans = karasuba_algo(x, y, b, m)
    print(x*y)
    print(ans)


def karasuba_algo(x, y, b, m):
    bm = pow(b, m)

    if min(x, y) <= bm:
        return x * y

    x0 = (int)(x % bm)
    x1 = (int)(x / bm)
    y0 = (int)(y % bm)
    y1 = (int)(y / bm)

    A = karasuba_algo(x0, y0, b, m)
    B = karasuba_algo(x1, y1, b, m)
    C = karasuba_algo(x1 + x0, y1 + y0, b, m) - B - A
    ret = karasuba_algo(karasuba_algo(B, bm, b, m) + C, bm, b, m) + A
    return ret


if __name__ == "__main__":
    main()
