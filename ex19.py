#Importação de bibliotecas

#Declaração de variáveis
primeiro: float = 0.0
segundo: float = 0.0

#Início

primeiro = float(input('Digite um valor: '))
segundo = float(input('Digite outro valor: '))

if primeiro > segundo:
    print(primeiro)
elif segundo > primeiro:
    print(segundo)
else:
    print('Os valores são iguais.')

#Fim
