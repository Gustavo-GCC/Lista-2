#Importação de bibliotecas

#Declaração de variáveis
n: int = 0
contador: int = 1
fatorial: int = 1
somatorio: float = 0.0

#Início

n = int(input('Digite um número: '))

while contador <= n:
    fatorial *= contador
    somatorio += 1/fatorial
    contador += 1

print(f'O somatório da série resulta em {somatorio + 1:.2f}')

#Fim
