import random


def spin_wheel():
	"""
	Randomnly picks 3 objects from the dictionary, analogous to spinning a wheel with 
	"""
	result = []
	options = { 1 : 'heart', 2 : 'spade' , 3 : 'diamond' , 4: 'club' , 5: 'crown', 6 : 'anchor' }

	for i in range(3):
		value = random.randint(1,6)
		result.append(options[value])

	return result


def money_won(bets,result):
	
	for k in range(len(bets)):
		if result[0] == result[1] == result[2]== 'anchor'==bets[k][5]:
			print("Player " + str(k) +" CISC 121 - Winner on Anchors")
			exit()


	total_money = [0,0,0,0,0,0]
	profit_money = [0,0,0,0,0,0]


	options = { 1 : 'heart', 2 : 'spade' , 3 : 'diamond' , 4: 'club' , 5: 'crown', 6 : 'anchor' }	
	#options = { 'heart' : 1,  'spade' : 2 ,  'diamond' : 3 , 'club' : 4 , 'crown' : 5, 'anchor' : 6 }
	
	for i in range(len(bets)):
		my_list = bets[i]

		for j in range(1,7):
			count = 0

			if my_list[j-1]>0:

				
				if options[j] == result[0]:
					count +=1
				if options[j] == result[1]:
					count +=1
				if options[j] == result[2]:
					count +=1


				total_money[i] += count*my_list[j-1] + my_list[j-1]
				profit_money[i] += count*my_list[j-1]

		print("Player "+ str(i) +" won "+ str(profit_money[i]))

	return total_money		



def check_player_money(total_current_money, money_earned):
	for i in range(len(total_current_money)):
		if total_current_money[i] == 0 && money_earned[i] ==0:
			print("Player "+ i+ " is not eligible to play anymore")
