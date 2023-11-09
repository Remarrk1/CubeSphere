import unittest
from cubesphere.main import *


class TestCubeSphereIntersect(unittest.TestCase):

    def test_create_sphere_vertices(self):
        # Проверяем, что список вершин сферы создается правильно
        create_sphere_vertices()
        self.assertEqual(len(vertices_sphere), (slices + 1) * (stacks + 1))

    def test_create_sphere_edges(self):
        # Проверяем, что список ребер сферы создается правильно
        create_sphere_edges()
        self.assertEqual(len(edges_sphere), slices * stacks * 4)

if __name__ == '__main__':
    unittest.main()