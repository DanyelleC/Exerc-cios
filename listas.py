#Atividade de listas 
#Professor: Frederico Favor
#Aluna: Danyelle Correia
#=============================#
#1- criar lista de livros

livros = ["Drácula", "Frankenstein","O médico e o monstro"]
print ("Lista de livros",livros)

#=============================#
#2- mostrar apenas o primeiro e o ultimo elemento
print ("primeiro livro:", livros [0])
print("Último livro:", livros[-1])

#==============================#
#3- adicionar mais dois livros
livros.append("O Morro dos Ventos Uivantes")
livros.append("Carmilla")
print("Lista atualizada:", livros)

#=============================#
#4- Inserir "Duna" na segunda posição

livros.insert(1,"Duna")
print("Lista com Duna:",livros)

#============================#
#5- Remover "Silêncio dos inocentes" 
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
else:
    print("Livro não encontrado")

print ("Lista final de livros:",livros)

#==============================#
#6- Quantas vezes o numero 2 aparece
numeros= [1, 2, 3, 2, 4, 2, 5]
print("O número 2 aparece:",numeros.count(2),"vezes")

#==============================#
#7- Percorrer lista de livros
for livro in livros:
    print(f' livro "{livro}" é interessante.')

#==============================#
#8- Exibir apenas idades maiores ou iguais a 18
idades = [12, 18, 25, 14, 30]
for idade in idades:
    if idade >= 18:
        print("Idade permitida:", idade)

#==============================#
#9- Calcular soma manualmente
valores = [10, 20, 30, 40]
soma = 0
for v in valores:
    soma += v
print ("Soma dos valores:", soma)

#===============================#
#10- Notas de dois alunos
# Notas do aluno 1
nota1_a1 = float(input("\nDigite a primeira nota do aluno 1: "))
nota2_a1 = float(input("\nDigite a segunda nota do aluno 1: "))
nota3_a1 = float(input("\nDigite a terceira nota do aluno 1: "))

# Notas do aluno 2
nota1_a2 = float(input("\nDigite a primeira nota do aluno 2: "))
nota2_a2 = float(input("\nDigite a segunda nota do aluno 2: "))
nota3_a2 = float(input("\nDigite a terceira nota do aluno 2: "))

aluno1 = [nota1_a1, nota2_a1, nota3_a1]
aluno2 = [nota1_a2, nota2_a2, nota3_a2]

notas = [aluno1, aluno2]

# médias
media1 = (nota1_a1 + nota2_a1 + nota3_a1) / 3
media2 = (nota1_a2 + nota2_a2 + nota3_a2) / 3

print("\nLista de notas:", notas)
print("\nMédia do aluno 1:", media1)
print("\nMédia do aluno 2:", media2)

#===============================#
#11- Criar um tabuleiro vazio 8x8 com list comprehension

tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]
pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]

# peças pretas
tabuleiro[0] = pecas                 
tabuleiro[1] = ["pea"] * 8           

# peças brancas
tabuleiro[6] = ["pea"] * 8           
tabuleiro[7] = pecas                 

for linha in tabuleiro:
    print(linha)
