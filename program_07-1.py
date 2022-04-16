palavra = input().strip()
frase = input().strip()
frase_codificada =""
c = ' '
tam = len(frase)
j = 0
while j < tam:
    c = frase[j]
    if c >= 'a' and c <=  'z':
        if c == 'a':
            frase_codificada = frase_codificada + 'i'
        elif c == 'i' :
            frase_codificada = frase_codificada + 'a'
        elif c =='z':
            frase_codificada = frase_codificada + 'p'
        elif c =='p':
            frase_codificada = frase_codificada + 'z'
        elif c =='e':
            frase_codificada = frase_codificada + 'o'
        elif c =='o':
            frase_codificada = frase_codificada + 'e'
        elif c =='n':
            frase_codificada = frase_codificada + 'l'
        elif c =='l':
            frase_codificada = frase_codificada + 'n'
        elif c =='r':
            frase_codificada = frase_codificada + 't'
        elif c =='t':
            frase_codificada = frase_codificada + 'r'
        else:
            frase_codificada = frase_codificada + c
    elif c >= 'A' and c <= 'Z':
        if c == 'A':
            frase_codificada = frase_codificada + 'I'
        elif c =='I':
            frase_codificada = frase_codificada + 'A'
        elif c =='Z':
            frase_codificada = frase_codificada + 'P'
        elif c =='P':
            frase_codificada = frase_codificada + 'Z'
        elif c =='E':
            frase_codificada = frase_codificada + 'O'
        elif c =='O':
            frase_codificada = frase_codificada + 'E'
        elif c =='N':
            frase_codificada = frase_codificada + 'L'
        elif c =='L':
            frase_codificada = frase_codificada + 'N'
        elif c =='R':
            frase_codificada = frase_codificada + 'T'
        elif c =='T':
            frase_codificada = frase_codificada + 'R'
        else:
            frase_codificada = frase_codificada + c
    else:
        frase_codificada = frase_codificada + c
    j = j + 1
palavras = []
nova_palavra = ''
for c in frase_codificada:
    if c not in ' ´´^~{[}]/?º:;>.<,\|@#$%&*()':
        nova_palavra = nova_palavra + c
    elif c == ' ':
        palavras.append(nova_palavra)
        nova_palavra = ''
palavras.append(nova_palavra)

conta = 0
for p  in palavras:
    if p == palavra:
        conta=conta+1
print(f'{palavra}: {conta}\n{frase_codificada}')