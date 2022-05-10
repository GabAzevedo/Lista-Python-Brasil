#Faça um Programa que leia três números e mostre-os em ordem decrescente.
N1 = int(input('Primeiro:'))
N2 = int(input('Segundo:'))
N3 = int(input('Terceiro:'))
Lista = [N1,N2,N3]
print(f'Ordem Crescente = {sorted(Lista)}')

'''#RESOLUÇÃO 2 
Num1 = int(input('Primeiro:'))
Num2 = int(input('Segundo:'))
Num3 = int(input('Terceiro:'))

if (Num1 >= Num2) and (Num1 >= Num3):
    print (f'{Num1}')
    if Num2 >= Num3:
        print(f'{Num2}')
        print(f'{Num3}')
    else:
        print(f'{Num3}')
        print(f'{Num2}')

elif (Num2 >= Num3):
    print(f'{Num2}')
    if Num1 >= Num3:
        print(f'{Num1}')
        print(f'{Num3}')
    else:
        print(f'{Num3}')
        print(f'{Num1}')
else:
    print (f'{Num3}')
    if (Num1 >= Num2):
        print(f'{Num1}')
        print(f'{Num2}')
    else:
        print(f'{Num2}')
        print(f'{Num1}')'''