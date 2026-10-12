# Alfabetul românesc - 31 caractere
ALFABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"

def valideaza_text(text):
    for ch in text:
        if ch != " " and ch.upper() not in ALFABET:
            return False
    return True

def pregateste_text(text):
    return text.replace(" ", "").upper()

def extinde_cheia(text, cheia):
    cheia = cheia.upper()
    cheie_extinsa = ""

    for i in range(len(text)):
        cheie_extinsa += cheia[i % len(cheia)]

    return cheie_extinsa

def criptare_vigenere(text, cheia):
    text = pregateste_text(text)
    cheia_extinsa = extinde_cheia(text, cheia)

    criptograma = ""

    for i in range(len(text)):
        m = ALFABET.index(text[i])
        k = ALFABET.index(cheia_extinsa[i])

        c = (m + k) % len(ALFABET)

        criptograma += ALFABET[c]

    return criptograma

def decriptare_vigenere(text, cheia):
    cheia_extinsa = extinde_cheia(text, cheia)

    mesaj = ""

    for i in range(len(text)):
        c = ALFABET.index(text[i])
        k = ALFABET.index(cheia_extinsa[i])

        m = (c - k) % len(ALFABET)

        mesaj += ALFABET[m]

    return mesaj

def main():
    print("===== CIFRUL VIGENERE =====")

    operatie = input("Alege operatia (criptare/decriptare): ").lower()

    cheia = input("Introdu cheia: ")

    if len(cheia) < 7:
        print("Eroare! Lungimea cheii trebuie sa fie minim 7 caractere.")
        return

    if not valideaza_text(cheia):
        print("Cheia contine caractere nepermise!")
        return

    text = input("Introdu mesajul: ")

    if not valideaza_text(text):
        print("Sunt permise doar literele alfabetului roman.")
        return

    if operatie == "criptare":
        rezultat = criptare_vigenere(text, cheia)
        print("Criptograma:", rezultat)

    elif operatie == "decriptare":
        rezultat = decriptare_vigenere(
            pregateste_text(text),
            cheia
        )
        print("Mesaj decriptat:", rezultat)

    else:
        print("Operatie invalida!")

if __name__ == "__main__":
    main()