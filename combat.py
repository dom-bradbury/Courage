def rps():

	import random

	health = 100
	enemy_health = 100

	while health > 0 and enemy_health > 0:
		print ("Your health: %s.  Enemy health: %s" % (health, enemy_health))
		actions = ['rock','paper','scissors']
		print ('Choices:')
		for i in actions: print ("%s, " % i),
		your_action = input("\n> ")
		enemy_action = actions[random.randint(0,2)]
		
		if your_action == enemy_action:
			print ("draw")
			continue
		
		if (your_action == 'rock' and enemy_action == 'scissors') \
		or (your_action == 'paper' and enemy_action == 'rock') \
		or (your_action == 'scissors' and enemy_action == 'paper'):
			print ("win")
			enemy_health -= 30
			continue
			
		if (your_action == 'paper' and enemy_action == 'scissors') \
		or (your_action == 'scissors' and enemy_action == 'rock') \
		or (your_action == 'rock' and enemy_action == 'paper'):
			print ("lose")
			health -= 30
			
	if health < enemy_health:
		print ("You lost")
		return 1
	else:
		print ("You win")
		return 2