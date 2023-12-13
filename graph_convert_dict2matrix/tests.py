import unittest
import numpy as np

from main import Graph


class TestConvertion(unittest.TestCase):
    """
        Test the convertion between the two representations methos of graphs: dict and adjancency
        matrix.

        We are the functions `dict_to_matrix` and `matrix_to_dict` present in the `Graph class`.
    """

    def test_convertion_dict_to_matrix(self):
        """
            Test convertion of Dict into adjacency Matrix representation.
        """
        print("\nTesting convertion of Dict to Matrix")

        adj_matrix_dict = {
            'A': ['C', 'B'],
            'B': ['A'],
            'C': []
        }

        expected_result = [
            [0, 1, 1],
            [1, 0, 0],
            [0, 0, 0],
        ]
        result = Graph().dict_to_matrix(adj_matrix_dict)

        print(f"Expected:\n {expected_result}\n\nResult:\n {result}")
        self.assertTrue(
            np.array_equal(result, expected_result),
            "The result isn't equal to the expected result."
        )

    def test_convertion_matrix_to_dict(self):
        """
            Test convertion of adjacency Matrix into Dict representation.
        """
        print("\nTesting convertion of Matrix to Dict")

        _adj_matrix = [
            [0, 1, 1],
            [1, 0, 0],
            [0, 0, 0],
        ]
        _vertices = ['A', 'B', 'C']

        # The result will be ordered from A-Z, because we are using `for` to
        # go through the vertices and it's neighbors.
        expected_result = {
            'A': ['B', 'C'],
            'B': ['A'],
            'C': []
        }
        result = Graph().matrix_to_dict(_adj_matrix, _vertices)

        print(f"Expected:\n {expected_result}\n\nResult:\n {result}")
        self.assertEqual(
            result, expected_result,
            "The result isn't equal to the expected result."
        )


def load_and_run_tests():
    """
        Load and run all the test cases.
    """
    print("Starting Unit Tests")

    test_suite = unittest.TestSuite()
    test_suite.addTests(tests=[
        TestConvertion('test_convertion_dict_to_matrix'),
        TestConvertion('test_convertion_matrix_to_dict'),
    ])

    runner = unittest.TextTestRunner()
    runner.run(test_suite)


if __name__ == '__main__':
    # unittest.main()
    load_and_run_tests()
