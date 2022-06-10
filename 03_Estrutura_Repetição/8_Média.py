cont = soma = media = 0

for c in range(1,6):
    num = int(input(f'{c}º Número:'))
    cont = cont + 1
    soma += num
    media= soma/5
print(f'Dos valores {cont} informados, a soma total dos valores é igual a {soma}')
print(f'A média dos valores informados é igual a {media}')
