# Importação de bibliotecas
import math

# Declaração de variáveis 
a: float = 0.0
b: float = 0.0
c: float = 0.0
x: float = 0.0
DISCRIMINANTE: float = 0.0


# Início 

a = float(input('Qual é o valor do coeficiente quadrático? '))
b = float(input('Qual é o valor do coeficiente linear? '))
c = float(input('Qual é o valor do termo independente? '))
DISCRIMINANTE = math.pow(b, 2) - 4*a*c

if DISCRIMINANTE < 0:
    print('As raízes da equação não pertencem ao conjunto dos números reais.')
elif DISCRIMINANTE == 0:
    x = (-b) / 2*a
    print('A única raiz da equação é', x)
else:
    x = ((-b) - math.sqrt(DISCRIMINANTE)) / 2*a
    print('A primeira raiz é', x)
    x = ((-b) + math.sqrt(DISCRIMINANTE)) / 2*a
    print('E a segunda raiz é', x)

# Fim