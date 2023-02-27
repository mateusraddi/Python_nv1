import random
print("-=-"*20)
print('vou pensar em um numero de 0 e 5. Tente adivinhar...')
print("-=-"*20)
pc = random.randint(0,2)
numero = int(input('Em que  número eu pensei? '))
input("PROCESSANDO...")
if numero == pc:
    print("Parabens!Voce conseguiu me Vencer!")
else:
    print(f'GANHEI!, eu pensei no numero {pc} ')


