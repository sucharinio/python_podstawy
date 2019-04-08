a = [1, 2, 3]  # definicja 3-elementowej listy
print(a)  # wyświetlenie listy

print(a[1])  # wyświetlenie wartości elementu listy o indeksie 1

a[1] = 'nowa wartość'  # nadpisanie 1 indeksu listy stringiem

# wydłużenie listy o nowy element (int 4)
# - wartość otrzymuje indeks "3"
a.append(4)
print(a)

# lista od 0 do 9
print(list(range(10)))

# różnica pomiędzy list a range
print(range(0, 10, 3))
print(list(range(0, 10, 3)))
