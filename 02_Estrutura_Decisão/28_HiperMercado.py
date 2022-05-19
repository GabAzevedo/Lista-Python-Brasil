print ('[FD] - Filé Duplo _____ PREÇO R$5,80')
print('[A] - Alcatra _____ PREÇO R$ 6,80 ')
print('[P] - Picanha _____ PREÇO R$ 6,90')
opção = str(input('Sua escolha para opção de Carne é:')).upper()

if opção == 'FD':
    print(f'A opção escolhida foi: Filé Duplo')
    quantidade = float(input('Informe a quantidade (KG) desejada:'))
    if quantidade >= 5:
        preço = 5.8 * quantidade
        desconto = (preço * 5)/100
        total = preço - desconto
        print(f'O preço para {quantidade:.2f}KG de {opção} foi de R${preço:.2f}')
        print(f'Com desconto de 5% o valor total é igual a R$ {total:.2f}')
    else:
        preço = 4.9 * quantidade
        desconto = (preço * 5)/100
        total = preço - desconto
        print(f'O preço para {quantidade:.2f}KG de {opção} foi de R${preço:.2f}')
        print(f'Com desconto de 5% o valor total é igual a R$ {total:.2f}')
elif opção == 'A':
    print(f'A opção escolhida foi: Alcatra')
    quantidade = float(input('Informe a quantidade (KG) desejada:'))
    if quantidade >= 5:
        preço = 6.8 * quantidade
        desconto = (preço * 5)/100
        total = preço - desconto
        print(f'O preço para {quantidade:.2f}KG de {opção} foi de R${preço:.2f}')
        print(f'Com desconto de 5% o valor total é igual a R$ {total:.2f}')
    else:
        preço = 5.9 * quantidade
        desconto = (preço * 5)/100
        total = preço - desconto
        print(f'O preço para {quantidade:.2f}KG de {opção} foi de R${preço:.2f}')
        print(f'Com desconto de 5% o valor total é igual a R$ {total:.2f}')
else:
    print('A opção escolhida foi: Picanha')
    quantidade = float(input('Informe a quantidade (KG) desejada:'))
    if quantidade >= 5:
        preço = 7.8 * quantidade
        desconto = (preço*5)/100
        total = preço - desconto
        print(f'O preço para {quantidade:.2f}KG de {opção} foi de R${preço:.2f}')
        print(f'Com desconto de 5% o valor total é igual a R${total:.2f}')
    else:
        preço = 6.9 * quantidade
        desconto = (preço*5)/100
        total = preço - desconto
        print(f'O preço para {quantidade:.2f}KG de {opção} foi de R${preço:.2f}')
        print(f'Com desconto de 5% o valor total é igual a R${total:.2f}')
        