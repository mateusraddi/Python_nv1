numero =int(input("Digite um número e eu lhe direi se é par ou ímpar."))
if numero == 0:
    print('Zero é nulo')
elif (numero % 2 == 0):
    print('O número',numero,'é par')
elif (numero % 2 !=0):
    print("O número",numero,"é ímpar")

