quantidade = 0 
while (quantidade  <= 0):
    quantidade = int(input('Informe a quantidade de números desejada:'))
    if (quantidade <= 0):
        print('A quantidade deve ser um valor positivo, tente novamente:')

list_num = []    
soma = 0
for i in range (0, quantidade):  
    numero = int(input(f'Informe número:'))
    list_num.append(numero)
    soma += numero
maior = max(list_num)
menor = min(list_num)
print(f'Menor número é igual a {menor}')
print(f'Maior número é igual a {maior}')
print(f'A soma dos números é igual a {soma}')