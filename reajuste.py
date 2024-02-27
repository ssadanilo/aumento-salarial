def calculo_reajuste(salario_atual, porc_reajuste):
    salario_novo = (salario_atual * porc_reajuste) / 100 + salario_atual
    return salario_novo

while True:
    pergunta = int(input('Digite 1 para calcular o reajuste, ou 2 para sair: '))
    if pergunta == 1:
        salario_atual = int(input('Digite o salário atual: '))
        porc_reajuste = int(input('Digite a porcentagem do reajuste: '))
        novo_salario = calculo_reajuste(salario_atual, porc_reajuste)
        print(f'O novo salário é de R${novo_salario} reais')
    elif pergunta == 2:
        print('Fim do programa')
        break