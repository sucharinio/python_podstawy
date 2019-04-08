class Cos: # nagłówek klasy
    def __init__(self, var): # konstruktor
        self.cecha1 = var  # definiowanie atrybutu klasy

    def pokaz(self):  # metoda
        print(f'cecha1: {self.cecha1}')


a = Cos('wartosc')  # zainicjowanie klasy
print(a)
print('wartosc cechy:', a.cecha1)
#  wywołanie metody bez () zwraca obiekt definicji metody
print('metoda: ', a.pokaz)
a.pokaz()
# możliwe jest usunięcie dowolnego obiektu w dowolnym momencie
# (także atrybutu klasy) a działanie poza interfejsem klasy
# może wpłynąć na jej działanie w nieprzewidywalny sposób
# del a.cecha1
# print('po usunieciu', a.pokaz())
a.cecha1 = 'b'
print('po zmianie')
a.pokaz()