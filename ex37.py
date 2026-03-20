#Importação de bibliotecas

#Declaração de variáveis
n: int = 0
fibonacci: int = 1
contador: int = 0
sequencia: int = 0

#Início

n = int(input('Digite um número da sequência de Fibonacci: '))

print(contador)

while contador <= n:
    sequencia += fibonacci
    print(sequencia)
    fibonacci = sequencia
    contador += 1

#Fim

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144