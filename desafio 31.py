ano= int(input('DIGITE O Ano para Analizar? '))
a1 = 2023
input("Processando...")
if ano % 4 ==0 and ano % 100 !=0:
    print(F'O ano {ano} é BISSEXTO')

else:
    print(f'O ano {ano} não é BISSEXTO')

