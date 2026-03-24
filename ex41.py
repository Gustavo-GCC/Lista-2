#Importação de bibliotecas

#Declaração de variáveis
p_dado: int = 0
s_dado: int = 7
soma: int = 0

#Início

while True:
    p_dado += 1
    s_dado -= 1

    if p_dado + s_dado == 7:
        print(f'Dado 1: {p_dado}\nDado 2: {s_dado}\n')

    if p_dado == 6:
        break

#Fim