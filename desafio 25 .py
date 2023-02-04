
import array


frase = str(input('Digite uma frase:  ')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print(f'a ultima letra apareceu na posição {frase.rfind("A")+1}')














