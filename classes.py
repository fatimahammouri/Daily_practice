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

    def __add__(self, other_fraction):
        """method adds two fractions, return result fraction"""

        result_num = self.num*other_fraction.den + other_fraction.num*self.den
        result_den = self.den * other_fraction.den
        # return Fraction(result_num, result_den)

        # after adding the helper function we can find the fraction in lowest term 
        common = gcd(result_num, result_den)
        return Fraction(result_num//common, result_den//common)


    def is_equal(self, other_function):
        """ method returns true if two fractions are equal"""

        return self.num * other_function.den == self.den * other_function.num 

    def __str__(self):
        """ Method to print Fraction object as string """

        return str(self.num) + "/" + str(self.den)



def gcd (m, n):
    """ Helper function to find greatest common divisor 
    to find the lowest term representation of a fraction"""

    while m % n != 0:
        orig_m = m
        orig_n = n

        m = orig_n
        n = orig_m % orig_n

    return n

    
# my_fraction = Fraction(1,4)
# my_fraction.show()
# other_fraction = Fraction(10, 20)
# other_fraction.show()
# print(my_fraction + other_fraction)
# print(my_fraction.is_equal(other_fraction))

# ////////////////////////////////////////////////////////////////////

""" Building a Linked List and Node """   

class Node():
    """ Node Class
        attributes:
        - data
        - next 
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    """ Linked List Class 
        attributes:
        - head 
    """
    def __init__(self):
        self.head = None

    def print_all(self):

        current = self.head
        while current != None:
            print (current.data)
            current = current.next

# ////////////////////////////////////////////////////////////////////

"""Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(data=1, next=Node(data=2, next=Node(data=3, next=Node(4))))
    >>> reverse_linked_list(ll).print_data()
    4
    3
    2
    1
""" 
class Node():
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next



def reverse_linked_list(head):
    # iterating over the llist
    # current = save the current Node
    # previousNode = save the current Node 
    # current = current.next
    # current.next = previousNode
    
    out_head = None
    current = head
    while current is not None:
        # tail = Node('A', None)
        out_head = Node(current.data, out_head)
        current = current.next

    return out_head


ll = Node(data=1, next=Node(data=2, next=Node(data=3, next=Node(4))))
ll.print_data()
print('Reversed Linked List')
reverse_linked_list(ll).print_data()