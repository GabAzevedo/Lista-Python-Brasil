TotMaçã = int(input('KG de Maçãs comprados:'))
TotMorango = int(input('KG de Morangos comprada:'))

if TotMaçã > 5:
    valorMaçã = TotMaçã*2.2
else:
    valorMaçã = TotMaçã*2.5

if TotMorango > 5:
    valorMorango = TotMorango * 1.5
else:
    valorMorango = TotMorango * 1.8

TotCompras = valorMorango + valorMaçã

if (TotMaçã + TotMorango) >= 8:
    print(f'Contabilizamos a compra de {TotMaçã + TotMorango}KG de fruta. Na compra de 8KG de frutas, você ganha um desconto de 10%')
    desconto = (TotCompras * 10)/100
    total = TotCompras - desconto
    print(f'O valor da sua compra foi R${TotCompras:.2f}, com desconto o novo valor será R${total:.2f}')
elif TotCompras > 25:
    print('Contabilizamos o valor de R${TotCompras:2.f}. Sendo o valor da compra de frutas superior a R$25,00 você ganhou um desconto de 10%')
    desconto = (TotCompras * 10)/100
    total = TotCompras - desconto
    print(f'O valor da sua compra foi R${TotCompras:.2f}, com desconto o novo valor será R${total:.2f}')
else:
    print(f'O valor da compra foi R${TotCompras:.2f}')
    
