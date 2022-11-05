import base64
import unittest

from main import etapa1, etapa2, etapa3


class MyTestCase(unittest.TestCase):
    def test_etapa1(self):
        self.assertEqual(37, etapa1(1234))
        self.assertEqual(156, etapa1(7878))
        self.assertEqual(60, etapa1(2346))
        self.assertEqual(18, etapa1(531))
        self.assertEqual(15, etapa1(69))
        self.assertEqual(2, etapa1(2))
        self.assertEqual(39, etapa1(int(base64.b64decode('MjM2MQ=='))))
        self.assertEqual(67, etapa1(int(base64.b64decode('OTQxOA=='))))

    def test_etapa2(self):
        self.assertEqual([2], etapa2([1, 1]))
        self.assertEqual([5, 6], etapa2([4, 3, 2, 7, 8, 2, 3, 1]))
        self.assertEqual([7, 8], etapa2([1, 6, 4, 5, 6, 2, 3, 4]))
        self.assertEqual([8, 9, 11, 13, 14], etapa2([1, 6, 4, 5, 6, 2, 3, 4, 7, 10, 12, 2, 4, 5]))

    def test_etapa3(self):
        self.assertTrue(etapa3('abba'))
        self.assertTrue(etapa3('aaaa'))
        self.assertFalse(etapa3('abbbb'))
        self.assertFalse(etapa3('ababa'))
        self.assertTrue(etapa3('ababababcccc'))
        self.assertFalse(etapa3(base64.b64decode('YWJhYmFiY3Njc2NzYXM=')))
        self.assertTrue(etapa3(base64.b64decode('YWJhYmFiYWJjY2NjZGRkZA==')))


if __name__ == '__main__':
    unittest.main()
