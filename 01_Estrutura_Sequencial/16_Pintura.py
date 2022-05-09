#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#A tinta é vendida em latas de 18 litros, que custam R$ 80,00.]
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math
tamanho = float(input('Tamanho da área em m²:'))
litro = tamanho/3
latas = math.ceil(litro/18)
valor = latas * 80

print(f'Para pintar a área de {tamanho} m² será necessário {latas} latas e irá custar R${valor:.2f}')
