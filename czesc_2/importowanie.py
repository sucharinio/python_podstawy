# przykładowe użycie modułu csv.
# Dane w pliku oddzielone są spacją, natomiast znak '|' oznacza początek/koniec
# nieinterpretowalnego ciągu znaków (coś jak string)
import csv
with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print('row ', row)
        print(', '.join(row))
