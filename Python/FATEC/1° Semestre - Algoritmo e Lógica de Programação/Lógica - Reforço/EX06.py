# Verificar na empresa o salário do funcionário e se ele tem dependentes. 
# Se o funcionário tiver dependentes, 
# entre com o número de dependentes e calcule o salario família, 
# recalcule o salario e reemita o salário do funcionário. 
# Para funcionários que não tem dependentes nenhum aumento será efetuado 
# e emitir a mensagem que o salário não terá reajuste. 
# Verifique se o usuário deseja continuar o cálculo. 
# Se não quiser continuar encerre o programa, caso contrário continue o processamento.

x = 1
while x == 1:
    salario = float(input('Digite seu salário: '))
    dependente = int(input('Possui dependente? (1 - SIM; 0 - NÃO): '))
    if dependente == 1:
        d = int(input(('Quantos: ')))
        s = salario + (d*(salario/10))
        print('Seu novo salário será de: {:.2f}'.format(s))
    elif dependente == 0:
        print('O salário não terá reajuste')
    else:
        print('Escolha inválida, tente novamente!\n')
    x = int(input('Deseja continuar? (1 - SIM; 0 - NÃO):'))

