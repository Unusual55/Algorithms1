def coin_change(coin_set: list, num: int):
    coin_set.sort(reverse=True)
    curr, i = 0, 0
    while num > 0:
        curr += int(num / coin_set[i])
        diff = int(num / coin_set[i])
        num -= diff * coin_set[i]
        i += 1
    return curr


if __name__ == '__main__':
    coin_set = [1, 2, 5, 10]
    print(coin_change(coin_set, 38))
