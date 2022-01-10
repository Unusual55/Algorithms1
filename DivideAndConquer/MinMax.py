import math


def minmax(A: list, i, j):
    if j == i:
        return A[i], A[i]
    if j == i + 1:
        if A[i] < A[j]:
            return A[i], A[j]
        else:
            return A[j], A[i]
    else:
        k = math.floor((i + j) / 2)
        m1, M1 = minmax(A, i, k)
        m2, M2 = minmax(A, k + 1, j)
        return min(m1, m2), max(M1, M2)

if __name__ == '__main__':
    a = [20, -4, 23, -44, -15, 17, 5, -3, 18, 2, -31, 37, -47, 36, 35, -25, 44, 15, 4, 13, 30, -18, -46, -6, -40]
    a_min=min(a)
    a_max=max(a)
    print("Expedted Min: "  ,str(a_min))
    print("Expected Max: " ,str(a_max))
    ac_min, ac_max = minmax(a, 0, len(a)-1)
    print("Actural Min: " ,str(ac_min))
    print("Actual Max: " + str(ac_max))