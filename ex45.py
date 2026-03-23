#Importação de bibliotecas

#Declaração de variáveis
contador: float = 1
somatorio: float = 0.0
adicoes: float = 0.0
subtracoes: float = 0.0
positivos: float = 0.0
negativos: float = 0.0

#Início

while contador <= 7.5:
    adicoes += (2*contador - 1) / (2*contador - 1) ** 2
    subtracoes -= 2*contador / (2*contador) ** 2

    positivos = (2*contador - 1) / (2*contador - 1) ** 2
    negativos = -(2*contador / (2*contador) ** 2)

    print(f'{positivos:.2f}\n{negativos:.2f}')
    somatorio = adicoes + subtracoes

    contador += 1

print(f'{adicoes:.2f}\n{subtracoes:.2f}')
print(f'{somatorio:.2f}')

#Fim