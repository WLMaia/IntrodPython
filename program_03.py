centavos=int(input("Informe o valor R$ de centavos:"))
cent1=cent5=cent10=cent25=cent50=real1=0
real1=centavos//100
cent50=(centavos % 100)//50
cent25=(centavos % 50)//25
cent10=(centavos % 25)//10
cent5=(centavos % 10)//5
cent1=(centavos % 5)//1
print("Moedas de 1  Real :", real1)
print("Moedas de 50 centavos :", cent50)
print("Moedas de 25 centavos :", cent25)
print("Moedas de 10 centavos :", cent10)
print("Moedas de 1  centavo  :", cent1)