nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo tem {len(nome)-nome.count(" ")} letras')
print(f'Seu primeiro nome é {nome.split("0")} e ele tem {nome.find(" ")}')











