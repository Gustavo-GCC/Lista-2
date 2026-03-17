#Importação de bibliotecas

#Declaração de variáveis
tabuada: int = 0
multiplos: int = 0
contador: int = 0

#Início

tabuada = int(input('Digite um número para imprimir sua tabuada: '))

print(f'A tabuada do número {tabuada} é:')

while contador < 11:  
    multiplos = tabuada * contador
    print(f'\t {tabuada} x {contador} = {multiplos}')      
    contador += 1

#Fim