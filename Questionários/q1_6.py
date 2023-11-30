# Introdução - Questão 6
def confere_tempo(n: float):
    if n - int(n) == 0:
        return n
    elif n - int(n) <= 0.5:
        return int(n) + 1
    else:
        return round(n, 0)


total_bytes = int(input())
taxas = list()

while sum(taxas) < total_bytes:
    taxa = int(input())
    taxas.append(taxa)

print(f"Transmitindo {total_bytes} bytes...")

taxas_temporarias = []
for taxa in taxas:
    if len(taxas_temporarias) == 5:
        if sum(taxas_temporarias) == 0:
            print("Tempo restante: pendente...")
        else:

            velocidade = sum(taxas_temporarias) / 5
            total_bytes -= sum(taxas_temporarias)


            resolve_imprecisao = round(total_bytes / velocidade, 3)
            tempo_restante = confere_tempo(resolve_imprecisao)
            print(f"Tempo restante: {int(tempo_restante)} segundos.")

        taxas_temporarias = []
        taxas_temporarias.append(taxa)
    else:
        taxas_temporarias.append(taxa)

tempo_total = len(taxas)
print(f"Tempo total: {tempo_total} segundos.")
