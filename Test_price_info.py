import unittest
import price_info as pi

def test_total_cost_shipping():
    result = 0.0
    result = pi.total_cost_shopping()
    assert (result == 46.75)

def test_cost_of_fruits():
    result = 0
    fruit = "apple"
    quantity = 3
    result = pi.cost_of_fruits(fruit, quantity)
    assert(round(result) == 4)

if __name__ == '__main__':
    unittest.main()
