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
    def __init__(self, start=0):
        """creating new generator and initiating a start value"""
        self.start = self.next = start

    def __repr__(self):
        """showing reprsentation of function"""
        return f"<SerialGenerator start={self.start} next ={self.next}"

    def generate(self):
        """incrementing self and returning next num"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """reset serial to original start num"""
        self.next = self.start