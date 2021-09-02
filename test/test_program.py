import unittest
import sys
sys.path.append('code')

import program

class uTest(unittest.TestCase):
        def test_run(self):
                self.assertEqual(program.number(3), 'Weird')
                self.assertEqual(program.number(24), 'Not Weird')
                self.assertEqual(program.number(4), 'Not Weird')
                self.assertEqual(program.number(18), 'Weird')
                self.assertEqual(program.number(20), 'Weird')

if __name__ == '__main__':
        unittest.main()
