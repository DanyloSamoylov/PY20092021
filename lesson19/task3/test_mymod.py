import unittest
import mymod


class MymodTest(unittest.TestCase):

    def setUp(self):
        self.test = mymod.test

    def test_result(self):
        with open('text.txt', 'w') as file:
            file.write('12345\n12345!')
            self.assertEqual(self.test('text.txt'), '2 lines, 12 chars in text.txt')

    def tearDown(self) -> None:
        pass

