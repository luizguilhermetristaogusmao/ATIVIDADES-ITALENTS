nota = float(input("Digite a nota de aluno entre 0.0 e 10.0: "))

if (nota < 0.0 or nota > 10.00):
    print("ERRO")
elif (nota < 6.00):
    print("Nota F")
elif (nota >= 6.00 and nota < 7.00):
    print("Nota D")
elif (nota >= 7.00 and nota < 8.00):
    print("Nota C")
elif (nota >= 8.00 and nota < 9.00):
    print("Nota B")
else:
    print("Nota A")

