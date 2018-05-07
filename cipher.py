L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def dekripsi():
    key = int(input("kunci: "))
    cipherText = str(input("Dekripsi\t: "))

    plaintext2 = ""
    for c in cipherText.upper():
        if c.isalpha():
            plaintext2 += I2L[(L2I[c] - key)%26]
        else:
            plaintext2 += c
    print("PlainText\t: ", plaintext2)

def enkripsi():
    key = int(input("kunci: "))
    plainText = str(input("PlainText\t: "))

    cipherText = ""
    for c in plainText.upper():
        if c.isalpha():
            cipherText += I2L[(L2I[c] + key)%26]
        else:
            cipherText += c
    print("enkripsi\t:",cipherText)
def p():
    print('''
1. Enkripsi
2. Dekripsi
    ''')

def main():
    try:
        def inicio():
            while True:
                p()
                kat1 = int(input(">>> "))
                if kat1 == 1:
                    enkripsi()
                elif kat1 == 2:
                    dekripsi()

                kat2 = str(input("lanjutkan [Y,n]: "))
                if (kat2 == "Y" or kat2 == "y"):
                    inicio()
        inicio()
    except Exception as e:
        raise


if __name__ == "__main__":
    main()
