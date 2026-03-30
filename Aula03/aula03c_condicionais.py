#estrutura condicional simples

nota = 7.0

if nota < 6:
    print("reprovado")

print("FIM")

#estrutura condicional composta

nota_final = 7.0

if nota_final <6:
    print("reprovado")
else:
    print("aprovado")

print("FIM")

#estrutura condicional encadeada

nota_final = 7.0

if nota_final <4:
    print("reprovado")
else:
    if nota_final <6:
        print("recuperação")
    else:
         print("aprovado")


print("FIM")

#estrutura condicional encadeada v2


nota_final = 7.0

if nota_final < 4:
    print("reprovado")
elif nota_final < 6:
    print("recuperação")
else:
    print("aprovado")

print("FIM")
