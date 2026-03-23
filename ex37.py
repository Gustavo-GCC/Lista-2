#Importação de bibliotecas

#Declaração de variáveis
entrada: int = 0
fibonacci: int = 0
proximo_termo: int = 1
contador: int = 0
sequencia: int = 0

#Início

entrada = int(input('Digite um número da sequência de Fibonacci: '))

while contador < entrada:
    print(fibonacci)
    sequencia = fibonacci + proximo_termo
    fibonacci = proximo_termo
    proximo_termo = sequencia
    contador += 1

#Fim

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144