inicio = int(input('Informe o número inicial:'))
fim = inicio
while (fim <= inicio):
    fim = int(input('Informe o número final'))    
    if (fim <= inicio):
        print('O valor final deve ser maior que o valor inicial')

for i in range (inicio, fim, +1):
    print (i, end=' ')