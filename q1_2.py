# Introdução - Questão 2
def frequencia(text: str):
    analyse = text
    frequency = dict()
    amounts = set()

    for char in text:
        if char in analyse:
            count = analyse.count(char)
            frequency[char] = count
            amounts.add(count)
            analyse = analyse.replace(char, "")

    if amounts:
        greatest_index = max(list(amounts))
    else:
        return ""

    for k, v in frequency.items():
        if v == greatest_index:
            return k
