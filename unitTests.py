### unit tests ###

import unittest

class Testing(unittest.TestCase):
    
    def test_input(self):
        
        # test if string length of int > 5 raises an error
        assertFalse(verifyInput(1234567890))
        
        # test if input throws error if string
        assertFalse(verifyInput("hippo123"))
        
        # test if input throws error if list
        assertFalse(verifyInput([1, 2, 3]))


