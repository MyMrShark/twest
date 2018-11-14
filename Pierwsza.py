def liczby(li):
    if li <= 1:
        return False
    if li == 2:
        return True
    for i in range(li):
        if i == 0 or i == 1:
            continue
        elif li % i == 0:
            return False
        else:
            return True


n = int(input("Podaj liczbe: "))
print(liczby(n))
