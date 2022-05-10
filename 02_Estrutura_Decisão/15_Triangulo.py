#Faça um Programa que peça os 3 lados de um triângulo. 
#O programa deverá informar se os valores podem ser um triângulo.
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os segmentos não formam um triângulo.')