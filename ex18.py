#Importação de bibliotecas

#Declaração de variáveis
x: int = 0
y: int = 0
z: int = 0

#Início

x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))

if x > y:
    z = x - y
    print('A diferença entre os números é', z)
elif x < y:
    z = y - x
    print('A diferença entre os números é', z)
else:
    print('Os valores são iguais.')

#Fim