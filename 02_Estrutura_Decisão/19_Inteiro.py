#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
num = input('Informe um numero inteiro: ')

centenas = int(num[0:1])
dezenas = int(num[1:2])
unidades = int(num[2:])

saida = []
saida.append(str(centenas))
if (centenas > 1):
        saida.append('centenas,')
else:
        saida.append('centena,')

saida.append(str(dezenas)) 
if (dezenas > 1):
    saida.append('dezenas') 
else:
    saida.append('dezena')

    saida.append('e')

if (centenas != 0) or (dezenas != 0):    
    saida.append(str(unidades))
if (unidades > 1):
        saida.append('unidades')
else: 
    saida.append('unidade')  
    
print(f'O valor informado foi {" ".join(saida)}')


