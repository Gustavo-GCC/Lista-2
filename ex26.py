#Importação de bibliotecas

#Declaração de variáveis
x: int = 0
y: int = 0
maior: int = 0
menor: int = 0

#Início

while x == y:
    x = int(input('Digite um valor: '))
    y = int(input('Digite outro valor: '))


if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x


if maior % menor == 0:
    print(f'Sim, {maior} é múltiplo de {menor}')
else: 
    print(f'Não, {maior} não é múltiplo de {menor}')

#Fim
