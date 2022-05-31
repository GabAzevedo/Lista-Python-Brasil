#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
numb = -1
while (numb < 0) or (numb > 10):
    numb = int(input('Informe um número de 0 a 10:')) 
    if (numb <0) or (numb > 10):
        print('Valor incorreto, Por favor informe um número de 0 a 10')
    
print(f'Você informou o número {numb}')
    
