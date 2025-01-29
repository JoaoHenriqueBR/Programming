# Função para detectar tentativas de invasão em registros de log
def detectar_invasao(registros):
    # Variáveis para rastrear o ID do usuário atual e suas falhas consecutivas
    usuario_atual = usuario_anterior = None
    tentativas_consecutivas = 0
    invasor_detectado = None

    # Percorre cada registro de log:
    for registro in registros:
        usuario_atual, status = registro.split(":")

        # Verifica se o usuário atual é o mesmo da iteração anterior
        if usuario_atual == usuario_anterior:
            # Se o status é "falha", incremente o contador de tentativas falhas
            if status == "falha":
                tentativas_consecutivas += 1
            else:
                # Se a tentativa foi bem-sucedida, reseta o contador de falhas
                tentativas_consecutivas = 0
        else:
            # Se mudar de usuário, verifica se o usuário anterior teve mais de 3 falhas consecutivas
            if tentativas_consecutivas > 3:
                invasor_detectado = usuario_anterior
            else:
                # Atualiza para o novo usuário e reinicie a contagem de tentativas falhas
                usuario_anterior = usuario_atual
                # Se a nova tentativa for "falha", inicie a contagem em 1; caso contrário, inicie em 0
                tentativas_consecutivas = 1 if status == "falha" else 0  # Reseta contagem

    # Após o loop, verifica se o último usuário teve mais de 3 tentativas de falha
    if tentativas_consecutivas > 3:
      invasor_detectado = usuario_atual

    # Retorna o resultado final
    return invasor_detectado if invasor_detectado else "Nenhum invasor detectado"

def main():
    entrada = input("Log (Usuário:status, Usuário:status): ")

    registros = [registro.strip().strip('"') for registro in entrada.split(",")]

    resultado = detectar_invasao(registros)

    print(resultado)

if __name__ == "__main__":
    main()