import numpy as np


#criação de 1 horário matriz 5dias X 5 blocos de aulas. É iniciada com valor 0.
dias, blocos = 5, 5
horario_grid = [[0 for x in range(dias)] for y in range(blocos)]



for i in range(dias):
    for j in range(blocos):
        horario_grid[i][j] = horario_grid[0][0]

for i in range(dias):
    for j in range(blocos):
        print("Resultado, i= " + str(+horario_grid[i][j]))

disciplinas = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 120]
professores = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Matriz com associação professor/disciplinas que leciona
# x disciplinas: y professores. espaço com 0, não há ligação, espaço com 1 indica conjunto disciplina/professor
profs_grid = [[0 for x in range(len(disciplinas))] for y in range(len(professores))]
for i in range(len(disciplinas)):
    for j in range(len(professores)):
        print(str(i) + " " + str(j))

profs_grid[0][7] = 1
profs_grid[0][1] = 1
profs_grid[3][2] = 1
profs_grid[0][3] = 1
profs_grid[0][4] = 1
profs_grid[2][2] = 1
profs_grid[2][6] = 1
profs_grid[1][7] = 1
profs_grid[0][8] = 1
profs_grid[5][9] = 1
profs_grid[6][11] = 1
profs_grid[7][12] = 1
profs_grid[8][13] = 1
profs_grid[8][14] = 1
profs_grid[7][15] = 1
profs_grid[8][16] = 1
profs_grid[6][17] = 1

for i in range(len(professores)):
    for j in range(len(disciplinas)):
        if profs_grid[i][j] != 0:
            print(str(professores[i]) + " " + str(disciplinas[j]))

#teste numpy
a = np.arange(6)
a[1]=9

for i in range(len(a)):
    print(str(a[i]))

