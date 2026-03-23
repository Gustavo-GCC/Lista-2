#Importação de bibliotecas

#Declaração de variáveis
serie: float = 0
contador: int = 1

#Início

while contador <= 50:
    serie += contador / (2*contador - 1)
    print(f'{serie:.2f}')
    contador += 1

#Fim