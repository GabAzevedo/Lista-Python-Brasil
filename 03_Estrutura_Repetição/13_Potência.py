base = int(input('Informe a base:'))
expoente = 0
while (expoente <= 0):
    expoente = int(input('Informe o valor do expoente:'))
    if expoente <= 0:
        print('O expoente deve ser positivo')

potencia = 1
for i in range(1, expoente + 1):
    potencia *= base

print (f'O valor da base {base} elevado ao expoente {expoente} é igual a {potencia}')