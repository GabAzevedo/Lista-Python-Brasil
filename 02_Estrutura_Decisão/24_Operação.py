#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
'''A -par ou ímpar;
B- positivo ou negativo;
C- inteiro ou decimal.'''
n1 = float(input('Primeiro termo:'))
n2 = float(input('Segundo termo:'))
soma = n1 + n2 
print('[1] = PAR ou ÍMPAR?')
print('[2] = POSITIVO ou NEGATIVO?')
print('[3] = INTEIRO ou DECIMAL')
print(f'O valor da soma é igual a {soma}')
opção = input('De acordo com as oções acima, qual informação deseja saber?')
if opção == '1':
    if soma % 2 == 0:
        print(F'{soma} é PAR!')
    else:
        print(f'{soma} é IMPAR')
elif opção == '2':
    if soma > 0:
        print(f'{soma} é POSITIVO')
    elif soma == 0:
        print(f'{soma} é NEUTRO')
    else: 
        print(f'{soma} é NEGATIVO')
else:
    if (soma == int(soma)):
        print(f'{soma} é INTEIRO')
    else:
        print(f'{soma} é DECIMAL')
