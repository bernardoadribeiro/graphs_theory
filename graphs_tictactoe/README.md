# Questão 2 - JOGO DA VELHA:

O cada situação possível de um jogo da velha pode ser representado por uma string de 9 posições, cada posição representando uma das 9 casas do tabuleiro e cada casa pode ter um dos seguintes valores:

- `-` : Casa vazia
- `x` : Casa ocupada por um x
- `o` : Casa ocupada por um o

a) Gere o grafo de SEMI-hipercubo de todas jogadas possíveis do Jogo da Velha a partir do vértice inicial '---------'. O "semi" significa que ele não será um hipercubo perfeito, pois dois vértices para serem vizinhos não bastam ter um dígito diferente, mas um dígito diferente de um jogador diferente (ou seja: uma jogada 'x' deve ser seguida por uma jogada 'o' para serem vizinhos, e vice versa)

b) Modifique o algoritmo de Árvores Geradoras para criar, a partir do hipercubo anterior, uma árvore de todas as próximas jogadas possíveis a partir de uma jogada inicial.