import sys

t = open(sys.argv[1] + '_tests.py', 'w')

t.write('import unittest\n')
t.write('from {} import *\n\n'.format(sys.argv[1]))
t.write('class TestCases(unittest.TestCase):\n')
t.write('   def test_1(self):\n')
t.write('      pass\n\n')
t.write("if __name__ == '__main__':\n")
t.write('   unittest.main()')

t.close()
