def calcular_media(notas):
    if len(notas) == 0:
        return 0 
    total = sum(notas)
    return total / len(notas)

def verificar_situacao(media):
    if media < 7:
        return "Reprovado"
    elif media == 10:
        return "Parabéns, sua média é 10"
    else:
        return "Aprovado"

notas = []
while True:
    nota = input("Digite a nota do aluno (ou 's' para sair): ")
    if nota.lower() == 's':
        break
    try:
        nota = float(nota)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

media = calcular_media(notas)
situacao = verificar_situacao(media)

print(f"A média do aluno é {media:.2f}")
print(f"Situação: {situacao}")