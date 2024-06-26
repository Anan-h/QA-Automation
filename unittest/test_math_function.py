import unittest
from math_function import modulo_func, is_even, is_odd, sum_function, sub_function, mul_function, div_function


class TestMathFunction(unittest.TestCase):

    def test_modulo_func(self):
        number=4
        result=modulo_func(number)
        return self.assertEqual(0,result,"The function doesn't work as expected !")

    def test_is_even_true(self):
        number=4
        result=is_even(number)
        return self.assertTrue(True,result)

    def test_is_even_false(self):
        number = 3
        result = is_even(number)
        return self.assertFalse(False, result)

    def test_is_odd_true(self):
        number = 3
        result = is_odd(number)
        return self.assertTrue(True, result)

    def test_is_odd_false(self):
        number = 4
        result = is_odd(number)
        return self.assertFalse(False, result)

    def test_sum_function(self):
        num_a=3
        num_b=4
        result=sum_function(num_a,num_b)
        return self.assertEqual(result,7)

    def test_sub_function(self):
        num_a = 4
        num_b = 3
        result = sub_function(num_a, num_b)
        return self.assertEqual(result,1)

    def test_mul_function(self):
        num_a = 3
        num_b = 4
        result = mul_function(num_a, num_b)
        return self.assertEqual(result,12)

    def test_div_function(self):
        num_a = 12
        num_b = 4
        result = div_function(num_a, num_b)
        return self.assertEqual(result,3)