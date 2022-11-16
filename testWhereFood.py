import io
import unittest
from unittest import mock


class TestWhereFood(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_prints_from_restaurant_list(self, mock_stdout):
        import whereFood
        self.assertIn(mock_stdout.getvalue().strip(), whereFood.restaurants)


if __name__ == '__main__':
    unittest.main()