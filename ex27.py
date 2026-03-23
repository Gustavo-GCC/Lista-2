#Importação de bibliotecas

#Declaração de variáveis
voltas: int = 0
duracao: int = 0
extensao: int = 0
velocidade_media: float = 0.0
conversao: float = 0.0

#Início

extensao = int(input('Digite quantos metros tem o circuito: '))
duracao = int(input('Digite quanto tempo leva para percorrê-la (EM MINUTOS): '))
voltas = int(input('Digite o números de voltas da pista: '))

velocidade_media = (extensao * voltas) / duracao 
conversao = velocidade_media * 0.06

print(f'A velocidade média é de {conversao:.2f} km/h')

#Fim