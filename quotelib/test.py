

# to run all tests:
# $ cd <quotelib dir>
# $ python -m unittest


import unittest

import quotelib

class TestQuote(unittest.TestCase):

    def test_contains_any_false(self):
        self.assertEqual(quotelib._contains_any('Mains, William, Gary', 'zx;\n\t-{}|ASDF'), False)

    def test_contains_any_true(self):
        self.assertEqual(quotelib._contains_any('Mains, William, Gary', 'zx;\n\t-{}|ASDF '), True)
    
    def test_already_quoted_true(self):
        self.assertEqual(quotelib._already_quoted('"Steve"'), True)

    def test_already_quoted_contains_quotechar(self):
        self.assertEqual(quotelib._already_quoted('"Octo\"pus"'), False)

    def test_already_quoted_true(self):
        self.assertEqual(quotelib._already_quoted('Steve'), False)

    def test_dumbquote(self):
        self.assertEqual(quotelib._dumbquote('hunger'), "'hunger'", True)

    def test_shlex_spaces(self):
        self.assertEqual(quotelib.quote('some text'), '\'some text\'')

    def test_noshlex_spaces(self):
        self.assertEqual(quotelib.quote('some text', use_shlex=False, always=False), "'some text'")      

    def test_shlex_numbers(self):
        self.assertEqual(quotelib.quote(1922), '1922')
    
    def test_noshlex_numbers(self):
        self.assertEqual(quotelib.quote(1922.01, use_shlex=False), '1922.01')      
    

if __name__ == '__main__':
    unittest.main()

