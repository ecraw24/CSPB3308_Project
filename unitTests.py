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

class HomePageTesting(unittest.TestCase):
#Testing subclass specific to the homepage and its related functions

	#connects to the database
	def setup(self):
		self.dbname = "AmIAverage"
		self.db = sqlite3.connect(self.dbname)
		self.c = self.db.cursor()

	#since home page will not be altering database, no need to commit any changes to it
	def teardown(self):
		self.db.close()

	#unit test to test the get_categories() function
	def test_get_categories(self):

		#unsure if there is a better way to test, since this is the same query from the function
		cats = self.c.execute("SELECT name FROM Categories;")
		i = 0

		for name in get_categories(self.dbname):
			assertEqual(name, cats[i][0], "Error:\nExpected: {}\nActual: {}".format(cats[i][0], name))


