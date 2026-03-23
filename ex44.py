#Importação de bibliotecas
import math

#Declaração de variáveis
base: int = 0
expoente: int = 0
potencia: int = 0

#Início

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

potencia = pow(base, expoente)

print(f'{base} elevado a {expoente} resulta em {potencia}')

#Fim
