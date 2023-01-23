import math

co = float(input('Comprimento do cateto oposto:  '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa  vai medir {math.hypot(co,ca):.2f}')

