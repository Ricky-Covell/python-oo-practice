"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, num=0):
        '''Makes a new Serial Generator starting at "num" and saves initial num argument for reset'''

        self.num = num
        self.initialNum = num

    def __repr__(self):
        '''Show representation'''

        return f"SerialGenerator num: {self.num}   initialNum = {self.initialNum}"

    def generate(self):
        '''Returns next serial number '''

        currentNum = self.num
        self.num += 1
        return currentNum
    
    def reset(self):
        '''Resets generator to initial num'''

        self.num = self.initialNum


