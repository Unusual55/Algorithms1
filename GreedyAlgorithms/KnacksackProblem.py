def fractional(inputs: list, capacity: int):
    inputs.sort(key=lambda x: x[1], reverse=True)

    value = 0

    for j in range(len(inputs)):
        wj, vj = inputs[j][0], inputs[j][1]
        if wj < capacity:
            print(str(wj) + " killos of item " + str(j) + " were taken")
            capacity = capacity - wj
            value += vj
        else:
            frac = wj / capacity
            value += vj * frac
            print(str(int(frac)) + " killos of item " + str(j) + " were taken")
            capacity = int(capacity - (wj * frac))
            break

    return value


def integer(inputs: list, capacity: int):
    inputs.sort(key=lambda x: x[1], reverse=True)
    value = 0
    for j in range(len(inputs)):
        wj, vj = inputs[j][0], inputs[j][1]
        if wj <= capacity:
            capacity -= wj
            print(str(wj) + " killos of item " + str(j) + " were taken")
            value += vj

    return value

if __name__ == '__main__':
    w = [10, 40, 20, 30]
    v = [60, 40, 100, 120]
    c = 50
    inputs = []
    for i in range(len(w)):
        t = (w[i], v[i])
        inputs.append(t)
    # print(fractional(inputs, c))
    print(integer(inputs, 50))
