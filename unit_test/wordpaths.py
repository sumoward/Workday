# -*- coding: utf-8 -*-
"""
Unit test for word paths
"""
import unittest
from src.wordpaths import WordPath
from collections import defaultdict


class TestWordPath(unittest.TestCase):
    def setUp(self):
        """
            Setup for use in tests
        """
        self.path = "../resources/test.txt"
        self.start_word = 'cat'
        self.end_word = 'dog'
        self.test_path = WordPath(self.path, self.start_word, self.end_word)
        self.expected_graph = defaultdict(list, {'fare': ['care', 'fire'],
                                                 'feal': ['real'], 'yagi': ['yali'],
                                                 'bert': ['burt', 'berm'], 'palp': ['paup', 'pali'],
                                                 'foul': ['foud'], 'dog': ['cog'], 'pali': ['yali', 'palp'],
                                                 'jest': ['gest', 'jesu'], 'jesu': ['jehu', 'jest'], 'jehu': ['jesu'],
                                                 'germ': ['berm', 'geum'], 'pent': ['dent', 'gent', 'pint', 'peat'],
                                                 'jina': ['pina'], 'foud': ['foul'], 'pray': ['prat'],
                                                 'paup': ['plup', 'palp'],
                                                 'guna': ['gena', 'guha'], 'blup': ['plup'], 'bitt': ['butt'],
                                                 'rial': ['real'], 'carp': ['camp', 'care'], 'pint': ['pent', 'pina'],
                                                 'real': ['feal', 'rial'], 'geez': ['geet'], 'fire': ['fare', 'fike'],
                                                 'peat': ['prat', 'pent'], 'dung': ['dunt'],
                                                 'geet': ['gent', 'gest', 'geez'],
                                                 'meum': ['geum'], 'burt': ['bert', 'butt'], 'cat': ['cot'],
                                                 'butt': ['bitt', 'burt'], 'berm': ['germ', 'bert', 'germ', 'bert'],
                                                 'fike': ['fire'], 'guha': ['guna'], 'dunt': ['dent', 'dung'],
                                                 'cot': ['cat', 'cog'], 'geum': ['meum', 'germ'],
                                                 'gent': ['dent', 'pent', 'geet', 'gest', 'gena', 'dent', 'pent',
                                                          'geet', 'gest', 'gena'],
                                                 'camp': ['carp'], 'prat': ['peat', 'pray'],
                                                 'dent': ['gent', 'pent', 'dunt'],
                                                 'cog': ['dog', 'cot', 'dog', 'cot'], 'plup': ['blup', 'paup'],
                                                 'gest': ['jest', 'geet', 'gent'], 'yali': ['pali', 'yagi'],
                                                 'pina': ['jina', 'pint'],
                                                 'care': ['fare', 'carp'], 'gena': ['guna', 'gent']})

    def test_are_valid_words(self):
        """
            Check if words are found in the supplied dictionary
        """
        self.assertTrue(self.test_path.are_valid_words())
        self.test_path.start_word = 'xxxxxxxx'
        self.assertFalse(self.test_path.are_valid_words())

    def test_no_path_given(self):
        """
        Check handling of  an invalid path
        """
        # xxxx.txt does not exist
        path = "../resources/XXXX.txt"
        start_word = 'cat'
        end_word = 'dog'
        test_path = WordPath(path, start_word, end_word)
        # only the start word is returned
        self.assertEqual(test_path.__str__() , 'cat')


def test_create_graph(self):
    """
        Test that we can create a graph from a dictionary
    """

    self.assertEqual(self.test_path.graph, self.expected_graph)


def test_search_graph(self):
    """
       Test that we can search a graph
    """
    self.test_path.graph = self.expected_graph
    self.assertEqual(self.test_path.paths, [['cat', 'cot', 'cog', 'dog']])


def test_main(self):
    """
    test the expected paths are generated for the start_word and end_word

    """
    test_data = ['cat -> cot -> cog -> dog',
                 'pint -> pent -> peat -> prat -> pray',
                 'fire -> fare -> care -> carp -> camp']

    for test in test_data:
        seperate = test.split()
        start_word = seperate[0]
        end_word = seperate[-1]
        expected = WordPath(self.path, start_word, end_word)
        self.assertEqual(expected.__str__(), test)

    # test identical start and end words
    expected = WordPath(self.path, 'cat', 'cat')
    self.assertEqual(expected.__str__(), 'cat')
    # test words not in dict
    expected = WordPath(self.path, 'xxxxx', 'yyyyy')
    self.assertEqual(expected.__str__(), 'xxxxx')


if __name__ == '__main__':
    unittest.main()
