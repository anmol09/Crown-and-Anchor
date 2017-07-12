import random



def spin_wheel():
	result = []
	options = { 1 : 'heart', 2 : 'spade' , 3 : 'diamond' , 4: 'club' , 5: 'crown', 6 : 'anchor' }

	for i in range(3):
		value = random.randint(1,6)
		result.append(options[value])

	return result

