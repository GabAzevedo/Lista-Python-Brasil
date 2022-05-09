#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a- Salário bruto.
#b- Quanto pagou ao INSS.
#c- Quanto pagou ao sindicato.
#d- O salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
ganho = float(input('Quanto você ganha por hora trabalhada:'))
hora = int(input('Quantas horas você trabalhou este mês:'))
salário = ganho * hora

print ('='*30)
IR = (salário*0.11)
INSS = (salário*0.08)
Sindicato = (salário*0.05)
Líquido = salário - IR - INSS - Sindicato
print(f'Salário Bruto: R${salário:.2f}')
print(f'IR(11%): R${IR:.2f}')
print(f'INSS(8%): R${INSS:.2f}')
print(f'Sindicato(5%): R${Sindicato:.2f}')
print(f'Seu salário líquido é igual a R${Líquido:.2f}')
print('='*30)
