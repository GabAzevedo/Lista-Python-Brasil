# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# A velocidade de um link de Internet (em Mbps)
# Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
mb = int(input('Informe o tamanho do arquivo em MB:'))
velocidade = int(input('Informe a velocidade de sua internet em Mbps:'))
tempo = (mb / (velocidade/8))/60

print(f'Para efetuar o download de {mb} MB com a velocidade de {velocidade} Mbps, irá demorar {tempo:.0f} minutos')
