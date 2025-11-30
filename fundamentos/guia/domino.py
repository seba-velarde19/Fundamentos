def encaja(a, b):
    encaja = False
    for num in range(len(a)):
        for numero in b:
            if a[num] == numero:
                encaja = True
    return encaja


print(encaja([2, 3], [3, 7]))
