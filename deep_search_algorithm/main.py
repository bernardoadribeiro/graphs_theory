class Graph():
    """
        graph example:
        ```python
            {
                'A' = []
            }
        ```
    """

    def __init__(self, _graph: dict) -> None:
        self.graph = _graph
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        pass


class DeepSearch():
    """ Class with methods to make Deep Search in a Graph.
        Graph must be in `dict` format.
    """

    def __init__(self) -> None:
        self.visited_vertices = {}
        self.count = 0

    def _start_visited_vertices(self, graph: dict) -> dict:
        """ Returns a dict of the visited vertices. The initial value for all vertices is `-1`
            Args:
                `graph` (dict):
        """
        visited = {}
        for vertex in graph:
            visited[vertex] = -1
        return visited

    def dfs_base_search(
        self,
        graph: dict,
        initial_vertex,
        visited_vertices: dict,
        count: int = 0
    ) -> int:
        """
            Base function to search for vertices in a graph represented with dictionary.

            Args:
                `graph` (dict): A dictionary of the graph.\n
                `vertices` (list): A list of vertices. \n
                `visited_vertices` (dict): A dict with all visited vertices \
                with it's count. If not visited, the value is -1. \n
                `count` (int): Optional, default is 0. The initial value of the counter. \n
        """

        count += 1

        visited_vertices[initial_vertex] = count
        print(f'{count}: {visited_vertices}')

        for i in graph[initial_vertex]:
            if visited_vertices[i] == -1:
                count = self.dfs_base_search(graph, i, visited_vertices, count)

        # just to show the visited vertices and count after
        self.visited_vertices = visited_vertices
        self.count = count

        return count

    def dfs_search():
        pass


if __name__ == '__main__':
    deep_search = DeepSearch()

    _graph = {
        'A': ['B', 'C', 'D', 'H'],
        'B': ['A', 'E'],
        'C': ['A', 'D', 'E', 'F', 'G'],
        'D': ['A', 'C'],
        'E': ['B', 'C'],
        'F': ['C', 'G'],
        'G': ['C', 'F'],
        'H': ['A'],
    }

    _visited_vertices = deep_search._start_visited_vertices(_graph)

    deep_search.dfs_base_search(_graph, 'B', _visited_vertices)
    print(f'Count: {deep_search.count} \nVisited: {deep_search.visited_vertices}')
