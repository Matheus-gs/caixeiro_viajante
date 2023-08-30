# O Caixeiro Viajante
O algoritmo apresentado é uma implementação básica do método de força bruta para resolver o problema do Caixeiro Viajante

![image](https://github.com/Matheus-gs/caixeiro_viajante/assets/54650216/b670d1f3-1b49-4096-8d4e-8eb1ca26395c)

# Metodologia Geral

### Representação das cidades 
O algoritmo assume que as cidades são representadas por coordenadas no plano bidimensional (x, y). Isso permite calcular as distâncias entre as cidades utilizando a fórmula da distância euclidiana.

### Geração de permutações
O algoritmo utiliza a biblioteca `itertools` para gerar todas as permutações possíveis das cidades. Isso significa que ele cria todas as combinações de cidades possíveis para avaliar qual delas forma o caminho mais curto.

### Cálculo de distâncias
A função `calcular_distancia` é usada para calcular a distância entre duas cidades com base em suas coordenadas. A função `calcular_distancia_total` usa essa função para calcular a distância total percorrida em um caminho específico.

### Iteração sobre permutações
O algoritmo itera sobre todas as permutações geradas pelo `itertools.permutations`. Para cada permutação (ou seja, para cada caminho possível), ele calcula a distância total percorrida.

### Atualização da melhor solução
O algoritmo mantém um registro da menor distância encontrada até o momento e do caminho correspondente que produz essa distância. Se uma nova permutação produzir uma distância menor, a solução é atualizada.

### Retorno da solução
Após iterar por todas as permutações possíveis, o algoritmo retorna o caminho e a distância mínima encontrada.

### Complexidade
Devido à geração de todas as permutações, a complexidade do algoritmo é fatorial ou seja *O(n!)* isso significa que a sua eficiência diminui rapidamente à medida que o número de cidades aumenta.

### Pontos fortes e limitações
Embora esse algoritmo seja simples de entender e implementar, ele é ineficiente para grandes conjuntos de cidades, devido à complexidade fatorial. Existem abordagens mais eficientes, como a Programação Dinâmica, Heurísticas e Algoritmos Genéticos, que lidam melhor com problemas maiores.

Em resumo, a metodologia utilizada neste algoritmo é baseada em testar todas as permutações possíveis para encontrar o caminho mais curto entre as cidades, utilizando coordenadas e cálculos de distância euclidiana.


