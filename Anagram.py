def anagram():
    global words1
    global words2
    if len(word1) != len(word2):
        return False

    if len(word1) == len(word2):
        words1 = sorted(word1)
        words2 = sorted(word2)

    if words1 == words2:
        return True
    else:
        return False


word1 = input("Podaj pierwsze słowo: ")
word2 = input("Podaj drugie słowo: ")

print(anagram())
