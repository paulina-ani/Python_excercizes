# Zad_3
# Napisz program obliczający koszty przyjazdu z miasta A do miasta B na podstawie podanej przez użytkownika liczby kilometrów, ceny paliwa oraz spalania. Zapytaj użytkownika także o nazwy miejscowości.

a = input('Podaj nazwę pierwszej miejscowości: ')
b = input('Podaj nazwę drugiej miejscowości: ')
c = float(input('Podaj dystans pomiędzy miejscowościami(km): '))
d = float(input('Podaj cenę paliwa za 1 litr (zł): '))
e = float(input('Podaj jakie spalanie ma twój samochód (litr/100km):'))

wynik = c*d*e/100

print(f'Pierwsza miejscowość: {a}')
print(f'Drugia miejscowość: {b}')
print(f'Dystans pomiędzy miejscowościa mi wynosi: {wynik:.2f}')