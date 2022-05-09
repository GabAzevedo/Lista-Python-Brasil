#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = int(input('Digite o raio do quadrado:'))
area = lado**2
dobro = area*2
print(f'Sendo o lado do quadrado igual a {lado}, sua área será {area}')
print(f'O dobro da área apresentada é igual a {dobro}')
