viagem  = float(input('Qual é a Distancia da sua Viagem? '))
print(f'Voce está Prestes a começar uma viagem de {viagem}Km.')
n = (viagem * 0.5) 
n2 = (viagem * 0.45)
if viagem  <=200:
    print(f'e o preço da sua passagem será de {n:.2f} R$.')
else:
    print(f'E o preço da sua Passagem será de {n2:.2f} R$.')   
    