import unittest

def sort(lst1,lst2):
    """функция для нахождения общих элементов в массивах"""

    counter = 0

    if len(lst1) > len(lst2):
        for i in range(len(lst2)):
            if lst2[i] in lst1:
                counter += 1
    else:
        for i in range(len(lst1)):
            if lst1[i] in lst2:
                counter += 1
    return counter


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        lst1 = [1, 2, 3]
        lst2 = [1]
        self.assertEqual(1, sort(lst1, lst2))

    def test_2(self):
        lst1 = [-1, -2, -3]
        lst2 = [1]
        self.assertEqual(0, sort(lst1, lst2))

    def test_3(self):
        lst1 = [72, 523, -3, 432, 432, -312, 12, 13]
        lst2 = [1, 12, 2, 72, 3]
        self.assertEqual(2, sort(lst1, lst2))



if __name__ == '__main__':
    unittest.main()