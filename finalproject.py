'''this fun game will help you decide what to have for dinner or any other meal.'''

def music_choice():
	print " "
 	print "1 - Rolling in the Deep by Adele"
 	print "2 - Born in the USA by Bruce Springstein"
 	print "3 - The Schulyer Sisters by Hamilton Broadway Cast"
 	print "4 - Hotline Bling by Drake"
 	print "5 - Stranger Things soundtrack"
 	choice = int(raw_input("What music should be playing while you eat?"))
 	print " "
 	if choice >= 6:
 		print "that is not a valid choice"
 		return choice == music_choice()
 	else:
 		return choice

def drink_choice():
	print " "
	print "1 - Gin martini stirred with a twist"
	print "2 - Mojito"
	print "3 - A beer with a shot of bourbon on the side"
	print "4 - Fresh lime margarita"
	print "5 - A glass of Pinot Noir"
	choice = int(raw_input("Whats your favorite cocktail to have before dinner?"))
	print " "
 	if choice >= 6:
 		print "that is not a valid choice"
 		return choice == drink_choice()
 	else:
 		return choice

def eatstyle_choice():
	print " "
	print "1 - Normal...whatever that is"
	print "2 - Bird-like"
	print "3 - Like a wild animal"
	print "4 - Sophiscated"
	choice = int(raw_input("How would you describe your eating style?"))
	print " "
 	if choice >= 5:
 		print "that is not a valid choice"
 		return choice == eatstyle_choice()
 	else:
 		return choice

def spice_choice():
	print " "
	print "1 - Not hot at all"
	print "2 - Ooh, thats got a little kick!"
	print "3 - My mouth is on fire!"
	print "4 - I'm happy with whatever happens"
	choice = int(raw_input("How spicy do you want it?"))
	print " "
 	if choice >= 5:
 		print "that is not a valid choice"
 		return choice == spice_choice()
 	else:
 		return choice

def time_choice():
	print " "
	print "1 - I had a sensible, healthy lunch"
	print "2 - I haven't eaten yet today and I'm hangry about it"
	print "3 - I'm a little peckish"
	print "4 - I had a bad day and just ate a pint of chocolate ice cream, but lets have dinner"
	choice = int(raw_input("When did you last eat?"))
	print " "
 	if choice >= 5:
 		print "that is not a valid choice"
 		return choice == time_choice()
 	else:
 		return choice

def utensils_choice():
	print " "
	print "1 - A steak knife"
	print "2 - My hands"
	print "3 - Chopsticks"
	print "4 - Umm, a fork duh"
	choice = int(raw_input("What kind of utensils do you want to use?"))
	print " "
 	if choice >= 5:
 		print "that is not a valid choice"
 		return choice == utensils_choice()
 	else:
 		return choice

def style():
	print " "
	print "1 - Healthy" 
	print "2 - Farm to table artistic creations"
	print "3 - Dessert"
	print "4 - Balanced and with many condiments"
	print "5 - Deep-fried"
	choice = int(raw_input("All foods should really be what?"))
	print " "
 	if choice >= 6:
 		print "that is not a valid choice"
 		return choice == style()
 	else:
 		return choice

def final_answer():
	print " "
	print "1 - Cook"
	print "2 - Delivery"
	choice = int(raw_input("Are you going to cook or get something delivered?"))
	return choice
	print " "


def main():
	print " "
	print "This is a fun game that will tell you what to have for dinner."
	print "Ready?"
	print "Let's go!"
	print " "
	print " "
	total_score = 0

 	choice = music_choice()
 	total_score = total_score + choice

 	choice = time_choice()
 	total_score = total_score + choice

 	choice = utensils_choice()
 	total_score = total_score + choice

 	choice = drink_choice()
 	total_score = total_score + choice

 	choice = spice_choice()
 	total_score = total_score + choice
 	
 	choice = eatstyle_choice()
 	total_score = total_score + choice

 	choice = style()
 	total_score = total_score + choice
 	
 	choice = final_answer()

 	if choice == 1 and total_score <=10:
 		print "For dinner you should have a comforting bowl of soup. Here's a recipe: https://smittenkitchen.com/2015/09/broccoli-cheddar-soup/"
 		
	elif choice == 1 and total_score >=11 and total_score <=14:
 		print "You should have shrimp with roasted squash. Make this: http://www.marthastewart.com/313375/roasted-shrimp-with-spaghetti-squash"
 		
 	elif choice == 1 and total_score >=15 and total_score <=19:
 		print "You should roast some chicken with figs. Try making this: http://www.thekitchn.com/recipe-balsamic-mustard-glazed-chicken-thighs-and-figs-234132"

	elif choice == 1 and total_score >=20 and total_score <=24:
 		print "Its pizza night! Here's a recipe: https://smittenkitchen.com/2013/10/lazy-pizza-dough-favorite-margarita-pizza/"

 	elif choice == 1 and total_score >=25 and total_score <=29:
 		print "Doesn't steak and veggies dound delicious? Make this: http://www.thekitchn.com/recipe-sheet-pan-steak-and-veggies-235973"

 	elif choice == 1 and total_score >=30 and total_score <=34:	
 		print "You need brain food: Make this: http://www.thekitchn.com/recipe-green-curry-braised-salmon-231077"

 	elif choice == 1 and total_score >=35 and total_score <=39:
 		print "You should try something new with chicken. Make this: https://smittenkitchen.com/2016/09/piri-piri-chicken/"

 	elif choice == 1 and total_score >=40 and total_score <=45:
 		print "You should get your Italian on. Make this: https://smittenkitchen.com/2016/01/spaghetti-pie-with-pecorino-and-black-pepper/"


 	if choice == 2 and total_score <=10:
 		print "You should get Korean BBQ short ribs from Han Il Kwan: https://postmates.com/sf/han-il-kwan-san-francisco"

 	elif choice == 2 and total_score >=11 and total_score <=14:
 		print "You should have pho from Turtle Tower: https://postmates.com/sf/turtle-tower-restaurant-san-francisco"

 	elif choice == 2 and total_score >=15 and total_score <=19:
 		print "Is there anything better than ribs and burgers? No. Get some 4505: https://postmates.com/sf/4505-burgers-bbq-san-francisco-2"

	elif choice == 2 and total_score >=20 and total_score <=24:
 		print "It's pizza night! Go Chicago style: https://www.patxispizza.com"

 	elif choice == 2 and total_score >=25 and total_score <=29:
 		print "Cambodian food is amazingly delicious. Get it now: https://www.trycaviar.com/san-francisco/angkor-borei-2753"

 	elif choice == 2 and total_score >=30 and total_score <=34:	
 		print "Treat yo self, House of Prime Rib style: https://postmates.com/sf/house-of-prime-rib-san-francisco"

 	elif choice == 2 and total_score >=35 and total_score <=39:
 		print "You should try some authentic Thai food. https://www.trycaviar.com/san-francisco/lers-ros-thai--mission-1897"

 	elif choice == 2 and total_score >=40 and total_score <=45:
 		print "You should get your Italian on with 54 Mint: https://www.trycaviar.com/san-francisco/54-mint-ristorante-2065"
 	

if __name__ == '__main__':
 	main()