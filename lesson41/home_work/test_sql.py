import unittest
from task_home_work import *


class SQLTestCase(unittest.TestCase):

    def setUp(self):
        self.engine = engine
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def test_task1(self):
        response = task1()
        self.assertEqual(task1(), response)

    def test_task1_is_instance(self):
        response = task1()
        self.assertIsInstance(response, list)

    def test_task1_type_error(self):
        with self.assertRaises(TypeError):
            task1('David')

    def test_task8_on_success(self):
        self.assertEqual(task8(), [('Susan Mavris', 6500, 'London')])
