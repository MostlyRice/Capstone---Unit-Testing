import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario
    def test_list_of_less_than_three_prices(self):
        prices = [10,4]
        expected_discount = None
        self.assertIsNone(expected_discount, discount(prices))
    
    def test_list_of_strings(self):
        prices = ['item1','item2','item3']
        expected_discount = None
        self.assertIsNone(expected_discount, discount(prices))
    
    def test_list_of_more_than_three_prices(self):
        prices = [80, 55, 78, 99, 67]
        expected_discount = 55
        self.assertEqual(expected_discount, discount(prices))
    
    def test_list_of_mixed_data(self):
        prices = [35, 'item1', 'apple', 67]
        expected_discount = None
        self.assertIsNone(expected_discount, discount(prices))
    
    def test_list_if_negative_prices(self):
        prices = [33, -7, 9, -1, 6]
        with self.assertRaises(ValueError):
            discount(prices)
    
    def test_if_list_of_same_min_prices(self):
        prices = [15, 5, 5, 5]
        expected_discount = 5
        self.assertEqual(expected_discount, discount(prices))

if __name__ == '__main__':
    unittest.main()