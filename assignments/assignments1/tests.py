from task1 import allocate
from task2 import fun
from task3 import areas
from task4 import table
#from task5 import string


import unittest

class TestAssignmentOne(unittest.TestCase):



    def test_fun(self):
        self.assertEqual(fun('mobile'), 'mbl')
        self.assertEqual(fun('MOBILE'), 'MBL')
        self.assertEqual(fun('MobIlE'), 'Mbl')

    def test_allocate(self):
        self.assertEqual(allocate('This is javaScript','i'), [2,5,15])


    def test_table(self):
        self.assertEqual(table(3), [[1],[2,4],[3,6,9]])



    def test_string(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        self.assertEqual(string(l1), d1)




    # def test_areas(self):
    #     self.assertEqual(area("r", 2), "4.0")
    #     self.assertEqual(area("t", 2, 3), "3.0")
    #     self.assertEqual(area("c", 2), "12.56")
    #     self.assertEqual(area("r", 2, 5), "10.0")

if __name__ == '__main__':
    unittest.main()
