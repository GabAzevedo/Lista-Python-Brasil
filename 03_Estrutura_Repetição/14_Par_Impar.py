print('Informe 10 números:')
pares = 0
ímpares = 0 
for i in range(1,11):
    numero = int(input(f'Informe o {i}º número:'))
    if (numero % 2 == 0):
        pares += 1
    else:
        ímpares += 1
print(f'A quantidade de números pares foi igual a {pares}')
print(f'A quantidade de números ímpares foi igual a {ímpares}')