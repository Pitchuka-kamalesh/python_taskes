import unittest


def add(a, b):

    return a + b


def letter(driver):
    output = []
    for i,data in enumerate(driver):
        if data.isupper():
            output.append(i)
    return output


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4,5), 9)
        self.assertEqual(add(-1,-5),-6)
        self.assertEqual(add(-1,8),7)

    def test_letter(self):
        print("this is letter test case")
        self.assertEqual(letter("KaMaL"),[0,2,4])
        self.assertEqual(letter("Happy Birthday"),[0,6])
        self.assertFalse(letter("kaMal") != [2])
        self.assertTrue(letter("kaMal") == [2])


if __name__ == '__main__':
    unittest.main()
