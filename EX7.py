salario = float(input("Digite o valor do salário do colaborador: "))

if (salario > 0 and salario < 280.00):
    print(f"O valor do salário antes do reajuste era de R${salario}")

    valor_aumento = (20/100) * salario
    salario = salario + valor_aumento

    print(f"O percentual de aumento do salário foi de 20%, o valor do aumento foi de R${valor_aumento} e o novo salário após o ajuste é de R${salario}")
elif (salario >= 280.00 and salario < 700.00):
    print(f"O valor do salário antes do reajuste era de R${salario}")
    
    valor_aumento = (15/100) * salario
    salario = salario + valor_aumento

    print(f"O percentual de aumento do salário foi de 15%, o valor do aumento foi de R${valor_aumento} e o novo salário após o ajuste é de R${salario}")
elif (salario >= 700.00 and salario < 1500.00):
    print(f"O valor do salário antes do reajuste era de R${salario}")
    
    valor_aumento = (10/100) * salario
    salario = salario + valor_aumento

    print(f"O percentual de aumento do salário foi de 10%, o valor do aumento foi de R${valor_aumento} e o novo salário após o ajuste é de R${salario}")
else:
    print(f"O valor do salário antes do reajuste era de R${salario}")
    
    valor_aumento = (5/100) * salario
    salario = salario + valor_aumento

    print(f"O percentual de aumento do salário foi de 5%, o valor do aumento foi de R${valor_aumento} e o novo salário após o ajuste é de R${salario}")
    
    