import openerp.tests.common as test_common

class TestExample(test_common.TransactionCase):

    def setUp(self):
        pass

    def test_00_example(self):
        self.assertEqual(1, 2)
