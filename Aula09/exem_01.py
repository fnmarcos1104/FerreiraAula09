import os

os.system('cls')

# try:
#     n = int(input('Informe um número: '))
# except:
#     print(f'Erro: O usuário não digitou um número!')


# try:
#     n = int(input('Informe um número: '))
# except ValueError as e:
#     print(f'Erro: O usuário não digitou um número!\nErro: {e}')
# except KeyboardInterrupt:
#     print(f'\nErro: O usuário cancelou a operação!')



try:
    n = int(input('Informe um número: '))
except (ValueError, KeyboardInterrupt) as e:
    print(f'Erro: O usuário não digitou um número!\nErro: {e}')
else:
    print(f'Você informou: {n}')




# try:
#     txt = input('Informe um nome: ')[0]
# except IndexError as e:
#     print(f'Erro: É necessário digitar algo!\nError: {e}')
# else:
#     print('OK!')
# finally:
#     print('Fim')