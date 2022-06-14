num = int(input('Digite um número:'))
contador = 0
for c in range(1, num+1):
    if num % c == 0:
        contador +=1

print(f'O número {num} foi divisível {contador} vezes')

if contador == 2:
    print('PRIMO')
else:
    print('Não é primo')