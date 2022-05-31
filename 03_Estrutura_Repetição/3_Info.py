#Validação Nome
name = ''
while (len(name) <= 3 ):
    name = str(input('Digite um nome:'))
    if (len(name) <= 3):
        print('Nome incorreto, Informe um nome maior que 3 caracteres')

#Validação Idade
idade = -1
while (idade < 0) or (idade > 150):
    idade = int(input('Digite sua idade:'))
    if (idade < 0) or (idade >150):
        print('Idade incorreta, Idade autorizada de 0 a 150 anos')

#Validação Salário
salario = 0
while (salario <= 0):
    salario = float(input('Digite seu salário:'))
    if salario < 0:
        print('Valor incorreto, defina um valor maior que 0')

#Validação Sexo
sexo = ''
while (sexo != 'F') and (sexo != 'M'):
    sexo = str(input('Informe seu sexo:')).strip().upper()[0]
    if (sexo != 'F') and (sexo != 'M'):
        print('Valor informado não encontrado, favor informar F para Feminino ou M para Masculino')

#Validação Estado Civil
estado_civil = ''
while estado_civil not in ('S','C','V','D'):
    estado_civil = str(input('Informe seu estado civil:')).strip().upper()[0]
    if estado_civil not in ('S','C','V','D'):
        print('Estado civil incorreto, tente novamente')
    