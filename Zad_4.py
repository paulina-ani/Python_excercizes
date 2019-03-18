# Zad_4
# Napisz program wypisujący twoje BMI na podstawie podanych danych.
imie = input('Podaj jak masz na imię: ')
print(f'Dzień dobry {imie}')
masa = float(input('Podaj swoją wagę w kg: '))
wzrost = float(input('Podaj swój wzrost w cm: '))
bmi = masa/(wzrost/100)**2;

if bmi < 18.5:
    print(f'Twoje BMI wynosi: {bmi:.2f}. Masz niedowagę')
elif 18.6 <= bmi < 25:
    print(f'Twoje BMI wynosi: {bmi:.2f}. Twoja waga jest prawdidłowa')
else:
    print(f'Twoje BMI wynosi: {bmi:.2f}. Masz nadwagę')
