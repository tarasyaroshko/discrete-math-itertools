import unittest
import main


class TestCalc(unittest.TestCase):

    def test_count(self):
        self.assertEqual(next(main.count(start=5, step=3)), 5)
        generator = main.count(1, 2)
        self.assertEqual(list(next(generator)
                         for _ in range(5)), [1, 3, 5, 7, 9])

    def test_product(self):
        self.assertEqual(list(main.product('ABCD', 'xy', '12')),
                         [('A', 'x', '1'), ('A', 'x', '2'), ('A', 'y', '1'),
                          ('A', 'y', '2'), ('B', 'x', '1'), ('B', 'x', '2'),
                          ('B', 'y', '1'), ('B', 'y', '2'), ('C', 'x', '1'),
                          ('C', 'x', '2'), ('C', 'y', '1'), ('C', 'y', '2'),
                          ('D', 'x', '1'), ('D', 'x', '2'), ('D', 'y', '1'),
                          ('D', 'y', '2')])
        self.assertFalse(len(tuple(main.product())) > 1)
        self.assertEqual(list(main.product(range(3))),  [(0,), (1,), (2,)])
        self.assertIn(('A', 'x'), list(main.product('ABCD', 'xy')))
        self.assertNotIn(('A', 'A'), list(main.product('ABCD', 'xy')))

    def test_permutations(self):
        self.assertEqual(list(main.permutations(range(3), 2)), [
                         (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)])
        self.assertEqual(list(main.permutations(['f', 'p', 'n'], 3)), [('f', 'p', 'n'), (
            'f', 'n', 'p'), ('p', 'f', 'n'), ('p', 'n', 'f'), ('n', 'f', 'p'), ('n', 'p', 'f')])
        self.assertTrue(('a', 'a', 'b') not in list(
            main.permutations(['a', 'b', 'c'], 3)))

    def test_combinations(self):
        self.assertEqual(tuple(main.combinations(3, 4)),
                         ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)))
        self.assertEqual(tuple(main.combinations(5, 7)), ((0, 1, 2, 3, 4), (0, 1, 2, 3, 5), (0, 1, 2, 3, 6),
                                                          (0, 1, 2, 4, 5), (0, 1, 2, 4, 6), (0, 1, 2, 5, 6), (
                                                              0, 1, 3, 4, 5), (0, 1, 3, 4, 6), (0, 1, 3, 5, 6),
                                                          (0, 1, 4, 5, 6), (0, 2, 3, 4, 5), (0, 2, 3, 4, 6), (
                                                              0, 2, 3, 5, 6), (0, 2, 4, 5, 6), (0, 3, 4, 5, 6),
                                                          (1, 2, 3, 4, 5), (1, 2, 3, 4, 6), (1, 2, 3, 5, 6), (1, 2, 4, 5, 6), (1, 3, 4, 5, 6), (2, 3, 4, 5, 6)))
        # self.assertEqual(list(main.combinations('ABCD', 2)),
        #                  [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')])

    def test_cycle(self):
        generator = main.cycle("ABC")
        self.assertTrue((list(next(generator) for _ in range(6)))
                        == ['A', 'B', 'C', 'A', 'B', 'C'])

    def test_repeat(self):
        generator = main.repeat("hello")
        self.assertTrue((list(next(generator)
                        for _ in range(3)) == ['hello', 'hello', 'hello']))

    def test_combinations_with_replacement(self):
        self.assertEqual(tuple(main.combinations_with_replacement('ABCD', 2)),
                         (('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')))
        self.assertTrue(('C', 'D') in tuple(
            main.combinations_with_replacement('ABCD', 2)))
        self.assertEqual(
            len(list(main.combinations_with_replacement('ABCD', 1))), 4)


if __name__ == "__main__":
    unittest.main()
