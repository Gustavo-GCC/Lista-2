#Importação de bibliotecas

#Declaração de variáveis
opcao: float = 0.0
poupanca: float = 0.0
renda_fixa: float = 0.0
investimento: float = 0.0

#Início

opcao = float(input('Digite 1 para a opção de poupança e 2 para renda fixa: '))
investimento = float(input('Qual valor desejas investir? '))

if opcao == 1:
    poupanca = investimento * 1.03
    print(f'Agora você possui R$ {poupanca:.2f} na sua conta')
elif opcao == 2:
    renda_fixa = investimento * 1.05
    print(f'Agora você possui R$ {renda_fixa:.2f} na sua conta')

#Fim
