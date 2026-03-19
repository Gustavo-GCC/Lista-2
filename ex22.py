#Importação de bibliotecas

#Declaração de variáveis
p: int = 0
s: int = 0

#Início

while p == s:
    p = int(input('Digite um valor: '))
    s = int(input('Digite outro: '))

if p > s:
    print(f'{p} e {s}')
else:
    print(f'{s} e {p}')

#Fim
