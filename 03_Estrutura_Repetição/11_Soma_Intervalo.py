inicio = int(input('Informe o número inicial:'))
fim = inicio
while (fim <= inicio):
    fim = int(input('Informe o número final:'))    
    if (fim <= inicio):
        print('O valor final deve ser maior que o valor inicial')
cont = soma = 0
for i in range (inicio, fim, +1):
    print(i, end=" ")
    cont += 1
    soma += i
print(f'\nDentro do intervalo de {inicio} a {fim} contabilizamos {cont} valores') 
print(f'A soma deles é igual a {soma}')
