valor = float(input("Digite o valor para ser convertido: "))
conversao_dolar = valor * 4.91
conversao_euro = valor * 5.26
conversao_libra_esterlina = valor * 6.00
conversao_dolar_canadense = valor * 3.55
conversao_peso_argentino = valor * 0.014
conversao_peso_chileno = valor * 0.0054

print(f"O valor digitado convertido para dolar é U${conversao_dolar}, para euro é €{conversao_euro}, para libra esterlina é  £{conversao_libra_esterlina}, para dolar canadense é C${conversao_dolar_canadense}, para peso argentino é ARS {conversao_peso_argentino} e para peso chileno é CLP {conversao_peso_chileno}")