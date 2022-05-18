print('[A] - Álcool = R$ 1,90')
print('[G] - Gasolina = R$ 2,50')
opção = str(input('Das opções acima, com qual combustível deseja abastecer?')).upper()


if opção == 'A':
    print(f'O combustível selecionado foi A - Álcool')
    quantidade = float(input(f'Quantos litros do combustível {opção} o senhor deseja?'))
    if quantidade <= 20:
        print('O desconto para o consumo de até 20L de Álcool é igual a 3% por litro')
        desconto = (((1.9 * quantidade)* 3)/100) 
        tot = (1.9 * quantidade)- desconto
        print(f'Você gastaria R${(1.9 * quantidade):.2f}, mas com o desconto passará a gastar R${tot:.2f}')
    else:
        print('O desconto para o consumo acima de 20L de Álcool é igual a 5% por litro')
        desconto = (((1.9 * quantidade)* 5)/100)
        tot = (1.9*quantidade)- desconto
        print(f'Você gastaria R${(1.9*quantidade)}, mas com o desconto passará a gastar R${tot}')
elif opção == 'G':
    print(f'O combustível selecionado foi G - Gasolina')
    quantidade = float(input(f'Quantos litros do combustível {opção} o senhor deseja?'))
    if quantidade <= 20:
        print('O desconto para o consumo de até 20L de Gasolina é igual a 4% por litro')
        desconto = (((2.5*quantidade)*4)/100)
        tot = (2.5*quantidade) - desconto
        print(f'Você gastaria R${(2.5*quantidade)}, mas com o desconto passará a gastar R${tot}')
    else:
        print(f'O desconto para o consumo acima de 20L de Gasolina é igual a 6% por litro')
        desconto = (((2.5 * quantidade)*6)/100)
        tot = (2.5*quantidade) - desconto
        print(f'Você gastaria R${(2.5*quantidade)}, mas com o desconto passará a gastar R${tot}')
else:
    print('Opção inválida, tente novamente')
