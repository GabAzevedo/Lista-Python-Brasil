#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
num = input('Informe um numero inteiro: ')

centenas = int(num[0:1])
dezenas = int(num[1:2])
unidades = int(num[2:])

saida = ' '
if (centenas > 0):
    saida = saida + str(centenas)
    if (centenas > 1):
        saida = saida + ('centenas')
    else:
        saida = saida + ('centena')

if (dezenas > 0):
    if (unidades == 0) and (centenas != 0):
        saida = saida + (',')
        saida = saida + str(dezenas)
    if (dezenas > 1):
        saida = saida + ('dezenas') 
    else:
        saida = saida + ('dezena')

if (unidades > 0):
    if (centenas != 0) or (dezenas != 0):
        saida = saida + ('e')
        saida = saida + str(unidades)
    if (unidades > 1):
        saida = saida + ('unidades')
    else: 
        saida = saida + ('unidade')  
    
print(f'O valor informado foi {" ".join(saida)}')


