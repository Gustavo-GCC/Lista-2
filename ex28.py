#Importação de bibliotecas

#Declaração de variáveis
preço_atual: float = 0.0
media_mensal: float = 0.0
novo_preço: float = 0.0

#Início

preço_atual = float(input('Qual é o valor do produto? '))
media_mensal = float(input('E qual é sua média mensal? '))

if (preço_atual < 500) and (media_mensal < 30):
    novo_preço = preço_atual * 1.1
elif (preço_atual >= 500 and preço_atual < 1000) and (media_mensal >= 30 and media_mensal < 80):
    novo_preço = preço_atual * 1.15
elif (preço_atual >= 1000) and (media_mensal >= 80):
    novo_preço = preço_atual * 0.95
else:
    novo_preço = preço_atual

print(f'O novo preço é {novo_preço:.2f}')

#Fim