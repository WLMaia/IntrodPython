palavra = input().strip()
frase = input().strip()
result = ''

de   = ['Z', 'E', 'N', 'I', 'T', 'P', 'O', 'L', 'A', 'R']
para = ['P', 'O', 'L', 'A', 'R', 'Z', 'E', 'N', 'I', 'T']

for i in frase:
  j = i.upper()
  try:
    letra = para[de.index(j)]
  except:
    letra = j
  result += letra if i.isupper() else letra.lower()
  quantidade = result.upper().count(palavra.upper())
print(f'{palavra}: {quantidade}')
print(f'{result}')