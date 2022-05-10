#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
'''Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E'''

N1 = float(input('Nota 1:'))
N2 = float(input('Nota 2:'))
media = (N1 + N2)/2
print(f'Sua média foi de {media}')

if media == 0 or media < 4: 
    print('Conceito E')
    
elif media == 4 or media < 6:
    print ('Conceito D')
    
elif media == 6 or media < 7.5:
    print('Conceito C')
    
elif media == 7.5 or media < 9:
    print('Conceito B')
    
elif media == 9 or media < 10:
    print('Conceito A')

else:
    print('Valor inválido')
