#Importação de bibliotecas

#Declaração de variáveis
hora_inicial: int = 0
minuto_inicial: int = 0
hora_final: int = 0
minuto_final: int = 0
duraçãoH: int = 0
duraçãoM: int = 0


#Início

hora_inicial = int(input('Que horas o jogo vai começar? '))
minuto_inicial = int(input('E os minutos? '))
hora_final = int(input('Que horas o jogo terminará? '))
minuto_final = int(input('E os minutos? '))

if hora_inicial >= hora_final:
    duraçãoH = hora_inicial - hora_final
else: 
    duraçãoH =  hora_final - hora_inicial 
    

if minuto_inicial >= minuto_final:
    duraçãoM = minuto_inicial - minuto_final
else:
    duraçãoM =  minuto_final - minuto_inicial

#Fim