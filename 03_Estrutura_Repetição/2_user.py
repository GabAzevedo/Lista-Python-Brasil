#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
user = ''
password = ''
while user == password:
    user = str(input('Login:')).upper()
    password = str(input('Senha:')).upper()
    if (user != password):
        print('Login e Senha registrados com sucesso.')
        break
    else:
        print('ERRO! Não é permitido que a senha seja igual a login, Tente novamente.')
    