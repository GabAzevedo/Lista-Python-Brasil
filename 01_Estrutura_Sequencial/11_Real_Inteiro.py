#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
'''a. O produto do dobro do primeiro com metade do segundo .
b- A soma do triplo do primeiro com o terceiro.
c- O terceiro elevado ao cubo.'''
n1 = int(input('Número 1:'))
n2 = int(input('Número 2:'))
n3 = float (input('Número 3:'))
a = ((n1*2) * (n2/2))
b = ((n1*3)+ (n3*3))
c = (n3**3)
print(f'O produto do dobro do primeiro número com metade do segundo número é igual a {a}')
print(f'A soma do triplo do primeiro número com o terceiro número é igual a {b}')
print(f'O terceiro número elevado ao cubo é igual a {c}')
