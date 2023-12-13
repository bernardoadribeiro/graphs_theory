from utils import _check_binary_difference, _check_binary_difference_v2


class Hypercube():
    """ Hypercube class with generate method.

        Methods:
        - `_generate_vertices(S: int)`: Generates the Vertices of the hypercube
        - `_generate_edges(S: int)`: Generates the edges of the hypercube
        - `generate(S: int=2)`: Returns the vertices and edges of the n-hypercube.
                                Default value for `S` is 2.

        ```python
        lenght(E) = 2^S
        ```
    """

    def _generate_vertices(self, S: int) -> list:
        """ Generates Hypercube vertices list based on the given `S` size.
        """
        V = []

        for i in range(2 ** S):
            # Converts `i` to a binart string
            # Use python Slice `[2:]` to remove the prefix '0b' added by bin()
            # zfill() Fill the binary string with zeros on the left if needed.
            vertex = bin(i)[2:].zfill(S)
            V.append(vertex)

        # print(V)
        return V

    def _generate_edges(self, S: int, V: list) -> set:
        """ Generates Hypercube Edges set based on the given `S` size.
        """
        E = set()

        # For each Vertice
        for i, v in enumerate(V):
            # For each next vertice after V[i]
            for j in range(i+1, len(V)):
                # Verify if him has difference in One digit, with others vertices.
                # If yes, create a tuple with the 2 vertices that has difference
                # in One digit. Else, verify the next vertice.
                if _check_binary_difference_v2(v, V[j]):
                    edge = (v, V[j])
                    E.add(edge)

        # print(E)
        return E

    def generate(self, S: int = 2):
        """ Generate a n-dimencional Hypercube Graph
        """
        print(f"Generating Hypercube Graph of {S}-dimensional")

        V = self._generate_vertices(S)
        E = self._generate_edges(S, V)

        return V, E


V, E = Hypercube().generate(4)
print(f'V (s: {len(V)}): {V} \nE (s: {len(E)}): {E}')


# for i in range(1, 2):
#     V, E = Hypercube().generate(i)
#     print("===================")
#     print(f'Size: {i}\n'
#           f'V (s: {len(V)})\n'
#           f'E (s: {len(E)})'
#           )
#     print("===================")
