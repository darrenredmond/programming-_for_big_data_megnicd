#Megan McDonnell, 10354513

#importing math functions for sin,cos,tan,sqrt
import math

#creating class calculator
class Calculator(object):

#function1 - add 2 numbers
    def add(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
 
#function2 - subtract 2 numbers 
    def subtract(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError  
            
#function3 - divide two numbers and guard for zero division errors
    def divide(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            if y == 0:
                return 'Dividing by zero has no meaning'
            return x / float(y)
        else:
            raise ValueError
            
#function4 - divide two numbers and guard for zero division errors            
    def multiply(self, x, y):
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError  
            
#function5 - exponent that takes two parameters so you can sqr, cube etc.
    def exponent(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x ** y
        else:
            raise ValueError
            
#function6 - take one parameter and !, guarding for 0 entries

    def factorial(self, x):
        number_types = (int)
        if isinstance(x, number_types):
            if x == 0 or x < 0:
                return 'Cannot perform factorial function on 0 or negative numbers'
            return math.factorial(x)
        else:
            raise ValueError   
            
#function7 - return sqrt of a single parameter, guard against negatives
    def sqrt(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            if x < 0:
                return 'Cannot get sqrt of a negative number'
            return math.sqrt(x)
        else:
            raise ValueError
                                      
# function8 - get the cos of an angle, converting to radians so correct result is returned
# also guarding for entries less than 0 and greater than 360 degrees                                
    def cos(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            if x > 360 or x < 0:    
                return 'Input must be in range 0 - 360'
            return math.cos(math.radians(x))
        else:
            raise ValueError
                                        
#function9 - get the sin of an angle, converting to radians so correct result is returned
#also guarding for entries less than 0 and greater than 360 degrees              
    def sin(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            if x > 360 or x < 0:    
                return 'Input must be in range 0 - 360'
            return math.sin(math.radians(x))
        else:
            raise ValueError
            
#function10 - get the tan of an angle, converting to radians so correct result is returned
#also guarding for entries less than 0 and greater than 360 degrees
    def tan(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            if x > 360 or x < 0:    
                return 'Input must be in range 0 - 360'
            return math.tan(math.radians(x))
        else:
            raise ValueError        
            
			
			

