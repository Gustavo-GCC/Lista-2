#Importação de bibliotecas

#Declaração de variáveis
hora_inicio: int = 0
minuto_inicio: int = 0
hora_final: int = 0
minuto_final: int = 0
duração: int = 0
tranformacao_minutos_inicio: int = 0
tranformacao_minutos_final: int = 0
reconversao_hora: int = 0
reconversao_minuto: int = 0


#Início

hora_inicio = int(input('Que horas o jogo vai começar? '))
minuto_inicio = int(input('E os minutos? '))
hora_final = int(input('Que horas o jogo terminará? '))
minuto_final = int(input('E os minutos? '))

tranformacao_minutos_inicio = 60 * hora_inicio + minuto_inicio
tranformacao_minutos_final = 60 * hora_final + minuto_final

if hora_final >= hora_inicio:
    duração = tranformacao_minutos_final - tranformacao_minutos_inicio
else: 
    duração = 1440 - (tranformacao_minutos_inicio - tranformacao_minutos_final) #1440 minutos são 24h
    
reconversao_hora = duração // 60
reconversao_minuto = duração % 60

print(f'O jogo vai durar um total de {reconversao_hora:02}:{reconversao_minuto:02}')

#Fim