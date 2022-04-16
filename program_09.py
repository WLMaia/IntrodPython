frase = input("Digite uma frase:").strip()
frase_inverte=frase
print(' Você digitou: {}'.format(frase))

frase = frase.replace(" ", "")
contarCaracter = 0

invertida = ' '.join(palavra[::-1] for palavra in frase_inverte.split())
print('A frase que você digitou invertida fica (por palavras): {}'.format(invertida))

for i in frase:
    contarCaracter = contarCaracter + 1
print("Quantidade de letras: ", contarCaracter)
print("A frase invertida completa fica: ", frase_inverte[::-1])
