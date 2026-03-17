#Importação de bibliotecas

#Declaração de variáveis
a: int = 0
b: int = 0
maior: int = 0
menor: int = 0
contador: int = 0
somatorio: int = 0

#Início

while a == b:
    a = int(input("Primeiro valor: "))
    b = int(input("Segundo valor: "))

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

contador = menor + 1
while contador < maior:
    if contador % 2 != 0:
        somatorio += contador
    contador += 1

print(f'O somatório dos números ímpares entre {menor} e {maior} é {somatorio}.')

#Fim