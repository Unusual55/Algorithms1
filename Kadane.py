def kadane(numbers: list):
    max_current, max_global = numbers[0], numbers[0]
    for i in range(len(numbers)):
        max_current = max(numbers[i], max_current + numbers[i])
        if max_current > max_global:
            max_global = max_current
    return max_global


def main():
    # A = [-2, 3, 2, -1]
    # print(kadane(A))
    B = [-3, -4, 5, -1, 2, -4, 6, -1]
    print(kadane(B))

if __name__ == '__main__':
    main()
