nome = str(input('Digite seu nome completo: ')).strip()
n = input('Digite seu primeiro nome: ')
print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo tem {len(nome)-nome.count(" ")} letras')
print(f'Seu primeiro nome é {n} e ele tem {nome.find(" ")} letras')















