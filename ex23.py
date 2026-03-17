#Importação de bibliotecas

#Declaração de variáveis
a: int = 0
b: int = 0
c: int = 0
d: int = 0

#Início

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

d = int(input('Quarto valor: '))

if d < a:
    print(f'Ordem:  {d}, {a}, {b}, {c}')
elif d > a and d < b:
    print(f'Ordem: {a}, {d}, {b}, {c}')
elif d > b and d < c:
    print(f'Ordem: {a}, {b}, {d}, {c} ')
else:
    print(f'Ordem: {a}, {b}, {c}, {d}')


#Fim