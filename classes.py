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
    
my_fraction = Fraction(5,10)
my_fraction.show()