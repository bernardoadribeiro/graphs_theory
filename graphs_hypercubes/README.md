## Questão 1 - HIPERCUBOS:

Um hipercubo é um grafo não-orientado `G = {V,E}`, onde os vértices de V são strings binárias de tamanho S. Dois vértices `i,j ∈ V` estão conectados se, e somente se, as strings representadas por i e j diferem em somente um dígito. Por exemplo: 

- O 1-hipercubo é o grafo `G = {V,E}`, tal que `V = {0,1}` e `E = {(0,1)}`
- O 2-hipercubo é o grafo `G = {V,E}`, tal que `V = { '00', '01', '10', '11' }` e `E = { ('00', '01'), ('00', '10'), ('11', '01'), ('11', '10') }`

a) Crie um algoritmo que aceite um parâmetro S crie hipercubos de tamanho S, gerando o conjuntos V e E do hipercubo.

Veja a implementação no arquivo [hypercube.py](./hypercube.py)


b) Ache e explique uma fórmula fechada para calcular o número de vértices de um hipercubo cujos vértices são strings de tamanho

**Fórmula:** $\ 2^S $. Pois temos apenas 2 dígitos possíveis 0 e 1, logo, o que nos dá $\ S $ vértices possíveis. $\ S $ É a quantidade de vértices que desejamos.


c) Ache e explique uma fórmula fechada para calcular o número de arestas de um hipercubo cujos vértices são strings de tamanho S.

Cada vértice possui $\ S $ vizinhos pois cada um deles se diferente em apenas um dígito, e temos $\ 2^S $ vértices. Logo, temos: $\ S . 2^S $.