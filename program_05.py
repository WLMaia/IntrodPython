magnitude=0.0
while (magnitude >= 0):
    magnitude = float(input("Informe o índice de magnitude do terremoto (na escala Richter):"))
    if (magnitude < 0.0):
        print("Impossível")
        exit(0)
    elif (magnitude >=0.0 and magnitude < 1.9):
        print("Micro")
    elif (magnitude >= 1.9 and magnitude < 3.9):
        print("Pequeno")
    elif (magnitude >=3.9 and magnitude < 4.9):
        print("Leve")
    elif (magnitude >=4.9 and magnitude < 5.9):
        print("Moderado")
    elif (magnitude >=5.9 and magnitude < 6.9):
        print("Forte")
    elif (magnitude >= 6.9 and magnitude < 8.9):
        print("Grande")
    else:
        if (magnitude > 8.9):
            print("Muito Grande")