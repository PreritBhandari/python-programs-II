"""
Write an if statement to determine whether a variable holding a year
is a leap year.
"""
import unittest

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

class testLeapYear(unittest.TestCase):
    def test_div_by_4(self):
        self.assertEqual(leap_year(2020),True) #divisible by 4 and not by 100
        self.assertEqual(leap_year(2200),False)#divisible by 4 and also by 100
    def test_div_by_100(self):
        self.assertEqual(leap_year(2100),False) #divisible by 4 and also by 100
        self.assertNotEqual(leap_year(2000),False) #2000 is leap year---->assert not equal 
    def test_div_by_400(self):
        self.assertEqual(leap_year(2400),True)#though non divisble 100 but divisible by 400 is always leap year

if __name__ == "__main__":
    
    year=int(input('Enter Year'))
    if leap_year(year):
        print (f'{year} is leapyear')
    else:
        print (f'{year} is not leapyear')
    unittest.main()
    

    
