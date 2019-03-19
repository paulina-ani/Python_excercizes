#Zad_6
#Napisz program sprawdzający czy podana przez użytkownika liczba jest:
#a) jest liczbą 11
#b) lub jest podzielna przez 3, większa od 14 i nieparzysta

a = float(input('Podaj liczbę: '))
b = a == 11
c = a%3 == 0 and a%2 == 1 and a > 10
print('Czy liczba jest parzysta, podzielna przez 3 i większa od 10?')
if c == True:
    print('Tak')
elif b == True:
    print('Nie, ale jej wartość wynosi 11')
else:
    print('Nie, liczba nie spełnia wymagań')

