#Importação de bibliotecas

#Declaração de variáveis
n: int = 0

#Início

n = int(input('Digite um número: '))

if n % 6 == 0:
    print(f'{n} é divisível por 2 e 3')
else:
    print(f'{n} não é divisível por 2 ou 3')

#Fim
