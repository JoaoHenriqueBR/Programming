# Entrada do usuário
email = input('Email: ').strip()

# Verifique as regras do e-mail:
def valida_email(e_mail):
    if ' ' not in e_mail:
        if '@gmail.com' in e_mail or '@outlook.com' in e_mail:
            if e_mail[0] != '@' and e_mail[-1] != '@':
                return 'E-mail válido'
        
    return 'E-mail inválido'

print(valida_email(email))

