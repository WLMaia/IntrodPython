traduzir = input("Digite um texto: ").strip()

dic_zp = {'z:p', 'e:o', 'n:l', 'i:a', 't:r'}
##p = ['p', 'o', 'l', 'a', 'r']

for zp in dic_zp:
    traduzir = traduzir.replace(zp, dic_zp[zp])
print(traduzir)

##for i in range(len(traduzir)):
##    traduzir_zp = traduzir.replace(z,p)
##    print(traduzir)
##    print(traduzir_zp)
##print(traduzir)
##print(traduzir_zp)
##traduzir_zp = traduzir[::-1]
##print(traduzir_zp)

#dicionario_zp = {'z':'p',
#                 'e':'o',
#                 'n':'l',
#                 'i':'a',
#                 't':'r'}

##dicionario_pz = {'p':'z',
#                 'o':'e',
#                 'l':'n',
#                 'a':'i',
#                 'r':'t',
#                 'P':'Z',
#                 'O':'E',
#                 'L':'N',
#                 'A':'I',
#                 'R':'T'}
#for zp in dicionario_zp:
#    traduzir_zp = traduzir_zp.replace(zp, dicionario_zp[zp])
#print(traduzir_zp)
#print(dicionario_zp)
#print(dicionario_pz)