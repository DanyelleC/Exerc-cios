#1
vitorias = 0
empates = 0
derrotas = 0

for i in range(1, 6):
    gols_selecao = int(input(f"Gols da Seleção no jogo {i}: "))
    gols_adv = int(input(f"Gols do adversário no jogo {i}: "))
    
    if gols_selecao > gols_adv:
        vitorias += 1
    elif gols_selecao == gols_adv:
        empates += 1
    else:
        derrotas += 1

print("=== Torneio de Futebol ===")
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
 #================================
#2
import random

secreto = random.randint(1, 20)
tentativas = 5

for i in range(tentativas):
    palpite = int(input("Adivinhe o número (1 a 20): "))
    
    if palpite == secreto:
        print("Você acertou!")
        break
    elif palpite < secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")
else:
    print(f"Game over! O número era {secreto}")
#=========================================
#3
total = 0
pessoas = int(input("Quantas pessoas vão ao show? "))

for i in range(1, pessoas + 1):
    idade = int(input(f"Idade da pessoa {i}: "))
    if idade <= 12:
        print("Entrada grátis")
    elif 13 <= idade <= 17:
        print("Meia entrada (R$ 10)")
        total += 10
    else:
        print("Ingresso inteiro (R$ 20)")
        total += 20

print(f"Total arrecadado: R$ {total}")
#===================================
#4

print("== Quiz de Conhecimentos Gerais ==")
pontos = 0

respostas = [
    ("Capital do Brasil?", ["São Paulo", "Brasília", "Rio de Janeiro"], 2),
    ("Planeta conhecido como planeta vermelho?", ["Marte", "Júpiter", "Vênus"], 1),
    ("Quem escreveu Dom Quixote?", ["Machado de Assis", "Cervantes", "Shakespeare"], 2),
    ("Qual o maior oceano?", ["Atlântico", "Pacífico", "Índico"], 2),
    ("Qual a cor da clorofila?", ["Verde", "Azul", "Amarela"], 1)
]

for i, (pergunta, opcoes, correta) in enumerate(respostas, start=1):
    print(f"{i}) {pergunta}")
    for j, opcao in enumerate(opcoes, start=1):
        print(f"{j}- {opcao}")
    resposta = int(input("Sua resposta: "))
    if resposta == correta:
        pontos += 1

print(f"Pontuação final: {pontos}/5")
if pontos == 5:
    print("Gênio!")
elif pontos >= 3:
    print("Mandou bem!")
elif pontos >= 1:
    print("Precisa estudar mais")
else:
    print("Zerou o quiz")

#==================================
#5

pontuacoes = [0, 0, 0]

for avaliador in range(1, 4):
    for candidato in range(3):
        nota = int(input(f"Nota do avaliador {avaliador} para o candidato {candidato+1}: "))
        pontuacoes[candidato] += nota

print("Pontuação final:")
for i, p in enumerate(pontuacoes, start=1):
    print(f"Candidato {i}: {p}")

maior = max(pontuacoes)
if pontuacoes.count(maior) > 1:
    print("Empate! Disputa acirrada")
else:
    vencedor = pontuacoes.index(maior) + 1
    print(f"Candidato {vencedor} é o campeão!")

#====================================
#6

nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    situacao = "APROVADO!"
elif nota >= 5:
    situacao = "em RECUPERAÇÃO!"
else:
    situacao = "REPROVADO!"

print(f"{nome} está {situacao}")

#==================================

