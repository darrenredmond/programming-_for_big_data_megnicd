#Megan McDonnell, 10354513

from calculator import *
import unittest

#creating test class and instantiating
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

#test1 for function1, add: 2+2=4, 2+4=6, 2+(-2)=0, 4+2.5=6.5
    def test_add_function(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)
        result = self.calc.add(4, 2.5)
        self.assertEqual(6.5, result)
        
#test2 for function2, add: 2-2=0, 2-4=-2, 2-(-4)=6, 4-2.5=1.5       
    def test_sub_function(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)

#test3 for function3, divide: 2/2=1 4/2=2, 2/-2=-1, 2/4=0.5, 2/0=no meaning
    def test_div_function(self):
        result = self.calc.divide(2, 2)
        self.assertEqual(1, result)
        result = self.calc.divide(4,2)
        self.assertEqual(2, result)
        result = self.calc.divide(2, -2)
        self.assertEqual(-1, result)
        result = self.calc.divide(2, 4)
        self.assertEqual(0.5, result)
        result = self.calc.divide(2, 0)
        self.assertEqual('Dividing by zero has no meaning', result)
        
#test4 for function4, multiply: 2*2=4, 2*4=8, 2*(-2)=-4, 2-0=0, (-2)*(-2)=4,2*2.5=5
    def test_prod_function(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2,4)
        self.assertEqual(8, result)
        result = self.calc.multiply(2, -2)
        self.assertEqual(-4, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)
        result = self.calc.multiply(-2, -2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2, 2.5)
        self.assertEqual(5, result)        

#test5 for function5, exponent: 2**2=4, 2**4=16, 2**-2=0.25, 2**0=1
    def test_exponent_function(self):
        result = self.calc.exponent(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(2,4)
        self.assertEqual(16, result)
        result = self.calc.exponent(2, -2)
        self.assertEqual(0.25, result)
        result = self.calc.exponent(2, 0)
        self.assertEqual(1, result)
        
#test6 for function6, factorial: 5!-120, 6!=720
    def test_factorial_function(self):
        result = self.calc.factorial(5)
        self.assertEqual(120, result)
        result = self.calc.factorial(6)
        self.assertEqual(720, result)
        result = self.calc.factorial(0)
        self.assertEqual('Cannot perform factorial function on 0 or negative numbers', result)
        result = self.calc.factorial(-2)
        self.assertEqual('Cannot perform factorial function on 0 or negative numbers', result)

#test7 for function7, sqrt: rt4=2, rt16=4, rt110~10.448
    def test_sqrt_function(self):
        result = self.calc.sqrt(4)
        self.assertEqual(2, result)
        result = self.calc.sqrt(16)
        self.assertEqual(4, result)
        result = self.calc.sqrt(110)
        self.assertAlmostEqual(10.488088481,result)
        result = self.calc.sqrt(-5)
        self.assertEqual('Cannot get sqrt of a negative number',result)
        
#test8 for function9, cos
    def test_cos_function(self):
        result = self.calc.cos(120)
        self.assertAlmostEqual(-0.5,result)
        result = self.calc.cos(270)
        self.assertAlmostEqual(0, result)  
        result = self.calc.cos(45)
        self.assertAlmostEqual(0.70710678, result)  
        result = self.calc.cos(100)
        self.assertAlmostEqual(-0.173648177, result)  
        result = self.calc.cos(375)
        self.assertAlmostEqual('Input must be in range 0 - 360', result) 
        
#test9 for function9, sin
    def test_sin_function(self):
        result = self.calc.sin(120)
        self.assertAlmostEqual(0.866025403, result)
        result = self.calc.sin(55)
        self.assertAlmostEqual(0.819152044, result)  
        result = self.calc.sin(45)
        self.assertAlmostEqual(0.707106781, result)  
        result = self.calc.sin(180)
        self.assertAlmostEqual(0, result)  
        result = self.calc.sin(375)
        self.assertAlmostEqual('Input must be in range 0 - 360', result)  
        
#test10 for function9, tan
    def test_tan_function(self):
        result = self.calc.tan(180)
        self.assertAlmostEqual(0,result) 
        result = self.calc.tan(45)
        self.assertAlmostEqual(1, result)  
        result = self.calc.tan(75)
        self.assertAlmostEqual(3.73205080, result)  
        result = self.calc.tan(-54)
        self.assertAlmostEqual('Input must be in range 0 - 360', result)     
                                         
if __name__ == '__main__':
    unittest.main()