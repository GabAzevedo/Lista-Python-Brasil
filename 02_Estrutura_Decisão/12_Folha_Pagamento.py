#Faça um programa para o cálculo de uma folha de pagamento
#Sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
#3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto
#Mas não é descontado (é a empresa que deposita).Desconto do IR:
'''Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%'''

#Salário Bruto
ganho = int(input('Ganho por hora:'))
hora = int(input('Horas trabalhadas:'))
salario = ganho * hora
print(f'Seu salário é de R${salario:.2f}')

#Descontos por salário
print('='*30)
if salario <= 900:
    INSS = (salario * 10)/100
    sindicato = (salario *3)/100
    FGTS = (salario*11)/100
    TotDesconto = INSS + sindicato
    Liquido = salario - TotDesconto
    print(f'Salário bruto = R${salario:.2f}')   
    print(f'Descontos = R${TotDesconto}')
    print(f'FGTS = R${FGTS}')
    print(f'Salário Líquido = R${Liquido:.2f}')

elif salario <= 1500:
    INSS = (salario * 10)/100
    IR = (salario*5)/100
    sindicato = (salario *3)/100
    FGTS = (salario*11)/100
    TotDesconto = INSS + sindicato + IR
    Liquido = salario - TotDesconto
    print(f'Salário bruto = R${salario:.2f}')   
    print(f'Descontos = R${TotDesconto}')
    print(f'FGTS = R${FGTS}')
    print(f'Salário Líquido = R${Liquido:.2f}')

elif salario <= 2500:
    INSS = (salario * 10)/100
    IR = (salario/10)/100
    sindicato = (salario *3)/100
    FGTS = (salario*11)/100
    TotDesconto = INSS + sindicato + IR
    Liquido = salario - TotDesconto
    print(f'Salário bruto = R${salario:.2f}')   
    print(f'Descontos = R${TotDesconto}')
    print(f'FGTS = R${FGTS}')
    print(f'Salário Líquido = R${Liquido:.2f}')

elif salario > 2500:
    INSS = (salario * 10)/100
    IR = (salario/20)/100
    sindicato = (salario *3)/100
    FGTS = (salario*11)/100
    TotDesconto = INSS + sindicato + IR
    Liquido = salario - TotDesconto
    print(f'Salário bruto = R${salario:.2f}')   
    print(f'Descontos = R${TotDesconto:.2f}')
    print(f'FGTS = R${FGTS:.2f}')
    print(f'Salário Líquido = R${Liquido:.2f}')