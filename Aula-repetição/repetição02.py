def valeidar_nota(nota):
    while nota < 0 or nota > 10:
        print("a nota deve estar entre 0 a 10")
        nota = float(input("digite a nota novamente:"))
    return nota

nA = float(input('digite a primeira nota:'))
nA = valeidar_nota(nA)

nB = float(input("digite a segunda nota:"))
nB = valeidar_nota(nB)

media = (nA + nB) / 2
print(media)