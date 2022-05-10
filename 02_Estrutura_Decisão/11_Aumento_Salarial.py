#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento
salario = float(input('Digite seu salário:R$'))
if salario <= 280:
    aumento = (salario * 20)/100
    liquido = salario + aumento
    print(f'Seu salário antes do reajuste era de R${salario:.2f}')
    print(f'Seu salário salário foi aumentado em 20%')
    print(f'O valor do aumento foi de R${aumento:.2f}')
    print(f'O novo salário após o aumento é R${liquido:.2f}')
elif salario > 280 and salario < 700:
    aumento = (salario *15)/100
    liquido = salario + aumento
    print(f'Seu salário antes do reajuste era de R${salario:.2f}')
    print(f'Seu salário salário foi aumentado em 15%')
    print(f'O valor do aumento foi de R${aumento:.2f}')
    print(f'O novo salário após o aumento é R${liquido:.2f}')
elif salario > 700 and salario < 1500:
    aumento = (salario * 10)/100
    liquido = salario + aumento
    print(f'Seu salário antes do reajuste era de R${salario:.2f}')
    print(f'Seu salário salário foi aumentado em 10%')
    print(f'O valor do aumento foi de R${aumento:.2f}')
    print(f'O novo salário após o aumento é R${liquido:.2f}')
elif salario > 1500:
    aumento = (salario * 5)/100
    liquido = salario + aumento
    print(f'Seu salário antes do reajuste era de R${salario:.2f}')
    print(f'Seu salário salário foi aumentado em 5%')
    print(f'O valor do aumento foi de R${aumento:.2f}')
    print(f'O novo salário após o aumento é R${liquido:.2f}')
