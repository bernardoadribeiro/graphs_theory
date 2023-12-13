from typing import Optional

import numpy as np
from numpy._typing import NDArray
from numpy import float64


class Graph():
    """
        Graph class which contains the methods that allow convert between Graph representations.

        Methods:
        - `dict_to_matrix(graph_dict: Dict)` return a numpy `NDArray[float64]`
        - `matrix_to_dict(adj_matrix: list[list], vertices: list` return a `dict`
    """

    def __init__(self):
        pass

    def dict_to_matrix(self, graph_dict: dict) -> NDArray[float64]:
        """
            Converts the graph representation from Dictionary (key:value) to Adjacency Matrix

            `graph_dict`: dict that represet the graph that will be converted into adjacency matrix
        """
        vertices = list(graph_dict.keys())
        vertices_quantity = len(vertices)

        graph_as_adj_matrix = np.zeros((vertices_quantity, vertices_quantity))

        for key in range(vertices_quantity):
            for value in range(vertices_quantity):
                if (vertices[key] in graph_dict and
                        vertices[value] in graph_dict[vertices[key]]):
                    graph_as_adj_matrix[key][value] = 1

        return graph_as_adj_matrix

    def matrix_to_dict(self, adj_matrix: list[list], vertices: Optional[list]) -> dict:
        """
            Converts the graph representation from Adjacency Matrix to Dictionary (key:value)

            `_adj_matrix`: Adjacency Matrix that represet the graph that will be converted into Dict
            representation {key:value}
            `_vertices`: vertices list of the graph
        """
        if vertices is None:
            for i in range(len(adj_matrix)):
                vertices.append(i)

            print('Generated vertex: ', vertices)

        graph_as_dict = {}
        vertices_quantity = len(vertices)

        for key in range(vertices_quantity):
            # `key` is the index (or vertex)
            graph_as_dict[vertices[key]] = []  # Create the vertex

            for value in range(vertices_quantity):
                # `value` is a neighbor (or relationship) of the vertex
                if adj_matrix[key][value] == 1:
                    # We append the neighbor in position [key][value]
                    # to the vertex, if in the coordinate has the value `1`.
                    graph_as_dict[vertices[key]].append(vertices[value])

        return graph_as_dict


if __name__ == '__main__':
    from tests import load_and_run_tests

    load_and_run_tests()

    # If you want to implement see the example:
