#functions for picking random ship positions
from random import randint

def random_orientation():
    return randint(0,1)

def determ_ship_space(length,size):
    poss_ship_space=[]
    orient=random_orientation()
    if orient==0:
        for x in range(size):
            poss_ship_space.append(["@"]*(size-length+1))
    else:
        for x in range((size-length+1)):
            poss_ship_space.append(["@"]*size)
    start_row=random_row(poss_ship_space)
    start_col=random_col(poss_ship_space)
    
    ship_space=[]
    for i in range(length):
        if orient==0:
            ship_space.append([start_row,start_col+i])
        if orient==1:
            ship_space.append([start_row+i,start_col])
    return ship_space
            

def random_row(ship_space):
    return randint(0, len(ship_space) - 1)

def random_col(ship_space):
    return randint(0, len(ship_space[0]) - 1)
	
def convert_to_tuple_array(array_of_list_pairs):
	temp=[]
	for pair in array_of_list_pairs:
		temp.append(tuple(pair));
	return temp
	
def convert_to_array_array(array_of_tuples):
	temp=[]
	for pair in array_of_tuples:
		temp.append(list(pair));
	return temp
	
def place_n_ships(length,size,no_ships):
	ship_spaces=[]; #ship_spaces is the place where all the selected ships and their addresses wait
	level_counter=[0]*no_ships; #intialize the counter for each level
	total_count=0; #intialize the total count
	ship_index=0; #the ship index is the current level of the search tree where the full depth is no_ships
	
	while True:
		print(total_count)
		level_counter[ship_index]+=1;
		total_count+=1;
		#randomly pick a ship placement for ship
		ship_space_guess=determ_ship_space(length,size);
		ship_space_guess=convert_to_tuple_array(ship_space_guess);
		all_ship_spaces=sum(ship_spaces,[]);
	
		
		#check if it fits
		if set(ship_space_guess).isdisjoint(all_ship_spaces):
			#add to list and move to next ship
			ship_spaces.append(ship_space_guess);
			if ship_index == no_ships-1:
				break
			else:
				ship_index+=1;
		else:
			if total_count>=10000:
				print("total count exceeded")
				break
			if level_counter[ship_index]>=100:
				level_counter[ship_index]=0;
				ship_index-=1;
				ship_spaces.pop(ship_index);
	
					
		#if not, try again
	return convert_to_array_array(ship_spaces)
	