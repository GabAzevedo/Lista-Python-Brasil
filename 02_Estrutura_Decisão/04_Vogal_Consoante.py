#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input('Digite uma letra:'))
if letra.lower() in ['a','e','i','o','u']:
    print('Vogal') 
else: 
    print('Consoante')