nome_duplas = ["ana", "lara", "luiz", "caio"]

duplas = []

for i in range(len(nome_duplas)):
    for j in range(i + 1 ,len(nome_duplas)):
        if i != j:
            duplas.append((nome_duplas[i], nome_duplas[j]))

for dupla in duplas:
    print(dupla)