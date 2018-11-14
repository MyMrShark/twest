def palindrom(word1):

    litery = list(word1)
    palindromq = True

    for litera in litery:
        if litera == litery[-1]:
            litery.pop(-1)
        else:
            palindromq = False
            break

    return palindromq


word = input("Podaj słowo: ")
palindrom1 = word.find(word[::-1])
if palindrom1 == 0:
    print(True)
else:
    print(False)
