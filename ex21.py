#Importação de bibliotecas

#Declaração de variáveis
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
media: float = 0.0

#Início

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print('APROVADO')
elif media >= 3 and media < 6:
    print('EXAME')
else:
    print('RETIDO')

#Fim