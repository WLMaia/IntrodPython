frase = input("Digite uma frase:").strip()
frase = frase.replace(" ", "")
contarCaracter = 0
for i in frase:
    contarCaracter = contarCaracter + 1
print("Quantidade de letras: ", contarCaracter)
