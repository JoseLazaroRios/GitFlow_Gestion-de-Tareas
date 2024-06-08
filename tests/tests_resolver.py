import unittest

from resolver import GitFlow_GestionarTareas
class TestSolveQuadratic(unittest.TestCase):

    def test_two_real_roots(self):
        root1, root2 = unittest(1, -3, 2)
        self.assertAlmostEqual(root1, 2)
        self.assertAlmostEqual(root2, 1)

    def test_one_real_root(self):
        root1, root2 = unittest(1, -2, 1)
        self.assertAlmostEqual(root1, 1)
        self.assertAlmostEqual(root2, 1)

    def test_no_real_roots(self):
        root1, root2 = unittest(1, 0, 1)
        self.assertIsNone(root1)
        self.assertIsNone(root2)

    def test_not_quadratic(self):
        with self.assertRaises(ValueError):
            unittest(0, 2, 1)

if __name__ == '__main__':
    unittest.main()
