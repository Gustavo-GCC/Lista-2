#Importação de bibliotecas

#Declaração de variáveis
x: int = 0
fatorial: int = 1

#Início

x = int(input("Digite um número: "))

while x > 1:
    fatorial *= x
    x -= 1

print(f'O fatorial de {x} é {fatorial}')

#Fim