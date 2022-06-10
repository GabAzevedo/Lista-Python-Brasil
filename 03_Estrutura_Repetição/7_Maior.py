maior = menor = 0
for c in range (1,6):
    num = int(input(f'{c}º Número:'))
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'O maior número informado foi {maior}')
print(f'O menor número informado foi {menor}')