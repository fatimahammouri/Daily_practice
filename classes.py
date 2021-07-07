class Fraction:
    """ implementing a fraction class 
        attributes:
        - numerator: any integer
        - denominator: any integer > 0
    """

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def show(self):
        """ method to show the Fraction object """
        
        print(self.num, "/", self.den)

    def add(self, other_fraction):
        """method adds two fractions, return result fraction"""

        result_num = self.num * other_fraction.den + other_fraction.num * self.den
        result_den = self.den * other_fraction.den
        return Fraction(result_num, result_den)
    
my_fraction = Fraction(5,10)
my_fraction.show()