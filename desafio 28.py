velocidade = int(input("qual é a velocidade do carro? "))
multa = 3500
kilometros = 1000
r = (multa*velocidade)/kilometros
if velocidade <=80:
    print('Tenha um Bom Dia! Dirija com Segurança')
else:
        print(f'Multado! voce excedeu o limite permitido que é de 80km/h\nvoce deve pagar uma multa de de {r}')