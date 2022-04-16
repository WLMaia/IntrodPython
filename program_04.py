codProduto=int(input("Informe o código do produto:"))
codProdutoStr=str(codProduto)
dvtesta=int(codProdutoStr[5])
somaImpar=somaPar=i=0
for i in range(5):
        if i % 2:
           somaPar = somaPar + int(codProdutoStr[i])
        else:
            somaImpar = somaImpar + int(codProdutoStr[i])
print("Soma impar:",somaImpar, "- Soma par:", somaPar)
dv = ((somaImpar*3)+somaPar) % 10
if dv == 0:
    print("True", dv)
else:
    dv = 10-dv
    if dvtesta == dv:
        print("True", dv)
    else:
        print("False", dv)
