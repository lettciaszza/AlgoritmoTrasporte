#Algoritmo de Transporte

import numpy as np
from scipy.optimize import linear_sum_assignment

def cantoNoroeste(cost_matrix, oferta, demanda):
    num_rows = len(oferta)
    num_cols = len(demanda)

    if sum(oferta) != sum(demanda):
        raise ValueError("O problema não está balanceado.")

    print("O problema está balanceado.")

    allocation = np.zeros((num_rows, num_cols), dtype=int)
    i, j = 0, 0

    while i < num_rows and j < num_cols:
        allocation[i, j] = min(oferta[i], demanda[j])
        oferta[i] -= allocation[i, j]
        demanda[j] -= allocation[i, j]

        if oferta[i] == 0:
            i += 1
        else:
            j += 1

    return allocation

def testeOtimalidade(cost_matrix, oferta, demanda, allocation):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)


    print("Alocação inicial:")
    print(allocation)

    print("\nValores de u e v:")
    u = np.zeros(len(oferta))
    v = np.zeros(len(demanda))

    for i, j in zip(row_ind, col_ind):
        u[i] = 0
        v[j] = cost_matrix[i, j] - u[i]

    print("u:", u)
    print("v:", v)


    for i in range(len(oferta)):
        for j in range(len(demanda)):
            if allocation[i, j] == 0:
                reduced_cost = cost_matrix[i, j] - u[i] - v[j]
                print(f"Custo reduzido para alocar na célula ({i+1}, {j+1}): {reduced_cost}")


costMatrix = np.array([
    [8, 12, 10],
    [4, 10, 6],
    [6, 15, 12]
])

oferta =  np.array([50, 70, 40])
demanda = np.array([60, 70, 30])

allocation = cantoNoroeste(costMatrix, oferta, demanda)
testeOtimalidade(costMatrix, oferta, demanda, allocation)
