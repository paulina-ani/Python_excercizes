# Zad_7
# Napisz program, który na podstawie wprowadzonych wymiarów obliczy, objętość podanego opakowania i sprawdzi czy jest ona większa od 1 litra
import math
print('Wybierz odpowiedni kształt opakowania: ')
print('1. Sześcian')
print('2. Walec')
print('3. Kula')
print('4. Prostopadłościan')
print('5. Graniastosłup')
print('6. Stożek')
print('7. Ostrosłup')

x = float(input('Podaj numer: '))
if x == 1:
    print('Podaj wymiary sześcianu:')
    a = float(input('a = '))
    V = a**3;
    print(f'Objętość sześcianu wynosi: {V:.2f}')
elif x == 2:
    print('Podaj wymiary walca:')
    r = float(input('r = '))
    h = float(input('h = '))
    V = h*math.pi*r**2;
    print(f'Objętość walca wynosi: {V:.2f}')
elif x == 3:
    print('Podaj wymiary kuli:')
    r = float(input('r = '))
    h = float(input('h = '))
    V = (4/3)*math.pi*r**2;
    print(f'Objętość kuli wynosi: {V:.2f}')
elif x == 4:
    print('Podaj wymiary prostopadłościanu:')
    a = float(input('a = '))
    b = float(input('b = '))
    h = float(input('h = '))
    V = a*b*h
    print(f'Objętość prostopadłościanu wynosi: {V:.2f}')
elif x == 5:
    print('Podaj wymiary graniastosłupa:')
    pp = float(input('pp = '))
    h = float(input('h = '))
    V = pp*h
    print(f'Objętość graniastosłupa wynosi: {V:.2f}')
elif x == 6:
    print('Podaj wymiary stożka:')
    r = float(input('r = '))
    h = float(input('h = '))
    V = (1/3)*math.pi*r**2
    print(f'Objętość stożka wynosi: {V:.2f}')
elif x == 7:
    print('Podaj wymiary ostrosłupa:')
    pp = float(input('pp = '))
    h = float(input('h = '))
    V = 1/3*pp*h
    print(f'Objętość ostrosłupa wynosi: {V:.2f}')
else:
    print('Wybrałeś niewłaściwy numer')
