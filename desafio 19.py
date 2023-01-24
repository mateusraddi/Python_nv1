import random

p1 = (input('primeiro aluno: '))

p2 = (input('segundo aluno: '))

p3 = (input('terceiro aluno: '))

p4 = (input('quarto aluno: '))

sorteio = [p1, p2, p3, p4]
print(f'O aluno escolhido foi {random.choice(sorteio)}')