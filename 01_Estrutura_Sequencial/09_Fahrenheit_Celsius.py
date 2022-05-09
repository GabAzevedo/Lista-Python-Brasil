#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
F = int(input('Digite a temperatura em Fahrenheit:'))
C = 5*((F-32)/9)
print(f'A temperatura em Celsius é igual a {C:.2f}')
