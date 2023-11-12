num = int(input("Digite um número inteiro: "))

contador = 1

while contador < num:
   contador = contador + 1
   if (num % contador) == 0:
      print(contador)
      