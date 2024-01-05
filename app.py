# Inicializa variáveis
soma = 0
quantidade_numeros = 0

# Loop para ler números até que o usuário digite 0
while True:
    # Solicita ao usuário um número inteiro
    numero = int(input("Digite um número inteiro (digite 0 para encerrar): "))

    # Verifica se o usuário digitou 0 para encerrar o loop
    if numero == 0:
        break

    # Atualiza a soma e a quantidade de números
    soma += numero
    quantidade_numeros += 1

# Verifica se foram digitados números antes de calcular a média
if quantidade_numeros > 0:
    # Calcula a média aritmética
    media = soma / quantidade_numeros

    # Exibe os resultados
    print(f"\nQuantidade de números digitados: {quantidade_numeros}")
    print(f"Soma dos números: {soma}")
    print(f"Média aritmética dos números: {media:.2f}")
else:
    print("Nenhum número foi digitado.")
