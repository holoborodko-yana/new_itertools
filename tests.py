import new_itertools as ni
import unittest


class TestCount(unittest.TestCase):
    def test_integer(self):
        '''
        Tests count function with integer numbers.
        '''
        check = ni.count(10, 2)
        current = []
        element = next(check)
        while len(current) != 5:
            current.append(element)
            element = next(check)
        result = current
        self.assertEqual(result, [10, 12, 14, 16, 18])

    def test_float(self):
        '''
        Test count function with float numbers.
        '''
        check = ni.count(5.5, 1.5)
        current = []
        element = next(check)
        while len(current) != 5:
            current.append(element)
            element = next(check)
        result = current
        self.assertEqual(result, [5.5, 7.0, 8.5, 10.0, 11.5])


class TestCycle(unittest.TestCase):

    def test_str(self):
        """
        Test that the function can cycle objects given in string.
        """
        check = ni.cycle('abcd')
        current = []
        element = next(check)
        while current.count(element) != 2:
            current.append(element)
            element = next(check)
        result = current

        self.assertEqual(result, ['a', 'b', 'c', 'd',
                                  'a', 'b', 'c', 'd'])

    def test_list(self):
        """
        Test that the function can cycle objects given in list.
        """
        check = ni.cycle([1, 2, 3, 4])
        current = []
        element = next(check)
        while current.count(element) != 2:
            current.append(element)
            element = next(check)
        result = current

        self.assertEqual(result, [1, 2, 3, 4,
                                  1, 2, 3, 4])

    def test_impossible_1(self):
        """
        Test that the function can't cycle an object with lenght less than 1.
        """

        result = list(ni.cycle(''))
        self.assertEqual(result, [])

    def test_impossible_2(self):
        """
        Test that the function can't cycle an object with lenght less than 1.
        """
        result = list(ni.cycle(123))
        self.assertEqual(result, [])


class TestRepeat(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(list(ni.repeat(2, 5)), [2, 2, 2, 2, 2])
        self.assertEqual(list(ni.repeat("ABBA", 4)),
                         ["ABBA", "ABBA", "ABBA", "ABBA"])
        self.assertEqual(list(ni.repeat(0, 0)), [])


class TestProduct(unittest.TestCase):

    def test_str(self):
        """
        Test that the function can combinate str.
        """
        generator = ni.product('abc', 'xy')
        result = [line for line in generator]

        self.assertEqual(result, [('a', 'x'),
                                  ('a', 'y'),
                                  ('b', 'x'),
                                  ('b', 'y'),
                                  ('c', 'x'),
                                  ('c', 'y')])

    def test_list(self):
        """
        Test that the function can combinate lists.
        """
        generator = ni.product(['a', 'b', 'c'], ['x', 'y'])
        result = [line for line in generator]

        self.assertEqual(result, [('a', 'x'),
                                  ('a', 'y'),
                                  ('b', 'x'),
                                  ('b', 'y'),
                                  ('c', 'x'),
                                  ('c', 'y')])

    def test_three(self):
        '''
        test that the function can find cartesian product of more than two sets
        '''
        generator = ni.product('abc', 'xy', '12')
        result = [line for line in generator]
        self.assertEqual(result, [('a', 'x', '1'),
                                  ('a', 'x', '2'),
                                  ('a', 'y', '1'),
                                  ('a', 'y', '2'),
                                  ('b', 'x', '1'),
                                  ('b', 'x', '2'),
                                  ('b', 'y', '1'),
                                  ('b', 'y', '2'),
                                  ('c', 'x', '1'),
                                  ('c', 'x', '2'),
                                  ('c', 'y', '1'),
                                  ('c', 'y', '2')])


class TestPermutations(unittest.TestCase):

    def test_str(self):
        """
        Test that the function can permutate str.
        """
        iterable = 'ABC'
        length = 2
        generator = ni.permutations(iterable, length)
        result = [line for line in generator]

        self.assertEqual(result, [('A', 'B'), ('A', 'C'),
                                  ('B', 'A'), ('B', 'C'),
                                  ('C', 'A'), ('C', 'B')])

    def test_int(self):
        """
        Test that the function can permutate numbers.
        """
        iterable = range(2)
        length = 2
        generator = ni.permutations(iterable, length)
        result = [line for line in generator]

        self.assertEqual(result, [(0, 1), (1, 0)])

    def test_impossible(self):
        """
        Test that the function can't permutate iterable with 
        length > len(iterable).
        """
        iterable = range(3)
        length = 5
        generator = ni.permutations(iterable, length)
        result = [line for line in generator]

        self.assertEqual(result, [])


class TestCombinations(unittest.TestCase):

    def test_str(self):
        """
        Test that the function can combinate str.
        """
        n = 'ABC'
        r = 2
        generator = ni.combinations(n, r)
        result = [line for line in generator]

        self.assertEqual(result, [('A', 'B'), ('A', 'C'), ('B', 'C')])

    def test_int(self):
        """
        Test that the function can combinate numbers.
        """
        n = range(4)
        r = 3
        generator = ni.combinations(n, r)
        result = [line for line in generator]

        self.assertEqual(result, [(0, 1, 2), (0, 1, 3),
                                  (0, 2, 3), (1, 2, 3)])

    def test_impossible(self):
        """
        Test that the function can't combinate iterable with
        n > len(iterable).
        """
        n = range(3)
        r = 5
        generator = ni.combinations(n, r)
        result = [line for line in generator]

        self.assertEqual(result, [])


class TestCombination_with_replacement(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(list(ni.combinations_with_replacement("ABCD", 2)),
                         [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'),
                          ('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')])
        self.assertEqual(list(ni.combinations_with_replacement("KL", 4)),
                         [('K', 'K', 'K', 'K'), ('K', 'K', 'K', 'L'), ('K', 'K', 'L', 'L'),
                          ('K', 'L', 'L', 'L'), ('L', 'L', 'L', 'L')])
        self.assertEqual(
            list(ni.combinations_with_replacement("ABCD", 0)), [()])
        self.assertEqual(
            list(ni.combinations_with_replacement("ABCD", -6)), [()])


if __name__ == '__main__':
    unittest.main()
