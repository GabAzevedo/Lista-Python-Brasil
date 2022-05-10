# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:

N1 = float(input('Digite a primeira nota:'))
N2 = float(input('Digite a segunda nota:'))
media = (N1 + N2)/2
if media >= 7:
    print('Média maior ou igual a 7, você está APROVADO')
elif media == 10:
    print('Média 10, você está APROVADO COM DISTINÇÃO')
else:
    print('Média inferior a 7, você está REPROVADO.')