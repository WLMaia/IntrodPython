import re

def inverte(palavra):
    if re.match(r'^\w+$', palavra):
        return palavra[::-1]
    return palavra

def invertePalavra(palavraInversa):
    if re.match(r'^\w+$', palavraInversa):
        return palavraInversa[::-1]
    return palavraInversa

frase = input("Digite uma frase:").strip()

invertida = ''.join(inverte(palavra) for palavra in re.split(r'(\W+)', frase))
print(invertida)

invertida2 = ''.join(invertePalavra(palavraInversa) for palavraInversa in re.split(r'(\W+)', frase))
print(invertida2)