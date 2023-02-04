nome = str(input('Digite seu nome completo: ')).strip()
s = nome.split()
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}'.format(s[0]))
print('Seu ultimo nome é {}'.format(s[-1]))

