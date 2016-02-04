import unittest
from is105 import sub

class TestSub(unittest.Testcase):
    def setUp(self):
        pass
    def test_numbers_20_7(self):
        self.assertEqual(sub(20,7), 15)
        
        
if_name_=="_main_":
    unittset.main()

