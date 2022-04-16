vlrLaptop = float(input("Informe o valor do laptop (em Reais):"))
vlrEntrada = float(input("Informe o valor de entrada para o laptop (em Reais):"))
vlrPoupar = float(input("Informe o valor inicial para poupança (em Reais):"))
diasAguardando = 1
##diasSemana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
while vlrLaptop > vlrEntrada:
    for i in range(7):
        print(i, vlrEntrada, vlrPoupar)
        vlrEntrada = vlrEntrada + vlrPoupar
        vlrPoupar = vlrPoupar + 1.0
        if vlrEntrada >= vlrLaptop:
            print(vlrLaptop, vlrEntrada, vlrPoupar, diasAguardando)
            break
        diasAguardando = diasAguardando + 1
