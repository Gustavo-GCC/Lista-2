#Importação de bibliotecas

#Declaração de variáveis
valor: int = 0
contador: int = 1
soma: float = 0.0

#Início

valor = int(input("Digite um número: "))

while contador <= valor:
    soma += 1/contador
    contador += 1

print(f'O resultado disso é {soma:.2f}')


#Fim