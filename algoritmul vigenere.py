ALFABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"


def pregateste_text(text):
    return text.upper().replace(" ", "")


def extinde_cheia(text, cheia):
    cheia = cheia.upper()
    rezultat = ""

    for i in range(len(text)):
        rezultat += cheia[i % len(cheia)]

    return rezultat


def criptare_vigenere(text, cheia):
    text = pregateste_text(text)
    cheia_extinsa = extinde_cheia(text, cheia)

    rezultat = ""

    for i in range(len(text)):
        m = ALFABET.index(text[i])
        k = ALFABET.index(cheia_extinsa[i])

        rezultat += ALFABET[(m + k) % len(ALFABET)]

    return rezultat


def decriptare_vigenere(text, cheia):
    cheia_extinsa = extinde_cheia(text, cheia)

    rezultat = ""

    for i in range(len(text)):
        c = ALFABET.index(text[i])
        k = ALFABET.index(cheia_extinsa[i])

        rezultat += ALFABET[(c - k) % len(ALFABET)]

    return rezultat


cheie = input("Cheie: ")
mesaj = input("Mesaj: ")

criptat = criptare_vigenere(mesaj, cheie)
print("Criptat:", criptat)

decriptat = decriptare_vigenere(criptat, cheie)
print("Decriptat:", decriptat)