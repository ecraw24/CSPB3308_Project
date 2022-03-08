
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

### Verify correct input type and length on "Enter Information" page ###
def verifyInput(resultInput):
    
    if(not isInstance(resultInput, (int, float)) | len(str(resultInput)) > 5):
        raise ValueError("Incorrect Input Format: Enter a number")
    else: 
        print("Input accepted.")


### Populate the display list
### this needs alotta work
def filldisplay(skill_list, curr_skill, display_list):
	if(display_list[0] == 0):
		i = 0
		while skill_list[curr_skill] != skill_list[-3] and i < 4:
			display_list[i] = skill_list[curr_skill]
			i+=1
			curr_skill+=1
	else:
		while skill_list[curr_skill] != skill_list[-3]:
			display_list[0] = display_list[1]
			display_list[1] = display_list[2]
			display_list[2] = display_list[3]
			display_list[3] = skill_list[curr_skill]
			curr_skill+=1
		if skill_list[curr_skill] == skill_list[-3]:
			curr_skill = 0
			display_list[0] = skill_list[-1]
			display_list[1] = skill_list[2]
			display_list[2] = skill_list[3]


