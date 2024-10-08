import os

os.system('cls')

try:
    n = int(input('Informe um número: '))
except:
    print(f'Erro: O usuário não digitou um número!')


# try:
#     n = int(input('Informe um número: '))
# except ValueError as e:
#     print(f'Erro: O usuário não digitou um número!\nErro: {e}')
# except KeyboardInterrupt:
#     print(f'\nErro: O usuário cancelou a operação!')

