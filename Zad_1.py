# Zad. 1.
# Napisz program do obliczania: pole trójkąta, pola koła, pola trapezu oraz objetości kuli.
import math
#Pole trójkąta
a=float(input('Wpisz wielkośc podstawy trójkąta: a='))
h=float(input('Wpisz wysokość trójkąta: h='))
p = (1/2)*a*h
print('Pole trójkąta o podstawie a=',a ,' i wysokości h=',h ,' wynosi: ', p)
print()
#Pole koła
r=float(input('Podaj promień koła: r='))
p=math.pi*r**2
print('Pole koła o promieniu r=',r ,' wynosi: ', p)
print()
#Pole trapezu
a=float(input('Podaj długość podstawy: a='))
b=float(input('Podaj długość podstawy: b='))
h=float(input('Podaj wysokość: h='))
p=(a+b)*h/2
print('Pole trapezu o długości podstaw a=', a, ' i b=', b,' oraz wysokości h=',h ,' wynosi: ',p)
print()
#Objętość kuli
R=float(input('Podaj promień kuli: R='))
V = 4/3*math.pi*R**3
print('Objętość kuli o promieniu R=',R ,' wynosi ',V)
