#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
#Deve pagar uma multa de R$ 4,00 por quilo excedente. 
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Quantos kg foram pescados?'))
limite = (peso - 50)
if limite > 0:
    valor = limite*4 
    print(f'Você pescou {peso}KG, ultrapassando {limite}KG do limite de 50KG estabelecido pelo regulamento')
    print(f'O valor da multa é 4 reais o kg ultrapassado, a multa é de R${valor:.2f}')
else: 
    print('Limite de peso foi respeitado!')