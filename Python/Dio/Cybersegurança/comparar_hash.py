def verificar_hashes(lista_hashes):
    for hash_comparacao in lista_hashes:
        hash_calculado, hash_esperado = hash_comparacao.split(",")

        if hash_calculado.strip() == hash_esperado.strip():
            print("Correto")
        else:
            print("Inválido")

lista_hashes = [
    "abc123, abc123",  # Esperado: "Correto"
    "abc123, def456",  # Esperado: "Inválido"
    "xyz789, xyz789",  # Esperado: "Correto"
]

verificar_hashes(lista_hashes)