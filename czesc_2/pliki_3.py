sciezka = "tekst2.txt"

with open(sciezka, 'w') as plik:
    print(plik.tell())

    plik.write("\nMoja kolejna linijka")
