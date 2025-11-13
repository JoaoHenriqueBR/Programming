try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Valor inválido!')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except KeyboardInterrupt:
    print('Programa encerrado!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
