# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Problema do Caixeiro Viajante, modelo de solução: Força Bruta + Plano Cartesiano
import itertools
import math
import matplotlib.pyplot as plt


# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Gerando gráfico para exibição dos caminhos percorridos
def plot_melhor_caminho(cidades, caminho):
    x = [cidades[cidade][0] for cidade in caminho]
    y = [cidades[cidade][1] for cidade in caminho]
    
    # Adicione a primeira cidade ao final para fechar o ciclo
    x.append(x[0])
    y.append(y[0])
    
    plt.plot(x, y, marker='o')
    plt.title('Caminho do Caixeiro Viajante')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(True)
    plt.show()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Calculo de distância baseada nas coordenadas de cada 
# cidade utilizando a fórmula euclidiana para calcular 
# as distâncias.
#
# Fonte: https://pt.wikipedia.org/wiki/Dist%C3%A2ncia_euclidiana
# 
def calcular_distancia(coord_cidade1, coord_cidade2):
    x1, y1 = coord_cidade1
    x2, y2 = coord_cidade2
    distancia_entre_pontos = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia_entre_pontos


def calcular_distancia_total(caminho, cidades):
    distancia_total = 0

    for i in range(len(caminho) - 1):
        coord_cidade_atual = caminho[i]
        coord_proxima_cidade = caminho[i + 1]

        # Soma a distância da cidade atual até a próxima cidade
        distancia_total += calcular_distancia(cidades[coord_cidade_atual], cidades[coord_proxima_cidade])
    
    # Soma a distância de volta ao ponto de partida
    distancia_total += calcular_distancia(cidades[caminho[-1]], cidades[caminho[0]])  
    return distancia_total


def caixeiro_viajante(cidades):
    execucoes = 0
    complexidade = len(cidades)

    if(complexidade > 8):
      raise Exception('Isso aqui tem complexidade O(n!) tem certeza? Foi o que eu pensei! :)')

    melhor_distancia = float('inf')
    melhor_caminho = None
    
    for caminho in itertools.permutations(cidades.keys()):
        # intertools.permutations(cidades.keys()) => retorna todas as possibilidades de caminhos
        execucoes += 1
        distancia_atual = calcular_distancia_total(caminho, cidades)

        if distancia_atual < melhor_distancia:
            melhor_distancia = distancia_atual
            melhor_caminho = caminho
            

    return melhor_caminho, melhor_distancia, execucoes, complexidade

# # # # # # # # # # # # # # 
# Coordenadas das cidades
# 
# 
# cidades = {
#     0: (0, 0),
#     1: (1, 3),
#     2: (4, 6),
#     3: (7, 1)
# }

cidades = {
    0: (4, 2),
    1: (13, 7),
    2: (2, 4),
    3: (12, 13),
    4: (7, 6),
    5: (10, 10),
    6: (3, 11),
    7: (6, 9)
}


# # # # # # # # # # # # # 
# Executando o algoritmo
melhor_caminho, melhor_distancia, execucoes, complexidade = caixeiro_viajante(cidades)

print("Melhor caminho:", melhor_caminho)
print("Melhor distância aproximada: ", round(melhor_distancia, 2))
print("Total de execuções: ", execucoes)
print("Complexidade: O(" + str(complexidade) + "!)")

plot_melhor_caminho(cidades, melhor_caminho)
