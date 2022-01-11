import random
from random import randint


def split(arr: list):
    left, right = [], []
    size = int(len(arr) / 2)
    for i in range(size):
        left.append(arr[i])
    for i in range(size, len(arr)):
        right.append(arr[i])
    return left.sort(reversed=False), right.sort(reversed=False)


def median(arr: list):
    left, right = split(arr)
    m1, m2 = median(left), median(right)
    if m1 == m2:
        return m1
    blue = []
    leftcut = int(len(left) / 3)
    rightcut = int(len(right) * (2 / 3))
    for i in range(leftcut, len(left)):
        blue.append(left[i])
    for i in range(rightcut):
        blue.append(right[i])
    if m1 < m2:
        m = median(blue)
        return m
    else:
        m = median(blue)
        return m


def select_random_pivot(arr: list, nth: int):
    k = random.randint(0, len(arr) - 1)
    s1 = [x for x in arr if arr[x] < arr[k]]
    s2 = [x for x in arr if arr[x] > arr[k]]

    # if the length of the first partition is nth-1, the last number is the number we wanted
    if len(s1) == nth - 1:
        return k

    # if the size of the first partition is bigger than than nth-1, the nth number is inside this partition
    elif len(s1) > nth - 1:
        select_random_pivot(s1, nth)

    # the nth number is inside the second partition
    else:
        select_random_pivot(s2, nth - len(s1) - 1)


def select_good_pivot(arr: list, nth: int):
    if len(arr) < 50:
        arr.sort(reversed=False)
        return arr[nth]
    k = choose_good_pivot(arr)
    s1 = [x for x in arr if arr[x] < arr[k]]
    s2 = [x for x in arr if arr[x] > arr[k]]

    # if the length of the first partition is nth-1, the last number is the number we wanted
    if len(s1) == nth - 1:
        return k

    # if the size of the first partition is bigger than than nth-1, the nth number is inside this partition
    elif len(s1) > nth - 1:
        select_good_pivot(s1, nth)

    # the nth number is inside the second partition
    else:
        select_good_pivot(s2, nth - len(s1) - 1)


def choose_good_pivot(arr: list):
    matrix = []
    medians = []
    for i in range(len(arr) / 5):
        row = []
        for j in range(5):
            row.append(arr[5 * i + j])
        row.sort(reversed=False)
        matrix.append(row)
        medians.append(medians(arr))
    return select_good_pivot(medians, len(arr) / 10)
