def sumadzielnikow(n):
    suma = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            suma += i
    return suma


def doskonala(n):
    return sumadzielnikow(n) == n


def doskonala1000():
    lista = [n for n in range(1, 10000) if doskonala(n)]
    return lista


print(doskonala1000())
a = int(input("Podaj liczbę: "))
if a in doskonala1000():
    print(True)
else:
    print(False)
