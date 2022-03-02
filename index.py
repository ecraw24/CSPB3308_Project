
#Just some prototypes for functions that might be used

import sqlite3

### For the index of categories page ###

#fn gets passed in a connection to a DB (should the connection get passed in or something else or nothing?)
def get_categories(category_DB):
	conn = sqlite3.connect(category_DB)
	c = conn.cursor()
	lst = []
	for entity in c.execute("SELECT name FROM Categories;"):
		lst.append(entity[0])	#items are returned as tuples for sqlite3

	conn.close()
	return lst
			

### For the home page ###

def list_featured_categories(category_DB):
	conn = sqlite3.connect(category_DB)
	c = conn.cursor()
	lst = []
	for entity in c.execute("SELECT name FROM Categories GROUP BY num_entries LIMIT 3;"):
		#this loop should get the names of the top 3 categories with the most entries/data points
	
		lst.append(entity[0])	#items are returned as tuples for sqlite	 
	conn.close()
	return lst
	
		
