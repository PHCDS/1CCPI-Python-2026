nome_duplas = ["ana", "lara", "luiz", "caio"]

for i in range(len(nome_duplas)):
    for j in range(i + 1,len(nome_duplas)):
        print(nome_duplas[i], nome_duplas[j])
