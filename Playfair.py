def genereaza_matrice(cheie):
    alfabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J este înlocuit cu I

    cheie = cheie.upper().replace("J", "I")
    matrice = []

    for litera in cheie:
        if litera not in matrice and litera in alfabet:
            matrice.append(litera)

    for litera in alfabet:
        if litera not in matrice:
            matrice.append(litera)

    return [matrice[i:i + 5] for i in range(0, 25, 5)]


def pozitie(matrice, caracter):
    for i in range(5):
        for j in range(5):
            if matrice[i][j] == caracter:
                return i, j


def pregateste_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")

    rezultat = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]

            if a == b:
                rezultat += a + "X"
                i += 1
            else:
                rezultat += a + b
                i += 2
        else:
            rezultat += a + "X"
            i += 1

    return rezultat


def cripteaza_playfair(text, cheie):
    matrice = genereaza_matrice(cheie)
    text = pregateste_text(text)

    criptat = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]

        r1, c1 = pozitie(matrice, a)
        r2, c2 = pozitie(matrice, b)

        if r1 == r2:
            criptat += matrice[r1][(c1 + 1) % 5]
            criptat += matrice[r2][(c2 + 1) % 5]

        elif c1 == c2:
            criptat += matrice[(r1 + 1) % 5][c1]
            criptat += matrice[(r2 + 1) % 5][c2]

        else:
            criptat += matrice[r1][c2]
            criptat += matrice[r2][c1]

    return criptat


def decripteaza_playfair(text, cheie):
    matrice = genereaza_matrice(cheie)

    decriptat = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]

        r1, c1 = pozitie(matrice, a)
        r2, c2 = pozitie(matrice, b)

        if r1 == r2:
            decriptat += matrice[r1][(c1 - 1) % 5]
            decriptat += matrice[r2][(c2 - 1) % 5]

        elif c1 == c2:
            decriptat += matrice[(r1 - 1) % 5][c1]
            decriptat += matrice[(r2 - 1) % 5][c2]

        else:
            decriptat += matrice[r1][c2]
            decriptat += matrice[r2][c1]

    return decriptat


cheie = input("Cheie: ")
mesaj = input("Mesaj: ")

criptat = cripteaza_playfair(mesaj, cheie)
print("Criptat:", criptat)

decriptat = decripteaza_playfair(criptat, cheie)
print("Decriptat:", decriptat)