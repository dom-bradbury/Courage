from sys import exit
import combat

class Scene(object):
	
	def enter(self):
		print ("This scene hasn't been written yet")
		return Bar()

class Choice(object):

	def __init__(self, possible_answers, responses):
		self.possible_answers = possible_answers
		self.responses = responses
		
	def choice(self):
	
		p_a_index = range(0,len(self.possible_answers)) # possible answer index list
		p_a_nums = list(map(str,range(1,len(self.possible_answers)+1)))
	
		while True:
		
			for i in p_a_index:
				print ("%d: %s" % (i+1, self.possible_answers[i]))
		
			answer = input("> ")
			
			if answer not in self.possible_answers + p_a_nums:
				print (self.responses[-1])
				continue
		
			for i in p_a_index:
			
				if answer == self.possible_answers[i] or answer == p_a_nums[i]:
					print (self.responses[i])
					break
					
			return i + 1
			break
			
class Death(Scene):
		
	def enter(self):
		print ("You died.")
		return Bar()
		
class Boring(Scene):

	def enter(self):
		print ("You were never cut out to be a hero.")
		print ("You do nothing noteworthy for the rest of your life and you die")
		print ("unsatisfied and alone.")
		return Bar()

class Bar(Scene):

	def enter(self):
		print ("You enter a bar")
		print ("What do you do?")
		
		possible_answers = ['order lager','order grog', 'spit at bartender']
		responses = ['Boring!',
		'The drink of a true adventurer! There\'s someone I think you should meet.',
		'Death!',
		'This isn\'t that kind of bar. Think again']
	
		path = Choice(possible_answers, responses).choice()
		if path == 1: return Boring()
		if path == 2: return Mystic()
		if path == 3: return Death()		
		
class Mystic(Scene):

	def enter(self):
		print ("There is an old mysterious woman. She looks unimaginably old.") 
		print ("It is said she can read peoples futures.")
		print ("She asks you: \"Tell me child, what path do you seek?\"")
		
		possible_answers = ["path of peace.","path of truth","path of honour"]
		responses = ["Ah, perhaps you should grow a pair and pick up a sword?",
		"Truth you seek, I can give you all of the truth. Look into my crystal ball. Look deeper.",
		"Yes! A noble warrior I see inside of you. \nTake this gem to the Blacksmith, and say the words: \n\"Dawn rises, The Dark retreats, The Light shall shine again,\"",
		"The path you seek is not what I see for you. Choose again."]
		
		path = Choice(possible_answers, responses).choice()
		if path == 1: return Boring()
		if path == 3: return Blacksmith()
		if path == 2: return Death()
		
class Blacksmith(Scene):

	def enter(self):
		print ("You enter a blacksmith")
		print ("Inside is a drunk old man")
		print ("What do you say?")
		
		possible_answers = ['Dawn rises, The Dark retreats, The Light shall shine again',
		'Uh.. Corn rises, The Bark depletes, The Kite shall shine again?',
		'You stink of piss and booze, you\'re a disgusting old man, what use could you be to me?']
		responses = ["Is that? No! It can\'t be!\nThe lost ruby from the Mighty Sword of Kanazin",
		'Can\'t you see I\'m busy, piss off!',
		'Death!',
		'You\'re talking bollocks mate!']
	
		path = Choice(possible_answers, responses).choice()
		if path == 1: return Battle()
		if path == 2: return Boring()
		if path == 3: return Death()
		
class Battle(Scene):

	def enter(self):
		print ("You here the sound of horses in the town square.")
		print ("You here the sound of screaming and terror and death")
		print ("What do you do?")
		
		possible_answers = ['Hide','Charge through the door with your mighty sword']
		responses = ['You survive, but hundreds of innocent people died because you failed to save them',
		'You charge through the door and scream \"Behold! The Mighty Sword of Kanazin!!!\"',
		'Stop dillydallying, this is the most important decision of your life']
		
		path = Choice(possible_answers, responses).choice()
		if path == 2: pass
		if path == 1: return Boring()
		
		print ("You are quickly surrounded by marauding villains")
		print ("They are terrifying, wicked and blood-thirsty.")
		print ("What do you do?")
		
		possible_answers = ['Swing your mighty sword in one foul swoop']
		responses = ['The Mighty Sword decapitates all of the villains, their heads roll across the square, blood pools at your feet.',
		'Are you really a hero? There\'s only one real choice!']
		
		path = Choice(possible_answers, responses).choice()
		if path == 1: pass
		
		print ("The leader approaches, he is fully clad in jet black armour, darker than the night itself")
		print ("He says \"Your puny sword will do nothing to me, no man can slay the mighty Black Knight\"")
		print ("What do you do?")
		possible_answers = ['Swing your Mighty Sword anyway', 'Walk away', 'Challenge him to a game of Rock Paper Scissors']
		responses = ['The sword bounces off his armour, he crushes your skull in his hand', 'He laughs, and kills everyone you ever loved', 'The Dark Knight never refuses a duel', 'Choose again']
		
		path = Choice(possible_answers, responses).choice()
		if path == 1: return Death()
		if path == 2: return Boring()
		if path == 3: pass
		
		print ("You say: \"Let's make this more interesting\"")
		print ("\"Lose 4 times and you die\"")
		result = combat.rps()
		
		if result == 1: return Death()
		if result == 2: pass
		
		print ("You win the game")
		exit(0)
		
		
		
class Engine(object):

	def __init__(self, scene):
		self.scene = scene
		
	def play(self):
		
		current_scene = self.scene
		
		while True:
		
			new_scene = current_scene.enter()
			current_scene = new_scene
		
		
		
scene = Bar()
game = Engine(scene)
game.play()