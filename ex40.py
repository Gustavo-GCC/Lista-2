#Importação de bibliotecas

#Declaração de variáveis
maior: int = 0
menor: int = 0
temp: int = 0
contador: int = 0
primo: bool
divisor: int = 0

#Início

while maior == menor and maior < 2 or menor < 2:
    maior = int(input('Digite um número: '))
    menor = int(input('Digite outro: '))

if menor > maior:
    temp = menor
    menor = maior
    maior = temp


while menor <= maior:
    primo = True
    divisor = 2

    while divisor * divisor <= menor:
        if menor % divisor == 0:
            primo = False
            break
        divisor += 1
    
    if primo:
        print(menor)

    menor += 1
    
#Fim