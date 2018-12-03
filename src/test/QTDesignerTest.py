import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

import unittest

class QTDesignerTest(unittest.TestCase):

    def setUp(self):
        print(':: setUp() ::')

    def tearDown(self):
        print(':: tearDown() ::')

    def test_visualization(self):
        print(':: test_visualization() ::')
        