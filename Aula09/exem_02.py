import os

os.system('cls')

try:
    resp = input('Informe (s/n): ').lower()

    if resp == '':
        raise EOFError('Você não digitou nada')
    if resp.isdigit():
        raise ValueError('Não informe números')
except EOFError as e:
    print(f'{e}')
except ValueError as e:
    print(f'{e}')