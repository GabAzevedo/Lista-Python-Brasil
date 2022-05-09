#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho = float(input('Digite seu ganho por hora:'))
horas = int(input('Quantas horas você trabalha no mês?'))
salário = ganho * horas
print(f'SeU salário este mês será R${salário:.2f}')