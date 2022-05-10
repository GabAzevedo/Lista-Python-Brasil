#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar.
#Sabendo que a decisão é sempre pelo mais barato.
P1 = int(input('Preço do primeiro produto:R$'))
P2 = int(input('Preço do segundo produto:R$'))
P3 = int(input('Preço do terceiro produto:R$'))
min = min(P1,P2,P3)
if (P1 == P2) and (P1 == P3):
    print('Após avaliação foi determinado que todos os produtos tem o mesmo preço.') 
else:
    print(f'Avaliando os valores informados, o produto recomendado é o de valor R${min:.2f}')
