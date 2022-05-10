#Faça um Programa que leia três números e mostre o maior e o menor deles.
N1 = int(input('Informe o primeiro número:'))
N2 = int(input('Informe o segundo número:'))
N3 = int(input('Informe o terceiro número:'))
max = max(N1,N2,N3)
min = min(N1,N2,N3)
print(f'Dentre os números {N1}, {N2} e {N3} o maior deles é o {max} e o menor é {min}')
