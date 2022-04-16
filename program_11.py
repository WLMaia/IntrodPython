frase = input("Digite uma frase:").strip()
frase_inverte=frase
print('Você digitou: {}'.format(frase))

if frase == frase[::-1]:
    print("Esta é uma palavra palindrome")
else:
    print("Esta palavra não é palindrome")
print('Palavra Invertida: {}'.format(frase[::-1]))

## def palindrome(a):
##    return a == a[::-1]
##
##palindrome('radar') 		# True