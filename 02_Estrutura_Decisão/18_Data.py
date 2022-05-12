#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = input('Informe uma data no formato dd/mm/yyyy:')

dia = (int(data[0:2]))
mes = (int(data[3:5]))
ano = (int(data[6:]))

print(f'A data informada foi {dia}/{mes}/{ano}') 

valida = True
if (mes in (1,3,5,7,8,10,12)):
    if (dia < 1) or (dia > 31):
        valida = False
elif(mes in (4,6,9,11)):
    if (dia < 1) or (dia > 30):
        valida = False
else:
    if (dia < 1) or (dia > 28):
        valida = False

if (valida):
    print('DATA VALIDA')
else:
    print('DATA INVALIDA')