#Importação de bibliotecas

#Declaração de variáveis
n: int = 0
maior: int = 0
menor: int = 0
total: int = 3
contador: int = 0
temp: int = 0

#Início

while contador < total:
    n = int(input(f'Número {contador + 1:02d}: '))
    if n > maior:
        maior = n
    elif menor < maior:
        menor = n
    contador += 1

print(f'O maior número da sequência é o {maior}')
print(f'E o menor, é o {menor}')

#Fim