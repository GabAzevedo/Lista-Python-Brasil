# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# A cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros. 
# Custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
'''
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

import math
area = float(input('Quantos m² deseja pintar?'))

litros = (area/6) * 1.1
latas = math.ceil(litros/18)
galão = math.ceil(litros/3.6)
valor_lata = latas * 80
valor_galão = galão * 25

mixlatas = round(litros/18)
mixgaloes = round((litros - mixlatas * 18)/3.6)

if ((litros - (mixlatas *18) % 3.6 != 0)):
    mixgaloes += 1
    total_mix = (mixlatas *80) + (mixgaloes * 25)

print(f'Para pintar {area} m², será necessário {latas} lata(s) de tinta e irá custar R${valor_lata} ')
print(f'Para pintar {area} m², será necessário {galão} galão(ões) de tinta e irá custar R${valor_galão:.2f}')
print(f'Se desejar mesclar latas e galões para dar oque precisa realmente, será necessário {mixlatas} lata(s)'
f' e {mixgaloes} galão(ões) e irá custar R${total_mix:.2f}')