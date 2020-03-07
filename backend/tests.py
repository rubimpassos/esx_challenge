from unittest import TestCase, main

from backend.core import balanced_brackets, two_sum, best_transaction_profit, retained_water


class BackendTest(TestCase):
    def test_two_sum(self):
        self.assertListEqual([0, 1], two_sum([2, 7, 11, 15], 9))
        self.assertListEqual([1, 2], two_sum([2, 7, 1, 15], 8))
        self.assertListEqual([0, 2], two_sum([3, 5, 2, 10], 5))
        self.assertListEqual([2, 3], two_sum([11, 12, 2, 10], 12))

        with self.assertRaises(ValueError) as ex:
            two_sum([4, 5, 2, 10], 5)

        self.assertEqual('No two sum solution', str(ex.exception))

    def test_balanced_brackets(self):
        self.assertEqual('Sim', balanced_brackets('{}'))
        self.assertEqual('Sim', balanced_brackets('()'))
        self.assertEqual('Sim', balanced_brackets('[]'))
        self.assertEqual('Não', balanced_brackets('}}'))
        self.assertEqual('Não', balanced_brackets(']]'))
        self.assertEqual('Não', balanced_brackets('))'))
        self.assertEqual('Não', balanced_brackets('{{'))
        self.assertEqual('Não', balanced_brackets('[['))
        self.assertEqual('Não', balanced_brackets('(('))
        self.assertEqual('Não', balanced_brackets('(]'))
        self.assertEqual('Não', balanced_brackets('(((((((()'))
        self.assertEqual('Sim', balanced_brackets('(((([()]))))'))
        self.assertEqual('Sim', balanced_brackets('()()()()'))
        self.assertEqual('Sim', balanced_brackets('(({}(())))'))

    def test_best_transaction_profit(self):
        self.assertEqual(5, best_transaction_profit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(6, best_transaction_profit([1, 7, 5, 3, 6, 4]))
        self.assertEqual(0, best_transaction_profit([7, 6, 4, 3, 1]))

    def test_retained_water(self):
        self.assertEqual(6, retained_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(14, retained_water([3, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(5, retained_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 1]))


if __name__ == '__main__':
    main()
