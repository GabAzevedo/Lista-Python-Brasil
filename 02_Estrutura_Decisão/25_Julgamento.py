print('='*30)
print('INTERROGATÓRIO')
print('='*30)
A = str(input('Telefonou para a vítima?')).upper()
print(f'A resposta do interrogado referente a pergunta A foi: {A}')
B = str(input('Esteve no local do crime?')).upper()
print(f'A resposta do interrogado referente a pergunta A foi: {B}')
C = str(input('Mora perto da vítima?')).upper()
print(f'A resposta do interrogado referente a pergunta A foi: {C}')
D = str(input('Devia para a vítima?')).upper()
print(f'A resposta do interrogado referente a pergunta A foi: {D}')
E = str(input('Já trabalhou com a vítima?')).upper()
print(f'A resposta do interrogado referente a pergunta A foi: {E}')

julgamento = 0
if (A == 'SIM'):
    julgamento += 1
if (B == 'SIM'):
    julgamento += 1
if (C == 'SIM'):
    julgamento += 1
if (D == 'SIM'):
    julgamento += 1
if (E == 'SIM'):
    julgamento += 1

print(f'Ao responder o interrogatório foi confirmado {julgamento} respostas positivas a cerca do envolvimento.')

if julgamento == 2:
    print('Você é considerado SUSPEITO')
if julgamento == 3 and julgamento == 4:
    print('Você é considerado CÚMPLICE')
if julgamento == 5:
    print('Você é considerado ASSASSINO')
else:
    print('Você é considerado INOCENTE')



