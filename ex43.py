#Importação de bibliotecas

#Declaração de variáveis
ana: float = 1.1
maria: float = 1.5
anos: int = 0

#Início

while ana < maria:
    ana += 0.03
    maria += 0.02
    anos += 1

print(f'Após {anos} anos, Ana terá {ana:.2f} metros, enqaunto Maria terá {maria:.2f} metros')

#Fim