from typing import List

dias, blocos = 5, 5
horario_grid = [[0 for x in range(dias)]for y in range(blocos)]


for i in range(dias):
    for j in range(blocos):
        horario_grid[i][j]= horario_grid[0][0]

for i in range(dias):
    for j in range(blocos):
        print ("Resultado, i= "+str(+horario_grid[i][j]))

disciplinas = ["Inteligência Artificial", "Cálculo", "Programação Imperativa", "Metodologias de Investigação", "Sistemas Analógicos e Digitais", "Teoria dos Circuitos Elétricos", "Bioeletricidade", "Microcontroladores", "Algoritmos e Estruturas de Dados I"]
professores = ["Ze", "Quim", "To", "Manel"]



profs_grid: list[list[int]] = [[0 for x in range(len(disciplinas))]for y in range(len(professores))]
for i in range(len(disciplinas)):
    for j in range(len(professores)):
        print (str(i)+" "+str(j))

profs_grid[0][7] = 1
profs_grid[0][1] = 1
profs_grid[3][2] = 1
profs_grid[0][3] = 1
profs_grid[0][4] = 1
profs_grid[2][2] = 1
profs_grid[2][6] = 1
profs_grid[1][7] = 1
profs_grid[0][8] = 1

for i in range(len(professores)):
    for j in range(len(disciplinas)):
        if profs_grid[i][j] != 0:
            print (str(professores[i])+" "+str(disciplinas[j]))
