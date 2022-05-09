#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
'''a- Para homens: (72.7*h) - 58
b- Para mulheres: (62.1*h) - 44.7'''
from re import M


sexo = str(input('Qual é o seu sexo? [M/F]'))
altura = float(input('Qual é a sua altura? [em metros]'))
peso = float(input('Qual é o seu peso? [em kg]' ))

if sexo == 'M':
    ideal = (72.7*altura)-58

else:
    ideal = (62.1*altura-44.7)

if peso > ideal:
    print(f'Seu peso é {peso}, seu peso ideal é {ideal:.2f}. Você está acima do seu peso ideal.')

elif peso < ideal:
    print(f'Seu peso é {peso}, seu peso ideal é {ideal:.2f}. Você está abaixo do seu peso ideal.')

else:
    print(f'Seu peso é {peso}, seu peso ideal é {ideal:.2f}. Você está no seu peso ideal')