## Exercício 1

**Questões**
- C.1) Represente os grafos completos e ponderados das intervalos cromáticos ascendentes e descendentes, onde os vértices representam as notas e o peso das arestas é o intervalo (ascendente ou descendente) entre as notas

    ```python
    MusicalScale().view_complete_scales_graph('major', 'ascending')
    
    #result
    {   'A': {'A': 0, 'B': 2, 'C#': 2, 'D': 1, 'E': 2, 'F#': 2, 'G#': 2},
        'A#': {'A': 2, 'A#': 0, 'C': 2, 'D': 2, 'D#': 1, 'F': 2, 'G': 2},
        'B': {'A#': 2, 'B': 0, 'C#': 2, 'D#': 2, 'E': 1, 'F#': 2, 'G#': 2},
        'C': {'A': 2, 'B': 2, 'C': 0, 'D': 2, 'E': 2, 'F': 1, 'G': 2},
        'C#': {'A#': 2, 'C': 2, 'C#': 0, 'D#': 2, 'F': 2, 'F#': 1, 'G#': 2},
        'D': {'A': 2, 'B': 2, 'C#': 2, 'D': 0, 'E': 2, 'F#': 2, 'G': 1},
        'D#': {'A#': 2, 'C': 2, 'D': 2, 'D#': 0, 'F': 2, 'G': 2, 'G#': 1},
        'E': {'A': 1, 'B': 2, 'C#': 2, 'D#': 2, 'E': 0, 'F#': 2, 'G#': 2},
        'F': {'A': 2, 'A#': 1, 'C': 2, 'D': 2, 'E': 2, 'F': 0, 'G': 2},
        'F#': {'A#': 2, 'B': 1, 'C#': 2, 'D#': 2, 'F': 2, 'F#': 0, 'G#': 2},
        'G': {'A': 2, 'B': 2, 'C': 1, 'D': 2, 'E': 2, 'F#': 2, 'G': 0},
        'G#': {'A#': 2, 'C': 2, 'C#': 1, 'D#': 2, 'F': 2, 'G': 2, 'G#': 0}
    }
    ```

- D.2) Crie um algoritmo que faça um percurso nos grafos ascendentes ou descendentes de tal forma que os intervalos entre os vértices respeitem os intervalos das escalas Maior, Menor e Pentatônica a partir de uma nota inicial (tom).

    ```python
    print(MusicalScale().generate('major', 'C', 'ascending'))
    
    #result:
    {'C': 0, 'D': 2, 'E': 2, 'F': 1, 'G': 2, 'A': 2, 'B': 2}
    ```

    ```python
    print(MusicalScale().generate('minor', 'C', 'descending'))
    
    #result:
    {'C': 0, 'Bb': 2, 'Ab': 1, 'G': 2, 'F': 2, 'Eb': 2, 'D': 1} 
    ```

    ```python
    print(MusicalScale().generate('pentatonica', 'C', 'ascending'))

    #result:
    {'C': 0, 'D': 2, 'E': 2, 'G': 3, 'A': 2} 
    ```

- D.3) Desenvolva um programa que gere uma melodia com notas escolhidas aleatoriamente, mas que estejam na mesma escala do mesmo tom. O algoritmo deve solicitar do usuário o tom da música e a escala, e então compor a música.
    ```python
    print(Music().compose_music('major', 'C', 'ascending'))
    
    #result:
    Notes: ['E', 'E', 'G', 'E', 'A', 'B', 'E', 'D', 'C', 'E', 'A', 'E']
    ```

### Como testar/rodar
- Execute com python o arquivo: `./graphs_musical_scale/main.py`
- Selecione uma das opções e pressione Enter.
- Verá o resultado da opção que escolheu no terminal.
- Fim.

> **Obs.:** Nas opções `[D3]` e `[Just Press Enter]`, caso seu OS não seja Windows, é possível que a reprodução do som não ocorra por estarmos usando a biblioteca `winsound`.
