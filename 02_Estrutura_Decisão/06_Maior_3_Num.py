#Faça um Programa que leia três números e mostre o maior deles.
N1 = int(input('Informe o primeiro número:'))
N2 = int(input('Informe o segundo número:'))
N3 = int(input('Informe o terceiro número:'))
max = max(N1,N2,N3)
if (N1 == N2) and (N1 == N3):
    print('Os números são iguais') 
else:
    print(f'Dentre os números {N1}, {N2} e {N3} o maior deles é o {max}')

                #RESOLUÇÃO 2 
'''Num1 = int(input('Informe o primeiro número:'))
Num2 = int(input('Informe o segundo número:'))
Num3 = int(input('Informe o terceiro número:'))

if (Num1 == Num2) and (Num1 == Num3):
    print('Os números são iguais')

elif (Num1>Num2) and (Num1 > Num3):
    print(f'{Num1} é o maior número')

elif (Num2 > Num1) and (Num2 > Num3):
    print(f'{Num2} é o maior número')

else:
    print(f'{Num3} é o maior número')'''