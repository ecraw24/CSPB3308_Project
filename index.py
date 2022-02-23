
#Just some prototypes for functions that might be used

import sqlite3

### For the index of categories page ###

#fn gets passed in a connection to a DB (should the connection get passed in or something else or nothing?)
def get_categories(category_DB):
	c = category_DB.cursor()
	lst = []
	for entity in c.execute("SELECT name FROM Categories;"):
		print(entity)	##obv will not print out the name, will store it somewhere to use
		lst.append(entity)	##for an HTML link/button,
					##but not sure how to do that/too lazy to figure
	return lst
			

### For the home page ###

def list_featured_categories(category_DB):
	c = category_DB.cursor()
	lst = []
	for entity in c.execute("SELECT name FROM Categories GROUP BY num_entries LIMIT 3;"):
		#this loop should get the names of the top 3 categories with the most entries
	
		print(entity)	##obv will not print out the name, will store it somewhere to use
		lst.append(entity)	##for an HTML link/button, 
					##but not sure how to do that/too lazy to figure it out
	return lst
	
		
