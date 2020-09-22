from random import uniform
from random import randint
import time
from random import shuffle
from datetime import datetime, timedelta
import random
import sys
import functools

w = "w"
a = "a"
d = "d"
s = "s"

def die(dice1,dice2):
	while True:
		dice = input(f"Press 'roll' to roll the dice (from {dice1} to {dice2}) ")
		if dice.lower() == "roll":
			dice_roll = randint(dice1,dice2)
			print (f"You rolled a {dice_roll}!")
			return dice_roll
import random
import sys
import copy


fight = False
attack_first = ""

letter = [" "," "," "," "] 
for k in range(17):
	letter.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWYZ"))
letter.append("   ")


#Puzzle1:
import random
letter = [" "," "," "," "] 
for k in range(14):
	letter.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWYZ"))
ny_liste = ["A","B","C"]
for k in ny_liste:
	letter.append(k)
for k in [" "," "," "]:
	letter.append(k)

def note1():
	print(" ----------------")
	print("|                |")
	print("|                |")
	print("|2, 4, 1, 6, 7, 0|")
	print("|                |")
	print("|                |")
	print(" ----------------")

def note2():
	print(" ----------------")
	print("| Z 1 D          |")
	print("|   R            |")
	print("|                |")
	print("|               A|")
	print("|             Q 2|")
	print(" ----------------")


def ground(letters):
	end = " -----"
	middle = "|━━━━━|"
	print("     ")
	print(end)
	print(f"|{letters[3]}|{letters[4]}|{letters[5]}|")
	print(middle)
	print(f"|{letters[6]}|{letters[7]}|{letters[8]}|")
	print(middle)
	print(f"|{letters[9]}|{letters[10]}|{letters[11]}|")
	print(middle)
	print(f"|{letters[12]}|{letters[13]}|{letters[14]}|")
	print(middle)
	print(f"|{letters[15]}|{letters[16]}|{letters[17]}|")
	print(middle)
	print(f"|{letters[18]}|{letters[19]}|{letters[20]}|")
	print(end)
	print("    ")

def puzzle1():
	nr1 = 2
	nr2 = 4
	nr3 = 1
	nr4 = 6
	nr5 = 7
	nr6 = 0
	nr1_n = 1
	nr2_n = 0
	nr3_n = 0
	nr4_n = 0
	nr5_n = 0
	nr6_n = 0
	ground(letter)
	#first:
	letter_copy = letter.copy()
	a = ""
	while a!= str(letter[18]) and a!= str(letter[19]) and a!= str(letter[20]):
		a = input(f"{letter[18]}/{letter[19]}/{letter[20]} or show note (n) ")
		if a.upper() == "N":
			note1()
		elif a == letter[18]:
			letter_copy[18] = "X"
		elif a == letter[19]:
			letter_copy[19] = "X"
		elif a == letter[20]:
			letter_copy[20] = "X"
		else:
			print_slow("unknown move, try again\n")
	print(ground(letter_copy))
	#second:
	letter_copy2 = letter.copy()
	remove_X = letter_copy.index("X")
	while True: 
		a = input("w/a/s/d or show note(n)")
		if a.upper() == "N":
			note1()
		elif a.lower() == "w":
			if nr1_n < nr1:
				print_slow("As you are about to move forward, a wall comes up and blocks you")
			else:
				letter_copy2[remove_X-3] = "X"
				break
		elif a.lower() == "a" and remove_X != 3 and remove_X != 6 and remove_X != 9 and remove_X != 12 and remove_X !=15 and remove_X !=18:
			letter_copy2[remove_X-1] = "X"
			nr1_n += 1
			break
		elif a.lower() == "d" and remove_X != 5 and remove_X != 8 and remove_X != 11 and remove_X != 14 and remove_X !=17 and remove_X !=20:
			letter_copy2[remove_X+1] = "X"
			nr1_n += 1
			break
		else:
			print("unknown move, try again")
	print(ground(letter_copy2))
	#rest:
	
	while letter_copy2[0] != "X" and letter_copy2[1] != "X" and letter_copy2[2] != "X": 
		remove_X = letter_copy2.index("X")
		letter_copy2 = letter.copy()
		while True:  
			a = input("w/a/s/d or show note(n)")
			if a.upper() == "N":
				note1()
			elif a == "w":
				print(remove_X)
				if (remove_X == 18 or remove_X == 19 or remove_X == 20) and (nr1_n < nr1): 
					print_slow("As you are about to move forward, a wall comes up and blocks you")
				elif (remove_X == 15 or remove_X == 16 or remove_X == 17) and (nr2_n < nr2):
					print_slow("As you are about to move forward, a wall comes up and blocks you")
				elif (remove_X == 12 or remove_X == 13 or remove_X == 14) and (nr3_n < nr3):
					print_slow("As you are about to move forward, a wall comes up and blocks you")
				elif (remove_X == 9 or remove_X == 10 or remove_X == 11) and (nr4_n < nr4):
					print_slow("As you are about to move forward, a wall comes up and blocks you")
				elif (remove_X == 6 or remove_X == 7 or remove_X == 8) and (nr5_n < nr5):
					print_slow("As you are about to move forward, a wall comes up and blocks you")
				elif (remove_X == 4 or remove_X == 5) and (nr6_n < nr6):
					print_slow("As you are about to move forward, a wall comes up and blocks you")
				else:
					letter_copy2[remove_X-3] = "X"
					break
			elif a.lower() == "a" and remove_X != 3 and remove_X != 6 and remove_X != 9 and remove_X != 12 and remove_X !=15 and remove_X !=18:
				letter_copy2[remove_X-1] = "X"
				break
			elif a.lower() == "d" and remove_X != 5 and remove_X != 8 and remove_X != 11 and remove_X != 14 and remove_X !=17 and remove_X !=20:
				letter_copy2[remove_X+1] = "X"
				break
			elif a == "s":
				letter_copy2[remove_X+3] = "X"
				break
			else:
				print("unknown move, try again")  
		print(ground(letter_copy2))
		
		if "X" in letter_copy2[18:21]:
			nr1_n +=1
			if nr1_n > nr1:
				print_slow("A small stone drops from the ceiling and hit your head.\n")
				class1.lose_hp(5)
		elif "X" in letter_copy2[15:18]:
			nr2_n +=1
			if nr2_n > nr2:
				print_slow("You feel spikes from underneath barely piercing your feet.\n")
				class1.lose_hp(6)
		elif "X" in letter_copy2[12:15]:
			nr3_n +=1
			if nr3_n > nr3:
				print_slow("A bunch of smaller stones drop from the ceiling, hitting your head and shoulders.\n")
				class1.lose_hp(7)
		elif "X" in letter_copy2[9:12]:
			nr4_n +=1
			if nr4_n > nr4:
				print_slow("A bunch of snakes drop from the ceiling. They bite you, but you manage to throw them off within not too long.\n")
				print_slow("It doesn't seem like they are poisonous, but it hurts either way.\n")
				class1.lose_hp(8)
		elif "X" in letter_copy2[6:9]:
			nr5_n +=1
			if nr5_n > nr5:
				print_slow("A wooden thing shoots out from the wall and hit you in the stomach.\n")
				class1.lose_hp(9)
		elif "X" in letter_copy2[4:6]:
			nr6_n +=1
			if nr6_n > nr6:
				print_slow("An arrow shoots out of the wall. it hits you in the leg.\n")
				class1.lose_hp(10)  
	print_slow("You made it past the puzzle.\n")

#puzzle2:
def note2():
	print(" ----------------")
	print("| Z 1 D          |")
	print("|   R            |")
	print("|                |")
	print("|               A|")
	print("|             Q 2|")
	print(" ----------------")

letter2 = {"D":["","D","W","H","C","A","Q"], "F":["","F","Z","G","V","H","T"], "G":["","G","R","R","B","Q","F"], "H":["","H","D","D","A","F","G"], "J":["","J","Y","Z","M","P","R"], "Q":["","Q","J","X","K","O","E"]}
def ground2(letters):
	end = " -----------"
	print("     ")
	print(end)
	print(f"|{letter2['D'][1]}|{letter2['F'][1]}|{letter2['G'][1]}|{letter2['H'][1]}|{letter2['J'][1]}|{letter2['Q'][1]}|")
	print(f"|{letter2['D'][2]}|{letter2['F'][2]}|{letter2['G'][2]}|{letter2['H'][2]}|{letter2['J'][2]}|{letter2['Q'][2]}|")
	print(f"|{letter2['D'][3]}|{letter2['F'][3]}|{letter2['G'][3]}|{letter2['H'][3]}|{letter2['J'][3]}|{letter2['Q'][3]}|")
	print(f"|{letter2['D'][4]}|{letter2['F'][4]}|{letter2['G'][4]}|{letter2['H'][4]}|{letter2['J'][4]}|{letter2['Q'][4]}|")
	print(f"|{letter2['D'][5]}|{letter2['F'][5]}|{letter2['G'][5]}|{letter2['H'][5]}|{letter2['J'][5]}|{letter2['Q'][5]}|")
	print(f"|{letter2['D'][6]}|{letter2['F'][6]}|{letter2['G'][6]}|{letter2['H'][6]}|{letter2['J'][6]}|{letter2['Q'][6]}|")
	print(end)
	print("    ")

def puzzle2(number1,number2):
	a1column = ""

	#number1
	print(ground2(letter2))
	while a1column != "1" and a1column != "2" and a1column != "3" and a1column != "4" and a1column != "5" and a1column != "6":
		a1column = input(f"Which column would you like to put the {number1} in (1/2/3/4/5/6) - or do you want to see the note (n) ")
		if a1column.lower() == "n":
			note2()
	a1row = ""
	while a1row != "1" and a1row != "2" and a1row != "3" and a1row != "4" and a1row != "5" and a1row != "6":
		a1row = input(f"Which row would you like to put the {number1} in (1/2/3/4/5/6) - or do you want to see the note (n) ")
		if a1row.lower() == "n":
			note2()
	if a1column == "1":
		letter2_copy['D'][int(a1row)] = number1
		print(letter2_copy['D'][int(a1row)])
		print (ground2(letter2_copy))

	elif a1column == "2":
		letter2_copy['F'][int(a1row)] = number1
		print(letter2_copy['F'][int(a1row)])
		print (ground2(letter2_copy))

	elif a1column == "3":
		letter2_copy['G'][int(a1row)] = number1
		print(letter2_copy['G'][int(a1row)])
		print (ground2(letter2_copy))

	elif a1column == "4":
		letter2_copy['H'][int(a1row)] = number1
		print(letter2_copy['H'][int(a1row)])
		print (ground2(letter2_copy))

	elif a1column == "5":
		letter2_copy['J'][int(a1row)] = number1
		print(letter2_copy['J'][int(a1row)])
		print (ground2(letter2_copy))

	elif a1column == "6":
		letter2_copy['Q'][int(a1row)] = number1
		print(letter2_copy['Q'][int(a1row)])
		print (ground2(letter2_copy))


	#number2
	a1row = ""
	while a1row != "1" and a1row != "2" and a1row != "3" and a1row != "4" and a1row != "5" and a1row != "6":
		a1row = input(f"Which row would you like to put the {number2} in (1/2/3/4/5/6) - or do you want to see the note (n) ")
		if a1row.lower() == "n":
			note2()
	a1column = ""
	while a1column != "1" and a1column != "2" and a1column != "3" and a1column != "4" and a1column != "5" and a1column != "6":
		a1column = input(f"Which column would you like to put the {number2} in (1/2/3/4/5/6) - or do you want to see the note (n) ")
		if a1column.lower() == "n":
			note2()
	if a1row == "1":
		letter2_copy['D'][int(a1column)] = number2
		print(letter2_copy['D'][int(a1column)])
		print (ground2(letter2_copy))

	elif a1row == "2":
		letter2_copy['F'][int(a1column)] = number2
		print(letter2_copy['F'][int(a1column)])
		print (ground2(letter2_copy))

	elif a1row == "3":
		letter2_copy['G'][int(a1column)] = number2
		print(letter2_copy['G'][int(a1column)])
		print (ground2(letter2_copy))

	elif a1row == "4":
		letter2_copy['H'][int(a1column)] = number2
		print(letter2_copy['H'][int(a1column)])
		print (ground2(letter2_copy))

	elif a1row == "5":
		letter2_copy['J'][int(a1column)] = number2
		print(letter2_copy['J'][int(a1column)])
		print (ground2(letter2_copy))

	elif a1row == "6":
		letter2_copy['Q'][int(a1column)] = number2
		print(letter2_copy['Q'][int(a1column)])
		print (ground2(letter2_copy))
	#Check right or wrong
	if letter2_copy['G'][2] == 1 and letter2_copy['H'][5] == 2:
		return True
	else:
		print("That didn't do anything...\n")
		print("Looks like that wasn't right. You remove the two bricks and start again.\n")

def die(dice1,dice2):
	while True:
		dice = input(f"Press 'roll' to roll the dice (from {dice1} to {dice2}) ")
		if dice.lower() == "roll":
			dice_roll = randint(dice1,dice2)
			print (f"You rolled a {dice_roll}!")
			return dice_roll



class Player():
	mana_required = 0
	hp_regen_rate = 10
	mana_regen_rate = 0
	def __init__(self,name):
		self.name = name.capitalize()
		self.hp = 1
		self.maxhp = 1
		self.rage = 0
		self.maxrage = 0	
		self.mana = 0
		self.maxmana = 0
		self.spellpower = 0
		#0
		self.xp = 0
		self.level = 1
		self.nextlevel = 50
		self.flee_skill = 0
	def lose_hp(self,amount):
		if self.hp > amount:
			self.hp -= amount
			print_slow (f"You lose {amount} hp. You now have {self.hp} hp" + "\n")
		else:
			print_slow(f"You lose {self.hp} hp. You now have 0 hp" + "\n")
			print_slow("You are dead")
			sys.exit()
	def earn_xp(self,enemy):
		xp_gained = randint(enemy.minxp,enemy.maxxp)
		if self.xp + xp_gained >= self.nextlevel:
			xp_gaining = xp_gained
			while self.xp != self.nextlevel:
				self.xp += 1
				xp_gaining -= 1
			self.level += 1
			self.nextlevel = 50 * self.level
			print_slow (f"You gain {xp_gained} xp from killing the {enemy.name}.\n")
			print_slow (f"Level up! You are now level {self.level}.\n")
			print_slow("you have regained some of your stats, and increased your max stats slightly.\n")
			self.maxhp += 10
			self.hp = self.maxhp
			print_slow(f"Your max health has permantly increased by 10 and is now at {self.maxhp} hp.\n")
			print_slow("You also regain all your health\n")
			input("...")
			if self.rage == 0: #mage
				self.maxmana += 10
				self.mana = self.maxmana
				print_slow(f"Your maxmana has permantly increased by 10. It is now at {self.maxmana}\n")
				print_slow("You also regain all your mana\n")
			elif self.mana == 0:
				self.maxrage = float(0.92 * self.maxrage)
				print_slow (f"You now only require {int(self.maxrage)} to have full rage and do double damage\n")
			input("...")
			self.xp = 0
			self.xp += xp_gaining
			print_slow(f"You have {self.xp} xp, and need {round(self.nextlevel - self.xp)} xp to reach level {self.level+1}\n")
		else:
			self.xp += xp_gained
			print_slow (f"You gain {xp_gained} xp from killing the {enemy.name}. You now have {self.xp} xp and need {round(self.nextlevel - self.xp)} xp to reach level {self.level+1}\n")

		
	def attack(self, enemy):
		print(f"you have attacked {enemy.name}")
		#print (f"You have {self.hp} health")
		fight = True
		return fight
	def flee(self,enemy):
		num = randint(1,4-self.flee_skill)
		if num == 1:
			print("you have succesfully fled")
			return False
		else:
			print(f"You failed to flee. {enemy.name} attacks you" + "\n")
	def check_death(self):
		if self.hp <= 0:
			print("You now have 0 health")
			print ("You are dead")
			global fight
			fight = False
			global playing
			playing = False
			return fight, playing
	def check_kill(self,enemy):
		if enemy.hp > 0:
			print(f"{enemy.name} now has {round(enemy.hp)} health")
		else:
			print(f"the {enemy.name} now has 0 health")
			print (f"You have killed {enemy.name}")
			fight = False
			return fight
	def check_only_kill(self,enemy): #for minotaur
		if enemy.hp <= 0:
			print(f"the {enemy.name} now has 0 health")
			print (f"You have killed {enemy.name}")
			fight = False
			return fight
	def regen_after_fight(self):
		hphp = 0
		if attack_first != 0:
			while self.hp < self.maxhp and hphp < self.hp_regen_rate:
				hphp += 1
			else:
				self.hp += 	hphp
			input("...")
			print_slow(f"you have regained {hphp} hp, and you now have {round(self.hp)} hp in total" + "\n")
		#only mage
		if self.mana != 0 and attack_first != 0:
			manamana = 0
			while self.mana < self.maxmana and manamana < self.mana_regen_rate:
				manamana += 1
			else:
				self.mana += manamana
			print_slow(f"you have regained {manamana} mana, and you now have {self.mana} mana in total\n")
class Mage(Player):
	what_class = "Mage"
	mana_required_fireball = 25
	mana_regen_rate = 30
	fire_dmg = 0
	mana_required_ice_spike = 15
	def __init__(self,name):
		Player.__init__(self,name)
		self.name = name
		self.hp = 300
		self.maxhp = 300
		self.mana = 200
		self.maxmana = 200
		self.spellpower = 1.4
		self.rage = 0
		if self.mana < 0:
			self.mana = 0

	def lose_hp(self,amount):
		return Player.lose_hp(self,amount)
	def earn_xp(self,enemy):
		return Player.earn_xp(self,enemy)
	def lose_mana(self,amount):
		if self.mana > amount:
			self.mana -= amount
			print_slow (f"You lose {amount} mana. You now have {self.mana} mana" + "\n")
		else:
			print_slow(f"You lose {self.mana} mana. You now have 0 mana" + "\n")
	def fireball(self, enemy):
		if self.fire_dmg != 0:
			dot = random.uniform(1.2 * self.spellpower, 2.1* self.spellpower)
			enemy.hp -= dot
			print (f"*{enemy.name} is on fire*")
			print (f"{enemy.name} loses {round(dot)} damage from burning")
			self.fire_dmg -= 1
		if self.mana >= self.mana_required_fireball:
			dmg = round(random.uniform(10 * self.spellpower,12*1.2*self.spellpower))
			self.mana -= self.mana_required_fireball
			enemy.hp -= dmg
			print(f"You damage the {enemy.name} with fireball")
			print(f"you deal {round(dmg)} damage")
			burn_dmg_randint = randint(1,7)
			if burn_dmg_randint == 1:
				self.fire_dmg += 1
				print_slow (f"You set {enemy.name} on fire. (low burn)" + "\n")
			elif burn_dmg_randint == 2:
				self.fire_dmg += 2
				print_slow (f"You set {enemy.name} on fire. (medium burn)" + "\n")
			elif burn_dmg_randint == 3:
				self.fire_dmg += 3
				print_slow (f"You set {enemy.name} on fire. (high burn)" + "\n")

			if randint(1,4) == 1:
				selfdmg = round(0.25 * dmg)
				self.hp -= selfdmg
				print_slow (f"Your spell backfires and hurt you as well. You lose {round(selfdmg)} hp, but manages to put out the fire before it gets too bad" + "\n")
		if self.mana < 0:
			print("You have 0 mana left" + "\n")	
		else:
			print(f"You have {self.mana} mana left" + "\n")
	def ice_spike(self,enemy):
		if self.mana >= self.mana_required_ice_spike:
			dmg = round(random.uniform(6 * self.spellpower,9*1.15*self.spellpower))
			self.mana -= self.mana_required_ice_spike
			enemy.hp -= dmg
			print(f"You damage the {enemy.name} with ice spike")
			print(f"you deal {round(dmg)} damage")
		if self.mana < 0:
			print("You have 0 mana left" + "\n")	
		else:
			print(f"You have {self.mana} mana left" + "\n")
	def staff_hit(self,enemy):
		dmg = random.uniform(3,6)
		enemy.hp -= dmg
		print(f"You hit the {enemy.name} with your staff")
		print(f"you deal {round(dmg)} damage")
	def regain_mana(self,enemy):
		mana_regen_spell = 15
		if self.mana != 0 and attack_first != 0:
			manamana = 0
			while self.mana < self.maxmana and manamana < mana_regen_spell:
				manamana += 1
			else:
				self.mana += manamana
			print_slow(f"you have regained {manamana} mana, and you now have {self.mana} mana in total" + "\n")
	def attack(self, enemy):
		return Player.attack(self,enemy)
	def flee(self,enemy):
		return Player.flee(self,enemy)
	def check_death(self):
		return Player.check_death(self)
	def check_kill(self,enemy):
		return Player.check_kill(self,enemy)
	def regen_after_fight(self):
		return Player.regen_after_fight(self)

class Fighter(Player):
	what_class = "Fighter"
	def __init__(self,name):
		Player.__init__(self,name)
		self.name = name
		self.hp = 350
		self.maxhp = 350
		self.rage = 0
		self.maxrage = 100
		self.attackdmg = 1.3
		self.tiredness = 0
		self.tired_threshold = 3
		self.mana = 0
	def lose_hp(self,amount):
		return Player.lose_hp(self,amount)
	def earn_xp(self,enemy):
		return Player.earn_xp(self,enemy)
	def sword_hit(self,enemy):
		dmg = round(random.uniform(9*1.3*self.attackdmg + (2*enemy.number_of),10*1.5*self.attackdmg+(3*enemy.number_of)))
		enemy.hp -= dmg
		print(f"You slash the {enemy.name} with your swords")
		print(f"you deal {round(dmg)} damage")
		self.tiredness += 2
	def shield_bash(self,enemy):
		dmg = round(random.uniform(5*1.2*self.attackdmg,9*1.4*self.attackdmg))
		enemy.hp -= dmg
		print(f"You bash the {enemy.name} with your shield")
		print(f"you deal {round(dmg)} damage")
		self.tiredness += 1
	def headbutt(self,enemy):
		dmg = round(random.uniform(5*1.3*self.attackdmg,9*1.5*self.attackdmg))
		enemy.hp -= dmg
		print(f"You headbutt the {enemy.name}")
		print(f"you deal {round(dmg)} damage")
		if randint(1,3) == 1:
			selfdmg = round(0.25 * dmg)
			self.hp -= selfdmg
			print_slow (f"You hurt your head headbutting the {enemy.name}. You lose {round(selfdmg)} hp, and now have {round(self.hp)}" + "\n")
	def kick(self,enemy):
		dmg = round(random.uniform(3*self.attackdmg,6*1.1*self.attackdmg))
		enemy.hp -= dmg
		print(f"You kick the {enemy.name}")
		print(f"you deal {round(dmg)} damage")
	def attack(self, enemy):
		return Player.attack(self,enemy)
	def flee(self,enemy):
		return Player.flee(self,enemy)
	def check_kill(self,enemy):
		return Player.check_kill(self,enemy)
	def check_death(self):
		return Player.check_death(self)
	def regen_after_fight(self):
		return Player.regen_after_fight(self)


class Enemy():
	def __init__(self, number_of, name):
		self.number_of = int(number_of)
		self.name = name
		self.minxp = 0
		self.maxxp = 1
	def attack(self):
		if class1.hp > 0:
			print(f"you now have {round(class1.hp)} health" + "\n")
	def appearing(self):
		if self.number_of > 1:
			print (f"{self.number_of} {self.name}s have appeared\n")
			print (f"{self.name} have {self.hp} health\n")
		else:
			print(f"{self.name} has appeared\n")
			print (f"They have {self.hp} health\n")
	
class Orc(Enemy):
	def __init__(self, number_of, name):
		Enemy.__init__(self, number_of, name)
		self.hp = 30 * self.number_of
		self.minxp = 4 * self.number_of
		self.maxxp = 7 * self.number_of
	def deal_dmg(self, player):
		dmg = round(randint(5 * self.number_of, 9* self.number_of))
		player.hp -= dmg
		print ("The orc(s) hit(s) you\n")
		print(f"it deals {dmg} damage\n")
		return Enemy.attack(self)
	def appearing(self):
		return Enemy.appearing(self)
mineorc1 = Orc(2,"Mine Orc")


class Goblin(Enemy):
	def __init__(self, number_of, name):
		Enemy.__init__(self, number_of, name)
		self.hp = 22 * self.number_of
		self.minxp = 3 * self.number_of
		self.maxxp = 5 * self.number_of
	def deal_dmg(self, player):
		goblin_att_times = 1
		if randint(1,5) == 1:
			goblin_att_times += 1
		while goblin_att_times > 0:
			dmg = round(random.uniform(3 * self.number_of, 6.2* self.number_of))
			player.hp -= dmg
			print ("The goblin(s) bite(s) you\n")
			print(f"it deals {round(dmg)} damage\n")
			goblin_att_times -= 1
		return Enemy.attack(self)	
	def appearing(self):
		print ("*Goblins have a small chance to strike twice when they attack*\n")
		return Enemy.appearing(self)
		

minegoblin1 = Goblin(3,"Goblin")

class Spider(Enemy):
	poison_dmg = 0
	def __init__(self, number_of, name):
		Enemy.__init__(self, number_of, name)
		self.hp = 9 * self.number_of
		self.poison_dmg = 0
		self.minxp = 2 * self.number_of
		self.maxxp = 4 * self.number_of
	def deal_dmg(self,player):
		if self.poison_dmg > 0:
			dot = 2 ** ((self.poison_dmg*0.75) + 1)
			player.hp -= dot
			print ("*You are poisoned*\n")
			print (f"You lose {round(dot)} health from the poison\n")
		dmg = round(random.uniform(2.4 * self.number_of, 3.6* self.number_of))
		player.hp -= dmg
		print ("The spider(s) bite(s) you. \n")
		print(f"It deals {round(dmg)} damage\n")
		if randint(1,4) == 1:
			self.poison_dmg += 1
			if self.number_of == 1:
				print ("The spider poisons you\n")
			else:
				print ("The spiders poison you\n")
		return Enemy.attack(self)
	def appearing(self):
		print ("*Spiders have a chance to hit you with poison that deals damage over time (each round) - damage stacks exponentially*\n")
		return Enemy.appearing(self)

minespider1 = Spider(5,"Cave Spider")

class Woodelf(Enemy):
	def __init__(self, number_of, name):
		Enemy.__init__(self, number_of, name)
		self.hp = 70 * self.number_of
		self.minxp = 10 * self.number_of
		self.maxxp = 15 * self.number_of
	def deal_dmg(self,player):
		if randint(1,4) == 1:
			bowdmg = round(randint(5*self.number_of,7 * self.number_of))
			class1.hp -= bowdmg
			if self.number_of == 1:
				print(f"{self.name} shoots you with his bow.\n")
			else:
				print_slow("The wood-elves shoot you with their bows.\n")
			print_slow(f"It deals {bowdmg} damage\n")
		dmg = round(random.uniform(15 * self.number_of, 25* self.number_of))
		player.hp -= dmg
		if self.number_of == 1:
			print (f"{self.name} slashes you with his sword. \n")
		else:
			print ("The wood-elves slash you with their swords. \n")
		print(f"It deals {round(dmg)} damage. \n")

		return Enemy.attack(self)
	def appearing(self):
		print ("*Wood elves have a chance to hit you with their bow and arror before they attack for bonus damage* \n")
		return Enemy.appearing(self)

Aegar_enemy = Woodelf(1,"Aegar")

class Skeletal(Enemy):
	def __init__(self, number_of, name):
		Enemy.__init__(self, number_of, name)
		self.hp = 38 * self.number_of
		self.minxp = 6 * self.number_of
		self.maxxp = 8 * self.number_of
	def deal_dmg(self,player):
		dmg = round(random.randint(8 * self.number_of, 11* self.number_of))
		player.hp -= dmg
		if self.number_of == 1:
			print (f"{self.name} hits you with a bone. \n")
		else:
			print ("The skeletals hit you with bones. \n")
		print(f"It deals {round(dmg)} damage. \n")
		return Enemy.attack(self)
	def appearing(self):
		print_slow ("*Skeletals have a small chance to resurrect another skeletal before the fight, increasing the number of them by 1*\n")
		Enemy.appearing(self)
		if randint(0,5) == 5:
			self.number_of += 1
			print_slow(f"The skeleton has resurrected another skeleton from the dead. You are now facing {self.number_of} skeletons.\n")

skeletal_trap1 = Skeletal(2,"Skeletal")

class Minotaur(Enemy):
	#brug a_fight_no_fightflee
	def __init__(self, number_of, name):
		Enemy.__init__(self, number_of, name)
		self.hp = 80 * self.number_of
		self.minxp = 12 * self.number_of
		self.maxxp = 13 * self.number_of
	def deal_dmg(self,player):
		if randint(1,2) == 1: #attack 1 - ram with horns
			if randint (1,3) == 1:
				if self.hp <= 12:
					print_slow(f"{self.name} kills itself by ramming into the wall. \n")
				else:
					self.hp -= 12
					print_slow(f"{self.name} misses you and charges into the wall. {self.name} loses 12 hp and now has {round(self.hp)}. \n")
			else:
				dmg = round(random.randint(20 * self.number_of, 22* self.number_of))
				player.hp -= dmg
				if self.number_of == 1:
					print (f"{self.name} rams into you. \n")
				else:
					print ("The Minotaurs ram into you. \n")
				print(f"It deals {round(dmg)} damage")
				return Enemy.attack(self)
		else: #attack 2 - hit with great axe
			dmg = round(random.randint(9 * self.number_of, 20* self.number_of))
			player.hp -= dmg
			if self.number_of == 1:
				print (f"{self.name} hits you with his great axe. \n")
			else:
				print ("The Minotaurs hit you with their great axes. \n")
			print(f"It deals {round(dmg)} damage. \n")
			return Enemy.attack(self)
	def appearing(self):
		print_slow ("*Minotaurs knows the place they are in so well that you cannot flee from them*\n")
		print_slow("It has 2 attacks:\nRam with horns - has high damage, but a chance to miss and damage itself instead.\nGreat axe hit - normal attack, damage varies from low to high\n")
		Enemy.appearing(self)
Minotaur_trap1 = Minotaur(1,"Minotaur")

class Troll(Enemy):
	def __init__(self, number_of, name):
		Enemy.__init__(self, number_of, name)
		self.hp = 80 * self.number_of
		self.minxp = 11 * self.number_of
		self.maxxp = 12 * self.number_of
	def deal_dmg(self,player):
		if randint(1,2) == 1: #attack 1 - bite
			dmg = round(random.randint(9 * self.number_of, 11* self.number_of))
			player.hp -= dmg
			if self.number_of == 1:
				print (f"{self.name} bites you. \n")
			else:
				print (f"{self.name} bite you. \n")
			print(f"It deals {dmg} damage")
			return Enemy.attack(self)
		else: #attack 2 - hit with knife
			dmg = round(random.randint(11 * self.number_of, 12* self.number_of))
			player.hp -= dmg
			if self.number_of == 1:
				print (f"{self.name} hits you with his knife. \n")
			else:
				print (f"{self.name} hit you with their knives. \n")
			print(f"It deals {round(dmg)} damage. \n")
			return Enemy.attack(self)
	def appearing(self):
		print_slow("*Trolls might not be very clever, but they are very dangerous beasts.*\n")
		print_slow("*They can either bite you, or hit you with their weapons.*\n")
		print_slow("*There is a small chance that they will pick up a rock and throw it at you before they attack, dealing bonus damage*\n")
		Enemy.appearing(self)

Udefrykte_Zolkaz = Troll(2,"Udefrykte and Zolkaz")

class Darkelf(Enemy):
	def __init__(self, number_of, name):
		Enemy.__init__(self, number_of, name)
		self.hp = 60 * self.number_of
		self.minxp = 8 * self.number_of
		self.maxxp = 12 * self.number_of
	def deal_dmg(self,player):
		dmg = round(random.uniform(8 * self.number_of, 13* self.number_of))
		player.hp -= dmg
		if self.number_of == 1:
			print (f"{self.name} stabs you with his daggers. \n")
		else:
			print ("The dark elves stab you with their daggers. \n")
		print(f"It deals {round(dmg)} damage. \n")
		return Enemy.attack(self)
	def appearing(self):
		print ("*Dark elves have a chance to dodge your attack* \n")
		return Enemy.appearing(self)

wagon_darkelves = Darkelf(2,"dark elves")

class Bear(Enemy):
	def __init__(self, number_of, name):
		Enemy.__init__(self, number_of, name)
		self.hp = 65 * self.number_of
		self.minxp = 10 * self.number_of
		self.maxxp = 13 * self.number_of
	def deal_dmg(self,player):
		if randint(1,2) == 1: #attack 1 - bite
			dmg = round(random.randint(10 * self.number_of, 12* self.number_of))
			player.hp -= dmg
			if self.number_of == 1:
				print (f"{self.name} bites you. \n")
			else:
				print (f"{self.name} bite you. \n")
			print(f"It deals {dmg} damage")
			return Enemy.attack(self)
		else: #attack 2 - clawing
			dmg = round(random.randint(5 * self.number_of, 17* self.number_of))
			player.hp -= dmg
			if self.number_of == 1:
				print (f"{self.name} claws you. \n")
			else:
				print (f"{self.name} claw you. \n")
			print(f"It deals {round(dmg)} damage. \n")
			return Enemy.attack(self)
	def appearing(self):
		print ("*Against bears you have the option of petting them or attacking them. petting them means they won't attack you for 2 turns* \n")
		print ("*This can stack*")
		return Enemy.appearing(self)

bear_forest = Bear(1,"brown bear")

def a_fight(player,enemy):
	fight = ""
	attack_first = ""
	abcde = False
	fighting = True
	answer1 = ""
	while answer1 != "fight" and answer1 != "flee":
		answer1 = input("you want to fight or attempt to flee (fight/flee)? ")
	if answer1 == "fight":
		player.attack(enemy)
		fight = True
	elif answer1 == "flee":
		if player.flee(enemy) == False:
			fight = False
		else:
			fight = True
			attack_first = "enemy"
	while fight:
		while fighting:
			if attack_first == "enemy":
					turn = "enemy"
			else:
				if attacks_first() == "enemy":
					turn = "enemy"
				else:
					turn = "player"
			while turn == "enemy":
				enemy.deal_dmg(player)
				turn = "player"
				abcde = False
				input("...")
			while turn == "player":
				if abcde == True:
					break
				if player.check_only_kill(enemy) == False:
					fighting = False
				if player.check_death() == (False,False):
					sys.exit()
				if player.what_class == "Mage":
					mage_spell = input("\n" + "what do you want to do? (1/2/3/4)" + "\n" "1 = fireball(cost 25 mana) " + "\n" + "2 = ice spike (cost 15 mana)" + "\n" + "3 = staff hit(cost 0 mana)" + "\n" + "4 = regain mana (regains 15 mana)" + "\n")
					if mage_spell == "1" and player.mana < player.mana_required_fireball:
						if player.mana < 0:
							print_slow (f"not enough mana to perform this, you have 0 mana, and it costs {player.mana_required_fireball}" + "\n")	
						else:
							print_slow (f"not enough mana to perform this, you have {player.mana} mana, and it costs {player.mana_required_fireball} mana" + "\n")
						continue
					elif mage_spell == "1" and player.mana >= player.mana_required_fireball:
						if player.fireball(enemy) == False:
							fight = False
							abcde = True
							break
					elif mage_spell == "2" and player.mana < player.mana_required_ice_spike:
						if player.mana < 0:
							print_slow (f"not enough mana to perform this, you have 0 mana, and it costs {player.mana_required_ice_spike}" + "\n")	
						else:
							print_slow (f"not enough mana to perform this, you have {player.mana} mana, and it costs {player.mana_required_ice_spike} mana" + "\n")
						continue
					elif mage_spell == "2" and player.mana >= player.mana_required_ice_spike:
						player.ice_spike(enemy)
						if randint(1,6) == 1:
							print_slow ("You froze the enemy, and can now do another action" + "\n")
							continue
					elif mage_spell == "3":
						player.staff_hit(enemy)
					elif mage_spell == "4":
						player.regain_mana(enemy)

					else:
						print_slow ("unknown spell, please pick a spell" + "\n")
						continue
				elif player.what_class == "Fighter":
					if player.rage == player.maxrage:
						player.attackdmg *= 2
						print_slow ("This move will do double damage\n")
					fighter_move = input("\n" + "what do you want to do? (1/2/3/4)" + "\n" "1 = sword hit(adds 2 tiredness) " + "\n" + "2 = shield bash (adds 1 tiredness)" + "\n" + "3 = headbutt" + "\n" + "4 = kick" + "\n")
					if fighter_move == "1" and player.tiredness < player.tired_threshold:
						player.sword_hit(enemy)
					elif fighter_move == "2" and player.tiredness < player.tired_threshold:
						player.shield_bash(enemy)
					elif fighter_move == "3":
						player.headbutt(enemy)
					elif fighter_move == "4":
						player.kick(enemy)
					else:
						print_slow ("You cannot do that, please pick one of the options available" + "\n")
						continue
					if player.rage == player.maxrage:
						player.attackdmg *= 0.5
						player.rage -= 100
					print_slow ("You regain rage after each attack. Roll how much you get. \n")
					rage_regen = 2*(die(1,6))
					ragerage = 0
					while player.rage+ragerage < 100 and ragerage < rage_regen:
						ragerage += 1
					else:
						player.rage += ragerage
					print_slow (f"Your rage increases by {ragerage}. You now have {player.rage} \n")
					if player.rage == player.maxrage:
						print_slow ("You now have full rage. Your next move will do double damage")
					if player.tiredness != 0:
						if fighter_move == "3" or fighter_move == "4":
							player.tiredness -= 1
							print_slow (f"Your tiredness decreases by 1. it is now at {player.tiredness} \n")

				turn = "enemy"
				if player.check_kill(enemy) == False:
					fighting = False
				abcde = True
				break
			break
		else:
			class1.regen_after_fight()
			if player.what_class == "Fighter":
				player.tiredness = 0
				print_slow ("After finishing the fight you realize you are not going to fight for a bit. \n")
				print_slow ("This means you lose some rage, 'roll' the dice to see how much \n")
				rage_loss = 2*(die(1,6))
				ragerage = 0
				while player.rage - ragerage != 0 and ragerage < rage_loss:
					ragerage += 1
				else:
					player.rage -= ragerage
				print_slow (f"Your rage decreases by {ragerage}. You now have {player.rage} \n")

			
			player.earn_xp(enemy)
			
			abc = False
			fight = False
			fighting = False
			break

def a_fight_no_fightflee(player,enemy,youstarting = False,dark_elf_combat = False,Bear_combat=False):
	abcde = False
	fight = True
	bear_tame = False	
	bear_tame_turns = 0
	turn = ""
	if youstarting == True:
		turn = "player"
	fighting = True
	while fight:
		while fighting:
			if turn == "enemynow":
				turn = "enemy"
			elif turn == "playernow":
				turn = "player"
			elif youstarting != True:
				if attack_first == "enemy":
					turn = "enemy"
				else:
					if attacks_first() == "enemy":
						turn = "enemy"
					else:
						turn = "player"
			while turn == "enemy":
				if bear_tame == True:
					bear_tame_turns = 2
					bear_tame = False
				if bear_tame_turns > 0:
					print_slow(f"{enemy.name} is still dancing the Jungle Boogie\n")
					bear_tame_turns -= 1
					turn = "playernow"
					break         
				else:
					enemy.deal_dmg(player)
					turn = "player"
					abcde = False
					input("...")
			while turn == "player":
				if abcde == True:
					break
				if player.check_only_kill(enemy) == False:
					fighting = False
				if player.check_death() == (False,False):
					sys.exit()
				attack_block = False
				if dark_elf_combat:
					if randint(1,5) == 1:
						attack_block = True
				if attack_block:
					if class1.what_class == "Mage":
						input("\n" + "what do you want to do? (1/2/3/4)" + "\n" "1 = fireball(cost 25 mana) " + "\n" + "2 = ice spike (cost 15 mana)" + "\n" + "3 = staff hit(cost 0 mana)" + "\n" + "4 = regain mana (regains 15 mana)" + "\n")
					elif class1.what_class == "Fighter":
						input("\n" + "what do you want to do? (1/2/3/4)" + "\n" "1 = sword hit(adds 2 tiredness) " + "\n" + "2 = shield bash (adds 1 tiredness)" + "\n" + "3 = headbutt" + "\n" + "4 = kick" + "\n")
					print("*The dark elf dodges your attack.*\n")
					turn = "enemy"
					break
				if Bear_combat == True:
					if Bear_combat == True:
						bear_petting = ""
					while bear_petting != "1" and bear_petting != "2":
						bear_petting = input("Do you want to pet the bear or attack it (1 = pet, 2 = attack)")
					if bear_petting == "1":
						if randint(1,4) == 1:
							print_slow(f"You succesfully petted the {enemy.name}. It starts dancing the Jungle Boogie\n")
							bear_tame = True
						else:
							print_slow("You failed to pet the bear. It does not look happy.\n")
						turn = "enemynow"
						break
				if player.what_class == "Mage":
					mage_spell = input("\n" + "what do you want to do? (1/2/3/4)" + "\n" "1 = fireball(cost 25 mana) " + "\n" + "2 = ice spike (cost 15 mana)" + "\n" + "3 = staff hit(cost 0 mana)" + "\n" + "4 = regain mana (regains 15 mana)" + "\n")
					if mage_spell == "1" and player.mana < player.mana_required_fireball:
						if player.mana < 0:
							print_slow (f"not enough mana to perform this, you have 0 mana, and it costs {player.mana_required_fireball}" + "\n")	
						else:
							print_slow (f"not enough mana to perform this, you have {player.mana} mana, and it costs {player.mana_required_fireball} mana" + "\n")
						continue
					elif mage_spell == "1" and player.mana >= player.mana_required_fireball:
						if player.fireball(enemy) == False:
							fight = False
							abcde = True
							break
					elif mage_spell == "2" and player.mana < player.mana_required_ice_spike:
						if player.mana < 0:
							print_slow (f"not enough mana to perform this, you have 0 mana, and it costs {player.mana_required_ice_spike}" + "\n")	
						else:
							print_slow (f"not enough mana to perform this, you have {player.mana} mana, and it costs {player.mana_required_ice_spike} mana" + "\n")
						continue
					elif mage_spell == "2" and player.mana >= player.mana_required_ice_spike:
						player.ice_spike(enemy)
						if randint(1,6) == 1:
							print_slow ("You froze the enemy, and can now do another action" + "\n")
							continue
					elif mage_spell == "3":
						player.staff_hit(enemy)
					elif mage_spell == "4":
						player.regain_mana(enemy)

					else:
						print_slow ("unknown spell, please pick a spell" + "\n")
						continue
				elif player.what_class == "Fighter":
					if player.rage == player.maxrage:
						player.attackdmg *= 2
						print_slow ("This move will do double damage\n")
					fighter_move = input("\n" + "what do you want to do? (1/2/3/4)" + "\n" "1 = sword hit(adds 2 tiredness) " + "\n" + "2 = shield bash (adds 1 tiredness)" + "\n" + "3 = headbutt" + "\n" + "4 = kick" + "\n")
					if fighter_move == "1" and player.tiredness < player.tired_threshold:
						player.sword_hit(enemy)
					elif fighter_move == "2" and player.tiredness < player.tired_threshold:
						player.shield_bash(enemy)
					elif fighter_move == "3":
						player.headbutt(enemy)
					elif fighter_move == "4":
						player.kick(enemy)
					else:
						print_slow ("You cannot do that, please pick one of the options available" + "\n")
						continue
					if player.rage == player.maxrage:
						player.attackdmg *= 0.5
						player.rage -= 100
					print_slow ("You regain rage after each attack. Roll how much you get. \n")
					rage_regen = 2*(die(1,6))
					ragerage = 0
					while player.rage+ragerage < 100 and ragerage < rage_regen:
						ragerage += 1
					else:
						player.rage += ragerage
					print_slow (f"Your rage increases by {ragerage}. You now have {player.rage} \n")
					if player.rage == player.maxrage:
						print_slow ("You now have full rage. Your next move will do double damage")
					if player.tiredness != 0:
						if fighter_move == "3" or fighter_move == "4":
							player.tiredness -= 1
							print_slow (f"Your tiredness decreases by 1. it is now at {player.tiredness} \n")

				turn = "enemy"
				if player.check_kill(enemy) == False:
					fighting = False
				abcde = True
				break
			break
		else:
			class1.regen_after_fight()
			if player.what_class == "Fighter":
				player.tiredness = 0
				print_slow ("After finishing the fight you realize you are not going to fight for a bit. \n")
				print_slow ("This means you lose some rage, 'roll' the dice to see how much \n")
				rage_loss = 2*(die(1,6))
				ragerage = 0
				while player.rage - ragerage != 0 and ragerage < rage_loss:
					ragerage += 1
				else:
					player.rage -= ragerage
				print_slow (f"Your rage decreases by {ragerage}. You now have {player.rage} \n")

			
			player.earn_xp(enemy)
			
			abc = False
			fight = False
			fighting = False
			break

def attacks_first():
	if class1.what_class == "Mage":
		if randint(0,1) == 0:
			return "enemy"
		else:
			return "player"
	elif class1.what_class == "Fighter":
		if randint(0,2) == 0:
			return "enemy"
		else:
			return "player"

import sys,time,random
def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.0000001)

class Potion():
	hppot_regen = 0
	manapot_regen = 0
	def __init__(self,size,kind,amount):
		self.amount = int(amount)
		self.size = size
		self.kind = kind
		self.small_manapot = 0
		self.large_manapot = 0
		self.small_hppot = 0 
		self.large_hppot = 0
		self.full_name = self.size + " " + self.kind + " " + "potion"
		print(f"*{class1.name.capitalize()} has found a {self.full_name}*" + "\n")
		print("You can choose to do something with it now, or the next time you arrive at a safe place")
	def new_potion(self):
		if self.size == "small" and self.kind == "mana":
			self.small_manapot += 1
		elif self.size == "small" and self.kind == "hp":
			self.small_hppot += 1
		elif self.size == "large" and self.kind == "mana":
			self.large_manapot += 1
		elif self.size == "large" and self.kind == "hp":
			self.large_hppot += 1
	def smash(self):
		print(f"*{class1.name} throws the {self.full_name} into the ground.*")
		print(f"The {self.full_name} is now destroyed.")
		print("That was pretty stupid, honestly")
		input("...")
		if self.size == "small" and self.kind == "mana":
			self.small_manapot -= 1
		elif self.size == "small" and self.kind == "hp":
			self.small_hppot -= 1
		elif self.size == "large" and self.kind == "mana":
			self.large_manapot -= 1
		elif self.size == "large" and self.kind == "hp":
			self.large_hppot -= 1
	def drink(self):
		if self.size == "small" and self.kind == "mana":
			self.small_manapot -= 1
			self.manapot_regen = 40
		elif self.size == "small" and self.kind == "hp":
			self.small_hppot -= 1
			self.hppot_regen = 20
		elif self.size == "large" and self.kind == "mana":
			self.large_manapot -= 1
			self.manapot_regen = 100
		elif self.size == "large" and self.kind == "hp":
			self.large_hppot -= 1
			self.hppot_regen = 50
		hppot_hppot = 0
		if self.hppot_regen > 0:
			while self.hppot_regen > 0 and (hppot_hppot + class1.hp) < class1.maxhp:
				hppot_hppot += 1
				self.hppot_regen -= 1
			else:
				class1.hp += hppot_hppot
				print(f"You have regained {hppot_hppot} hp, and now have {class1.hp} hp")
		manapot_manapot = 0
		if self.manapot_regen > 0:
			while self.manapot_regen > 0 and (manapot_manapot + class1.mana) < class1.maxmana:
				manapot_manapot += 1
				self.manapot_regen -= 1
			else:
				class1.mana += manapot_manapot
				print(f"You have regained {manapot_manapot} mana, and now have {class1.mana} mana")
		
	   

def potion_action(potion):
	while True:
		if potion.kind == "mana":
			print(f"You currently have {class1.mana} mana")
			print(f"The {potion.full_name} gives you {potion.amount} mana")
		elif potion.kind == "hp":
			print(f"you currently have {class1.hp} hp")
			print(f"The {potion.full_name} gives you {potion.amount} hp")
			
		pot_act = input("Do you want to drink the potion, smash it into the ground, or do nothing with it? (drink = 1, smash = 2, do nothing = 3) " )
		if pot_act == "1":
			potion.drink()
			break
		elif pot_act == "2":
			potion.smash()
			break
		elif pot_act == "3":
			print(f"{class1.name.capitalize()} saves the potion for another day. It won't expire - probably")
			break


w = "w"
a = "a"
d = "d"
s = "s"

#lav liste i stedet for string ["hvad der sker", "tast der klarer det","Hvor tæt edderkoppen kommer = int", "besked for man ikke klarer det", "besked for man klarer det"]
w1 = ["OBSTACLE: A barrel starts rolling towards you.\n",w,2,"You fail to jump over the barrel. This slows you down, and you can feel the spider getting closer.\n","You time the jump perfectly, and leap over the barrel. You continue on your way out.\n"]
w2 = ["OBSTACLE: You are about to trip over a big bunch of spiderweb on the ground.\n",w,1,"Your feet gets stuck in the spiderweb, and you trip. You manage to get free quickly, and continue on your way.\n","You jump a little to avoid the spiderweb.\n"]
w3 = ["OBSTACLE: You see a big hole in the ground in front of you.\n",w,3,"You fail to jump over the hole, which means you are now stuck down here. \nIt takes you a lot of time, but you manage to climb up, and be on your way.\n","Even though the hole is pretty big, you manage to beautifully jump over.\n"]
w4 = ["OBSTACLE: You are about to trip over a dead body. ",w,1,"You trip over the dead body. You better hurry up out the way,so you don't end up like him.\n","You manage to make a big step over him. Whew, now you won't end up like that poor soul\n"]
w5 = ["OBSTACLE: In front of you there is a bridge. Or was, since there is not much left of it. You have to pass it though.\n",w,2,"You see the gap, but not in time to get a proper jump. You manage to grab the ledge, \nbut pulling yourself up is pretty hard. You are pretty tired as well. But you have to get a move on.\n","Even though there is no bridge anymore, you manage to cross it. Well done.\n"]#grabber ledge i stedet, tager lidt tid at løfte sig op
da1 = ["OBSTACLE: You see a puddle of mud in front of you. It is too big to jump over.",[d,a],2,"You fumble around, and end up stepping in the middle of the puddle. \nIt's pretty thick and pretty difficult to get out. Fortunately, you manage to break free in the end\n","You run to the side, and avoid the mud.\n"]
da2 = ["OBSTACLE: You see a puddle of water in front of you. It is too big to jump over.",[d,a],1,"You fumble around, and end up stepping in the middle of the puddle.\nYour feet gets wet, but other than that it doesn't slow you down that much.\n", "You run to the side, and avoid the puddle\n"]
da3 = ["OBSTACLE: Suddenly a small rock drops from the top of the cave",[d,a],2,"You didn't manage to dodge, so it hits you right in the head. \nIt hurts a bit, so you need to recover, but you manage to get up and move on.\n","The small rock falls to the ground, but you manage to dodge it, by jumping to the side. \nIt hits the ground, and you continue ony your way.\n"]
da4 = ["OBSTACLE: There is a bunch of bones on the path in front of you",[d,a],1,"You didnt manage to move to the side, you stepping on them slows you down mildly, but you continue.\n","You move to the side and avoid the bones.\n"]
a1 = ["OBSTACLE: You are about to run into some cobweb. You can see a small path around it to your left",a,1,"You failed to run to the left to avoid it. The cobweb get's everywhere, but you manage to remove it and continue moving.\n","You evade the cobweb, by runnung to the left, and maintain your momentum.\n"]
d1 = ["OBSTACLE: You can see the cave dividing in two. Coming a bit closer you notice the left path is a dead end",d,1,"You didn't manage to choose the right path, and have to accelerate again.\n","You chose the right way by going right, and you are now one step closer to escaping the cave.\n"]
s1 = ["OBSTACLE: Ahead of you, you notice the cave ceiling lowering.",s,2,"You didn't manage to duck, so you hit your head into the cave ceiling. This hurts, and you need some time to recover.\n","You magnificently slide under the cave ceiling and keep your speed.\n"]
s2 = ["OBSTACLE: You feel the cave rumbling. Suddenly the whole cave ceiling starts falling apart. There is no other way than through",s,3,"You didn't manage to slide under, so now the path is completely blocked. You have to take a detour around now.\n","You speed up, and slide under, making it through the collapsing part of the cave. \nYou look back, and see that the path back is completely blocked. Whew!\n"]

#liste [event,{dictionary: tast1: [afstand tast1, besked for tast1], tast2: [afstand tast2, besked for tast2]}
updown1 = ["PATH: you can either crawl down into a cave or proceed on your way forward.",{w:[0,"You choose to proceed on your way forward. This seems like the right way since the path is clear.\n"],s:[1,"You take the chance and crawl into the little cave. \nIt doesn't seem to get bigger, so you are forced to crawl. This slows you down.\n"]}]
rightleft3 = ["PATH: To the left there is a thin ledge you have walk on. To the right the path looks clear so far.",{a:[0,"You risk it and sneak past the ledge. Luckily it isn't like this for long, so you are quickly able to run again.\n"],d:[1,"You take the clear path. It is nice to begin with, but after a while you regret going this way. \nThe terrain is very uneven, and there are holes everywhere, you have to go slow, which really slows you down.\n"]}] #ledge en side (den rigtige), clear path anden side
rightleft4 = ["PATH: To the left you can go through a thin passage - if you can fit. To the right the passage looks very dark.",{a:[2,"Walking closer you are having serious second doubts. You can fit - but barely. \nIt takes a very long time but you make it past to the other side.\n"],d:[1,"The passage starts of pitch black, meaning you are going very slow the first few steps. \nLuckily it gets lighter and lighter, and you are out in no time.\n"]}] #thin passage venstre - dark passage højre

# lav 2 muligheder som values til key, den ene for lav terningeslag, den anden for højt, [lav terninge besked, høj terning besked], anden mulighed besked
updown2 = ["PATH: There are stairs going up, and stairs going down. The stairs up are in perfect shape, but the stairs down are in bad condition",{s:[2,0],w:1},["You walk down the stairs, but keep twisting you ankle, so you decide to slow down.\n","You walk down the stairs. The condition of the stairs don't mean much to you, so you pick up the pace.\n"],"You walk up the stairs. This is no problem but it takes some extra time.\n"] #(kræver dice roll for at klare ordentligt - stairs down)
updown3 = ["PATH: There is a big hole in the ground in front of you. It's too big to jump, but there is a rope. \nOtherwise you can go down under the bridge. That path looks very long though",{w:[3,0],s:2},["You go for the rope. You swing and swing and then jump. Damn, you missed the bridge. \nYou fall down and manage to grab the ledge down under. \nPulling yourself up is difficult, and then you have to take the whole detour around as well.\n","You grab the rope, swing forwards, then backwards, and then jump, landing safely on the other side of the bridge"],"The risk doesn't seem like a good idea, so you take the long detour around.\n"]#svinge i reb  får grebet fast i kanten hvis fejler, eller tag omvej under
rightleft1 = ["PATH: To the right it is going downwards pretty steep. To the left, the path is leading backwards",{a:[0,2],d:1},["You try to walk down the steep path, but slip and fall, and get up again. This happens multiple times, slowing you down a lot.\n","You take the steep way down, but walk diligently, but still with some pace. You manage to get out without tripping once.\n"],"You take the path leading backwards. It may be slower, but nothing happens this way.\n"]
rightleft2 = ["PATH: To the right you can follow the path, to the left you can go offroad. The left way looks faster though.",{a:[2,-2],d:0},["You take the risky path to the left. It is very slippery, so to avoid falling you walk very slow.","You take the risky path to the left. You notice it is very slippery. \nLuckily, right after entering you notice something looking like a shell. \nYou decide to slide down throught the mud. You get down in no time.\n"],"You decide to take no chances and just follow the path"] #risikabel en side, følg sti den anden
rightleft5 = ["PATH: You can now proceed forward (press d), or take a side route to the left",{a:[1,-1],d:0},["You take the side route. It feels a bit long.\n","You take the side route. It feels like a nice little detour and you are out in no time.\n"],"You proceed forward.\n"]
rightleft6 = ["PATH: The path ahead is blocked. You have to go upwards. \nTo the right you might be able to leap up. To the left you can climb up.",{a:[3,0],d:2},["You try to leap up. Instead you fail, hit your head, and are forced to climb up.\n","You try to leap up. You manage to grab the ledge, and pull yourself up.\n"],"You climb up. It might take longer time than jumping, but it is less risky.\n"]

def evading(all_evade_lists):
    #all_evade_lists = evade_list[index]
    action = all_evade_lists[0]
    if type(all_evade_lists[1]) == list:
        key1,key2 = all_evade_lists[1]
    else:
        key1 = all_evade_lists[1]
        key2 = 0
    spider_distancing = all_evade_lists[2]
    failed = all_evade_lists[3]
    completed = all_evade_lists[4]
    print(action)
    start = datetime.now()
    the_input = input("")
    if (the_input.lower() == key1 or the_input.lower() == key2) and datetime.now()<=start + timedelta(seconds = 5):
        #right answer
        print_slow(completed)
    else:
        print_slow(failed)
        global spider_distance
        spider_distance += spider_distancing

ready = input("Are you ready to play? (y / n) ")
if ready.lower() == "y":
	print("Welcome to the game!")
	playing = True
else:
	playing = False
name = "" 
while name == "":
	name = input("What is your name? ").capitalize()
if playing == False:
	ready2 = input("Are you ready to play now? (y / n) ")
	if ready2.lower() == "y":
		print("Welcome to the game!")
		playing = True
	else:
		sys.exit()

def choose1(all_choose_lists):
    extra_distance = 0
    #all_choose_lists = choose_list[index]
    action = all_choose_lists[0]
    first_key,second_key = all_choose_lists[1].keys()
    first_way = all_choose_lists[1][first_key][1]
    second_way = all_choose_lists[1][second_key][1]
    first_distance = all_choose_lists[1][first_key][0]
    second_distance = all_choose_lists[1][second_key][0]
    while True:
        print(action)
        start = datetime.now()
        the_input = input("")
        if the_input.lower() == first_key and datetime.now()<=start + timedelta(seconds = 5):
            print_slow(first_way)
            return first_distance + extra_distance
            break
        elif the_input.lower() == second_key and datetime.now()<=start + timedelta(seconds = 5):
            print_slow(second_way)
            return second_distance + extra_distance
            break
        else:
            print_slow("You took too long or picked an unavailable action. The spider gets closer.\n")
            extra_distance += 1
            continue
def choose2(func):
    global spider_distance
    spider_distance += func
def choose(all_choose_lists):
    choose2(choose1(all_choose_lists))

def choose_roll1(all_choose_roll_lists):
    extra_distance = 0
    #all_choose_roll_lists = choose_roll_list[index]
    action = all_choose_roll_lists[0]
    first_key,second_key = all_choose_roll_lists[1].keys()
    bad_first_distance,good_first_distance = all_choose_roll_lists[1][first_key]
    second_distance = all_choose_roll_lists[1][second_key]
    bad_first_way,good_first_way = all_choose_roll_lists[2] 
    second_way = all_choose_roll_lists[3]
    while True:
        print(action)
        start = datetime.now()
        the_input = input("")
        if the_input.lower() == first_key and datetime.now()<=start + timedelta(seconds = 5):
            the_dice = die(1,6)
            if the_dice == 1 or the_dice == 2 or the_dice == 3:
                print_slow(bad_first_way)
                #global spider_distance
                #spider_distance += bad_first_distance + extra_distance
                return bad_first_distance + extra_distance
                break
            else:
                print_slow(good_first_way)
                #global spider_distance
                #spider_distance += good_first_distance + extra_distance
                return good_first_distance + extra_distance
                break
        elif the_input.lower() == second_key and datetime.now()<=start + timedelta(seconds = 5):
            print_slow(second_way)
            #global spider_distance
            #spider_distance += good_first_distance + extra_distance
            return second_distance + extra_distance
            break
        else:
            print_slow("You took too long or picked an unavailable action. The spider gets closer")
            extra_distance += 1
            continue            
def choose_roll2(func):
	global spider_distance
	spider_distance += func
def choose_roll(all_choose_roll_lists):
    choose_roll2(choose_roll1(all_choose_roll_lists))

combined_list = [functools.partial(evading,w1), functools.partial(evading,w2), functools.partial(evading,w3), functools.partial(evading,w4), functools.partial(evading,w5), functools.partial(evading,da1), functools.partial(evading,da2), functools.partial(evading,da3), functools.partial(evading,da4), functools.partial(evading,a1), functools.partial(evading,d1), functools.partial(evading,s1), functools.partial(evading,s2), functools.partial(choose,updown1), functools.partial(choose,rightleft3), functools.partial(choose,rightleft4), functools.partial(choose_roll,updown2), functools.partial(choose_roll,updown3), functools.partial(choose_roll,rightleft1), functools.partial(choose_roll,rightleft2), functools.partial(choose_roll,rightleft5), functools.partial(choose_roll,rightleft6)]  
random.shuffle(combined_list)
final_list = combined_list[0:15]

def big_spider_full():
    spider_distance = 0
    spider_dmg = 10
    spider_attacks = 0
    for events in final_list:
        if spider_distance >= 5:
            print_slow("The spider has caught up with you.\n")
            spider_attacks +=1
            if spider_attacks == 5:
                print_slow("After the spider has injured you so many times, it manages to catch up with you for real this time.\nIt webs you completely, and eats you alive.\n")
                print_slow("*But it is not over yet. There is a slim chance for survival*\n")
                if die(1,6) == 6:
                    print_slow("Luckily, while going into the spider's throat, some of the web around you got cut off by the spider's teeth.\nOn you way to the stomach, you manage to break free and ")
                    if class1.what_class == "Mage":
                    	print_slow("use your magic to break out the spider's insides.\n")
                    elif class1.what_class == "Fighter":
                    	print_slow("carve yourself out of the spider's insides with your sword.\n")
                else:
                	print_slow("Unfortunately, you didn't make it. You die in the spider's stomach.\n")
                	sys.exit()
            class1.lose_hp(spider_dmg)
            print_slow(f"The spider deals {spider_dmg} damage. You now have {class1.hp} hp left.\n")
            spider_dmg = round(spider_dmg * 1.5)
            spider_distance -= 5
            print_slow("After attacking you the spider has to wait a bit to regain its strength.\n")
            input("...")
        events()
        input("...")

  

print_slow("You can either choose to be a mage or a fighter.\n")
print_slow("A mage has medium health, and require mana to use spells. As a mage you have 2 spells,\n1 basic attack, and the ability to regain mana\n")
print_slow("A mage has these moves:" + "\n")
print_slow("fireball - this has high damage, can do damage over time (stack in time - not damage), but there is a small risk of self harm (costs 25 mana)" + "\n")
print_slow("ice spike - medium damage, medium mana cost. chance to slow the enemy, so you get an extra turn (cost 15 mana)" + "\n")
print_slow("staff hit - this has low damage, but does not cost any mana" + "\n")
print_slow("regains mana - regains 15 mana" + "\n")
input("...")
print_slow("A fighter has high health, and increased chance to go first in combat" + "\n")
print_slow("They have 2 armed moves, and 2 unarmed moves." + "\n")
print_slow(f"if your tiredness reaches 3, you will not be able to perform armed moves" + "\n")
print_slow("You can increase your tiredness threshold throughout the game" + "\n")
print_slow("The fighter has rage. If your rage reaches 100, your next attack will do double damage." + "\n")
print_slow("You gain rage from dealing damage, and lose it when you are done with a fight." + "\n")
print_slow("The ammount of rage gained and lost is random." + "\n")
print_slow("A fighter has these moves:" + "\n")
print_slow("sword hit - high damage, makes you very tired. This will hit more enemies if possible. Damage is increased based on\nnumber of enemies" + "\n")
print_slow("shield bash - low minumum damage, high maximum damage, makes you a little tired." + "\n")
print_slow("headbutt - High unarmed damage - no increased tiredness. a chance to hit your head and do self harm" + "\n")
print_slow("kick - basic unarmed attack - no increased tiredness." + "\n")
while True:
	global class1
	class1 = input("Choose your class: (Fighter, Mage) ")
	if class1 == "Fighter" or class1 == "fighter":
		class1 = Fighter(name)
		break
	elif class1 == "Mage" or class1 == "mage":
		class1 = Mage(name)
		break

def intro():
	input("Press 'enter' to continue when you see '...'	")
	print_slow("Once upon a time there was peace in all of the Kingdom of Enderal. ")
	print_slow("This all changed when the evil Drackle came. ")
	print_slow(" \nWith his army of Orcs, he wrecked havoc in all of Enderal, starting with the small villages," + "\n" "progressing through the towns and cities")
	print_slow("\nFinally he seized control of Enderal, by imprisoning the great King Jack," + "\n" "and killing his trusted bodyguards, and noble followers" + "\n")
	print_slow("It seems all hope was lost, and the Kingdom of Enderal lived like this for a long time.")
	print_slow("\n" + " ...")
	print_slow("30 years later" + "\n")
	print_slow("In the town of Bournemouth, a small chance of hope was born")
	input(" ...")
	print (f"He was a {class1.what_class}")	
	print_slow(f"His name was {name}. He lived as a farmer until the age of 18, without any idea how important he was." + "\n" "At age 18 he found out that he had special powers, allowing him to do what most men could not." + "\n")
	print_slow("On his 18th birthday, it was the end of the month, and Drackle had sent his men to claim what the farmers have earned" + "\n")
	print_slow(f"When they arrived at the farm, {name} and his family were celebrating {name}'s birthday." + "\n" "They did not notice the dark men on horseback at first." + "\n")
	print_slow(f"'Well, well, well. Wait till the Boss finds out that you do not work on your working hours." + "\n" f"He drew his sword, and pointed at the {name}'s mother" + "\n")
	print_slow(f"2 of the other men, jumped down from their horses, and grabbed the mother," + "\n" f"forcing her hand on the stomp next to where {name}'s family was seated" + "\n")
	print_slow("'You know the cost of this', he said, raising his left pinky finger above the other fingers." + "\n" "Now he went down from the horse, moving towards the stump." + "\n")
	print_slow(f"He knew that he could not do anything to prevent what would happen, but when her finger was cut clean off," + "\n" f"and {name} heard her screams, he jumped from his seat" + "\n")
	input("...")
	if class1.what_class == "Mage":
		print_slow ("The ground started rumbling, and a big storm breaks out." + "\n")
		print_slow (f"When {name} points his arm at one of the guards holding his mother, a big lightning hits the guard," + "\n" "and he is reduced to ashes." + "\n")
		print_slow ("He then throws a big ball of fire on the second guard, making him burst into flames." +"\n" "For the first few seconds he screams, but it quickly stops when he falls to the ground shortly after." + "\n") 
		print_slow ("Now you look at the man who cut off your mothers finger, you drain all lifeforce of everything around you," + "\n" "as plants near you starts rotting" + "\n")
		print_slow (f"{name} then throws a mix of ice, fire, and lightning at the man, making him freeze, burn, and electrocute to death." + "\n")
	elif class1.what_class == "Fighter":
		print_slow ("You are now full of rage, as you pick up a rock from the ground and throws it at one of the the guards. \nHe falls to the ground instantly" + "\n")
		print_slow ("You then walk over to the man who cut your mother's finger off. \n You look him dead in the eyes, kick him and then headbutt him." + "\n")
		print_slow ("He is still standing, but not for long as you hit him with the meanest right hook ever seen in Enderal. \nHe falls to the ground." + "\n")
		print_slow ("The last guard starts trembling. He runs away, hoping to escape your anger." + "\n")
		print_slow ("On the ground, you spot a fairly large and pointy stick. \nYou put your finger in the air to check the wind speed, and you then throw the big stick" + "\n")
		print_slow ("Seconds later, the man suddenly stops running. \nHe falls to the ground, and even though he is far away, you still manage to hear his screams." + "\n")

	print_slow(f"After this was over, {name} collapsed, and lost almost all of his powers." + "\n")
	print_slow("A week later, he wakes up, sure of what he shall do next. He remembers old tales, his mother told him of the evil \nDrackle, and his army of orcs. He knows he have to defeat him. With great power comes great responsibility." + "\n")

allies_with_woodelves = ""
enemies_with_woodelves = ""
dark_elf_dead = False
last_chance_luck = False
def level1():
	attack_first = ""
	print_slow(f"On his path to Ark - the capital of Enderal, and the home of Drackal - {name} reaches a crossroad." + "\n" "He needed to go East, but there was mountains blocking his way.")
	input(" ...")
	print_slow("He can now either go through the forest to the North East," + "\n" "or to the South East through the mines - he stops for a moment and wonders where to go ..." + "\n")
	lvl1_stage1 = True
	while lvl1_stage1:
		formin = input("Where do you want to go, Forest or Mines? ")
		if formin == "Forest" or formin == "forest":
			print_slow(f"*{name} has entered the forest*\n")
			print_slow("When arriving at the forest, you see a nice path to follow leading deep into the forest\n")
			print_slow("You walk on the path for a few minutes, but suddenly you see a corpse lying on the side of the road.\n")
			print_slow("It looks almost human, but its ears are pointy, and he is very pale.\n")
			print_slow("He also looks very big, and has green armor on.\n")
			print_slow("You bow down and see that he has a crumbled note in his hand. You pick it up, and read it:\n")
			print_slow("*They attack at midnight from west*\n")
			print_slow("You put the note in your pocket, and when you stand up, and look forward to proceed towards your goal, \nyou see a big figure standing right in front of you. \n")
			print_slow("He looks very similar to the one on the ground, except his armor looks slightly thicker, \nand this one is very much alive.\n")
			print_slow("   'Hello. Welcome to the grand birchwood forest.'\n")
			print_slow("   'My name is Aegar, and I am a wood elf. '\n")
			print_slow("He starts searching through the dead elf's pockets, and then looks up with a sigh.\n")
			print_slow("   'I don't suppose you noticed if he had anything on him - A note or something?'\n")
			print_slow("   'You see we are at war with the dark elves. The one you see on the ground here is on of our scouts.'\n")
			print_slow("   'He was supposed to gather knowledge about them, but it doesn't look like he has any information on him.'\n")
			print_slow("   'So this leads back to my question before. \n   'Also, I saw you bowing down in front of him, so I was wondering why you did that.'\n")
			Aegar_talk = ""
			while Aegar_talk != "1" and Aegar_talk != "2" and Aegar_talk != "3":
				Aegar_talk = input("\n" + "Dialogue (1/2/3/4):" + "\n" "1 = 'I found this note.' *show note* " + "\n" + "2 = 'I haven't seen an elf before. I was curious as to how he looked. I didn't find anything on him. *keep note*" + "\n" + "3 = *attack Aegar*" + "\n" + "4(question) = 'Can you tell me more about this battle you have with the dark elves?'" + "\n")
				if Aegar_talk == "4":
					print_slow ("no.\n")
			input("...")
			if Aegar_talk == "1":
				print_slow("    'Hmmm, let me see that...'")
				print_slow("    'Oh, I have to hurry back, and inform the others.'' \n    'Thank you kind sir, I will tell the other wood elves that you are to be trusted'\n")
				print_slow("He shakes your hand firmly, turn around, and walk away from you.\n")
				global allies_with_woodelves
				allies_with_woodelves = True
			elif Aegar_talk == "2":
				print_slow("    'Okay, guess he didn't find anything.\n")
				print_slow("    'Anyway, I need to get back to the others.\n")
			elif Aegar_talk == "3":
				Aegar_enemy.appearing()
				class1.attack(Aegar_enemy)
				a_fight_no_fightflee(class1,Aegar_enemy,True)
				input("...")
				print_slow("After killing this Aegar, you notice something that looks like a very powerful ring on his finger.\n")
				if class1.what_class == "Mage":
					print_slow ("It is the ring of magic. This will permantly increase your spellpower.\n")
				elif class1.what_class == "Fighter":
					print_slow ("It is the ring of strength. This will permantly increase your attack damage.\n")
				Aegar_ring = ""
				while Aegar_ring != "y" and Aegar_ring != "n":
					Aegar_ring = input("Do you want to put the ring on - yes or no? (y/n) ")
				if Aegar_ring == "n":
					print_slow ("You decide to not put on the ring. pretty stupid choice honestly.\n")
				elif Aegar_ring == "y":
					if class1.what_class == "Mage":
						print_slow ("You put on the ring. \n")
						class1.spellpower += 0.1
						print_slow(f"Your spellpower is permantly increased by 0.1 and is now at {round(class1.spellpower)}\n")
					elif class1.what_class == "Fighter":
						print_slow ("You put on the ring. \n")
						class1.attackdmg += 0.1
						print_slow(f"Your attack damage is permantly increased by 0.1 and is now at {round(class1.attackdmg)}\n")
				print_slow("You rise from his bloody corpse. You look at your two bloody hands standing next to 2 elven corpses.\n")
				print_slow("You sigh, and looks up at the sky. From the corner of your eye, you spot another wood elf.\n")
				print_slow("The two of you gets eye contact, and after looking at the two corpses beneath you, he runs away.\n")
				print_slow(f"'Let us hope you do not meet any other wood elves' {class1.name} thought to himself.\n")
				global enemies_with_woodelves
				enemies_with_woodelves = True



			input("...")
			print_slow("You continue through the forest.\n")
			print_slow("After walking for what feels like a very long time, you come accross a crossroads.\n")
			print_slow("It looks like you have to go either go right through a bushy road, or left through a clearer road.\n")
			crossroads_forest = ""
			while crossroads_forest != "1" and crossroads_forest != "2":
				crossroads_forest = input("Do you want to go left (bushy road) or right (clear road) (1 = left, 2 = right)? ")
			if crossroads_forest == "1":
				print_slow("You choose the bushy road to the left. \n")
				print_slow("After taking the first few steps you already regret walking this densely bushed road.\n")
				print_slow("After walking for around 10 minutes without making any real progress, \nbecause of the heavy bushed path, you feel the ground underneath you letting go. \n")
				print_slow("It seems someone has made a big hole and covered it with branches and leaves, and since it's so bushy, \nyou didn't notice a thing before it's too late. \n")
				print_slow("Almost too late! Luckily your instincts have increased along with you abilities, when turning 18.\n")
				print_slow("Roll the dice to see how you've fared!\n")
				trap1 = die(1,6)
				if trap1 == 1 or trap1 == 2 or trap1 == 3:
					print_slow("It seems you instincts aren't that good. You try to grab the ledge, but fail.\n")
					print_slow("While falling your life starts flashing before your very eyes. Luckily you land in a big pool of water.\n")
					print_slow("It is very dark, but you can see a dim light ahead of you, so you swim towards it.\n")
					print_slow("You suddenly feel a ledge with your hands, and pull yourself up.\n")
					print_slow("You get closer to the light source, and see that it is a torch. Not a particular good one.\n")
					print_slow("You grab the torch and continue on your way through the cave.\n")
					print_slow("You keep walking for a while longer, until suddenly ...\n")
					print_slow("*Crunch*\n")
					print_slow("You look down and put the torch towards the ground, you stepped on some sort of white stick.\n")
					print_slow("You bend down to have a closer look, and notice that it is in fact a human bone.\n")
					print_slow("You look up again, and spot 2 skeleton-type creatures looking at you with bones in their hands.\n")
					class1.attack(skeletal_trap1)
					a_fight(class1,skeletal_trap1)
					print_slow("You look around to see if there are anymore skeletals in here.\n")
					print_slow("You don't really spot any so decide to move on through the cave.\n")
					print_slow("You move further and suddenly spot a door leading somewhere.\n")
					print_slow("It is really dark, and as you take your first step forward, you realize there is no ground underneath you.\n")
					print_slow("You fall down and down, until you finally hit some water. You can feel the deja vu.\n")
					print_slow("The area is blocked ahead of you, so you swim a bit the other way.\n")
					print_slow("Now that way is also blocked. You look hopelessly around, but manage to spot some light below you.\n")
					print_slow("You take a deep breath and follow the light. After some diving, you look up, and see the light.\n")
					print_slow("You swim up there, jump out the water, and move forward.\n")
					print_slow("You enter a massive part of the cave, and to your right way off in the distance, you spot a ruin.\n")
					print_slow("It looks like there is no other way through the cave than through the ruin.\n")
					print_slow("You sigh, but continue towards the ruin.\n")
					print_slow("When arriving at the ruin you see a trail of blood leaving to the right of the ruin.\n")
					ruin1 = ""
					while ruin1 != "1" and ruin1 != "2":
						ruin1 = input("You want to try and follow the trail or not (1 = follow, 2 = don't follow) ")
					if ruin1 == "1":
						print_slow("You turn to the right, and start following the trail of blood.\n")
						print_slow("You keep your senses hightened, and try to prepare for everything.\n")
						print_slow("You turn around a corner, and see something that looks like smaller person.\n")
						print_slow("He looks dead. You walk a bit closer...\n")
						input("...")
						print_slow("*cough, cough*, To your surprise, he is not dead.\n")
						print_slow("He looks at you, with a surprised face, slowly turning into a worried one.\n")
						print_slow("    'What... you ... doing here?'\n")
						print_slow("'What's happened? Who are you? WHAT are you?'\n")
						print_slow("    'I, dwarf. this... Dwarven castle was.' He coughs of some blood.\n")
						print_slow("    'We live... peace. Then. mo-monster.\n")
						print_slow("    'Everyone. Everyone dead.\n")
						print_slow("    'Don't. inside. Inside only death.\n")
						input("...")
						print_slow("'But there is no other way through. I have to go here', you respond.\n")
						print_slow("    'Then. Come. whisper.\n")
						print_slow("*You bow down and put your ear to his mouth*\n")
						print_slow("    'Aim. for. eyes.', he whispers and collapses.\n")
						input("...")
						print_slow("You return to the ruin.\n")
						#increase attack damage
						minotaur_weakness = True
						input("...")

					print_slow("You take your first step into the ruin. You feel shivers running down your spine.\n")
					print_slow("You look around, but cannot see anything - or anyone.\n")
					if minotaur_weakness:
						print_slow("The dwarf was right about everyone being dead - or gone at least.")
					print_slow("You cannot see anywhere to go, except some stairs leading down.\n")
					print_slow("You take your chances and go downstairs.\n")
					print_slow("It's very quiet, and very dark downstairs.\n")
					print_slow("You can see a bit ahead though, and you spot a door a few meters ahead of you.\n")
					print_slow("You take a deep breath and open the door.\n")
					print_slow("This room is very light. You see a creature standing in the middle of the room.\n")
					if minotaur_weakness:
						print_slow("This must be the monster that the dwarf spoke of.\n")
					print_slow("It looks fairly humanoid, although it has horns and is about 3 meters tall.\n")
					print_slow("In its hands it has a massive great axe.\n")
					print_slow("BANG\n")
					input("...")
					print_slow("The door closes behind you. Looks like there is no turning back now.\n")
					print_slow("The monster turns around and looks at you with eyes red as blood.\n")
					if minotaur_weakness:
						print_slow("You remember what the dwarf told you. Aim for the eyes.\n")
						if class1.what_class == "Fighter":
							print_slow(f"Your attack dmg is temporarily (in this battle only) increased by 0.5. it is now at {round(class1.attackdmg)}\n")
							class1.attackdmg += 0.5
						elif class1.what_class == "Mage":
							class1.spellpower += 0.7
							print_slow(f"Your spell power is temporarily (in this battle only) increased by 0.7. it is now at {round(class1.spellpower)}\n")
					Minotaur_trap1.appearing()
					a_fight_no_fightflee(class1,Minotaur_trap1)
					if minotaur_weakness:
						if class1.what_class == "Fighter":
							class1.attackdmg -= 0.5
						elif class1.what_class == "Mage":
							class1.spellpower -= 0.7
					print_slow("You did it. it was a tough battle, but you made it.\n")
					print_slow("You look around the room, for a way out of this shithole.\n")
					print_slow("Although you can't see any way out, you now notice why it was so empty upstairs.\n")
					print_slow("Down here you spot 100 - at least - dead dwarves. There is blood everywhere.\n")
					print_slow("While looking through this wrecked and bloody place, one thing really catches your eye.\n")
					print_slow("Directly to the left of you, you spot one single dwarf. It looks like he is holding something in his hand.\n")
					print_slow("When you walk closer, you notice a section of the wall behind him looks different to the rest of the wall.\n")
					print_slow("You grab his arm and see that what he was holding was in fact a note.\n")
					print_slow("You pick it up, and notice how it is not whole.\n")
					input("...")
					print_slow("You look at it. It looks like this:\n")
					note1()
					print_slow("You look at his other hand. You can see that it is stretched really far to the upper right.\n")
					print_slow("It almost looks like he is pointing at something.\n")
					print_slow("Taking a closer look, he is pointing at a rock that looks somewhat different to the other's.\n")
					print_slow("You put your hand up to feel it, and suddenly the wall starts collapsing.\n")
					print_slow("You look around, and notice nothing is happening to the other walls. It's only this one section of the wall.\n")
					print_slow("When you look back, the wall is gone, and there are stairs leading further down.\n")
					ruin2 = ""
					while ruin2 != "1" and ruin1 != "2":
						ruin2 = input("Do you want to go down the stairs or not (1 = go down, 2 = don't go down)? ")
					if ruin2 == "1":
						print_slow("You descend the stair. This leads you to a well lit room.\n")
						print_slow("On the far end, there is a door.\n")
						print_slow("Between you and the door, there are some giant stone tiles - 18 exactly.\n")
						print_slow("They have letters on them - except one - and form a grid.\n")
						print_slow("It kinda looks like a puzzle.\n")
						input("...")
						print_slow("This is what it looks like:\n")
						ground(letter)
						print_slow("Every stone on the grid looks like a pressure plate.\n")
						print_slow("*You will now see everything from a 3rd person view. You are the X.\nYou start by typing which of the letters you want to start at.\nWhen you have done that, you move with wasd (w = forward, d = right, a=left, s=backwards).\nYou can also press n, to see the note at any time.*")
						puzzle1()
						print_slow("You now reach a wall, that has a bunch of letters on it.\n")
						print_slow("It looks like this:\n")
						ground2(letter1)
						print_slow("On the ground you notice 2 bricks that are exactly the same size as each brick with a letter on on the wall.\n")
						print_slow("One is labelled '1', the other '2'. You reckon that these fit exactly on to those on the wall.\n")
						print_slow("The problem is which one do they go on. There is a lot of options here.\n")
						print_slow("You look around you, searching for clues, but you don't notice anything.\n")
						print_slow("You almost give up, but when the note from before drops out of your pocket, you notice something on the back of it.\n")
						print_slow("Unfortunately the fact that the note is not whole is a factor now, \nas the sribbled notes are in each corner, obviously missing something.\n")
						print_slow("Anyway, this is all you have. It has to be enough.\n")
						print_slow("The note looks like this:\n")
						ground2(letter1)
						puzzle2start = ""
						while puzzle2start != "1" and puzzle2start != "2":
							puzzle2start = input("Which number would you like to start with (1 or 2)? ")
						done = False
						while not done:
							letter2 = {"D":["","D","W","H","C","A","Q"], "F":["","F","Z","G","V","H","T"], "G":["","G","R","R","B","Q","F"], "H":["","H","D","D","A","F","G"], "J":["","J","Y","Z","M","P","R"], "Q":["","Q","J","X","K","O","E"]}
							letter2_copy = letter2.copy()
							if puzzle2start == "1":
								if puzzle2(1,2) == True:
									done = True
							elif puzzle2start == "2":
								if puzzle2(1,2) == True:
										done = True
						print_slow("The numbers start glowing, and the wall splits up in the middle.\n")
						if class1.what_class == "Fighter":
							print_slow("You now see a golden chestplate in front of you.\n")
						elif class1.what_class == "Mage":
							print_slow("You now see an armored leather rope. It looks not too heavy, but still more tough than the one you are wearing.\n")
						puzzle_armor = ""
						while puzzle_armor != "1" and puzzle_armor != "2":
							puzzle_armor = input("Would you like to put it on or not (1 = yes, 2 = no)")
						if puzzle_armor == "1":
							print_slow("You put on the armor.\n")
							class1.maxhp += 40
							print_slow(f"*Your max hp has increased by 40. It is now at {class1.maxhp}*")
						print_slow("You turn around, and notice that the pressure plates with letters from the first puzzle is gone.\n")
						print_slow("You walk out from where you came from to continue your journey.\n")
						print_slow("You are now back in the bigger room with the dead minotaur and the hundreds of dead dwarves.\n")

					print_slow("You look around you once more, trying to find a way out and to the left of you, you spot a door.\n")
					print_slow("'This must lead out', you think to yourself.\n")
					print_slow("You open the door and spot a ladder leading up further than the eye can see.\n")
					print_slow("After what feels like an eternity, you finally make it up the ladder.\n")
					print_slow("You are now back on the densely bushed road.\n")
					print_slow("You proceed on your way out of the forest.\n")
					print_slow("You feel very tired, but decide to keep walking anyways.\n")
					print_slow("This turns out to be a bad idead, because after taking another step, you feel a line tightening.\n")
					print_slow("'ahh fuck, not agai...'\n")


					
					#man bevæger sig ind i en slags ruin
						
						#slags boss: minotaur
						#senere - få et puzzle ind man skal solve - uncharted style
							#skal give noget loot - måske rustning så man får mere liv.
						
				else:
					if trap1 == 4:
						print_slow("You manage to grab the ledge, but hit your head in the process.\n")
						print_slow("'Whew' you think to yourself, although you feel a heavy pain in your head.\n")
						class1.lose_hp(15)
					else:
						print_slow("Your instincts really have improved. You managed to grab the ledge, and pick yourself up fairly easily.\n")
						print_slow("'Crisis averted' you think to yourself. You continue on your way out the forest.\n")
						print_slow("Let's hope you won't run into any more traps.\n")
					print_slow("You continue on your way out the forest.\n")
					print_slow("After walking a little while longer, the bushes start getting further away from each other.\n")
					print_slow("'Ahhhh' you say to yourself, finally you can actually see where you are going.\n")
					print_slow("You take one more step and can feel a line tightening in the middle of your step.\n")
					print_slow("'Ahhh shi...'\n")
				trap2 = die(1,6)
				if trap2 == 1 or trap2 == 2 or trap2 == 3:
					print("From underneath you, a net starts assembling. You did not react in time to avoid being caught in it.\n")
					if class1.what_class == "Mage":
						print_slow("You start preparing a fireball to help you get out of this net.\n")
					elif class1.what_class == "Fighter":
						print_slow("You grab your sword, and start trying to cut the net.\n")
					print_slow("    'I wouldn't do that if I were you', you suddenly hear a voice say.\n")
					print_slow("    'That would indeed be very unwise', this is coming from the opposite direction.\n")
					print_slow("You look down and see 2 big trolls.\n")
					print_slow("    'Finally some proper meat. I am getting so tired of this elven meat'\n")
					response1 = ""
					input("...")
					print_slow("*You now have to write your response when replying to the trolls. \nCertain keywords in your text may be caught, and act as a response. Use lower case letters only.\nIf it does not find any keywords, you will have a bad response, and it will not be good for you in the long run.\nAfterwards you roll a dice to see how you have fared.*\n ")
					regretresponse = True
					input("Press enter, and then type your answer and then press enter again.")
					while True:
						response1 = input("What is your response to the trolls. How do you convince them not to eat you?")
						response1_roll = die(1,6)
						if "poison" in response1 or "sick" in response1:
							if response1_roll != 1 or response1_roll != 2:
								print_slow("	'Zolkaz! I really don't want to eat poisonous meat.'\n ")
								print_slow("	'I know, Udefrykte, but we haven't had anything besides elf for the last month.'\n")
								print_slow("	'Besides. He may be lying just get out of this.'\n")
								print_slow("	'Are you lying, little human? what happens if we eat you?'\n")
								poisonresponse = input("What is your response to this? ")
								poison_roll = die(1,7)
								if "heart" in poisonresponse:
									if poison_roll != 1:
										print_slow("	'Our hearts will what? Stop? I really think we should let him go now, Zolkaz'\n")
										print_slow("	'You are right, Udefrykte. Just cut him down. We have a few elves back in the hut anyway'\n")
										succes = True
										break
									else:
										print_slow("	'Our hearts will stop? What are you on about. The only heart that will stop is yours, when we are done eating'\n")
										succes = False
										break
								elif (("turn" or "transform" or "become") and "human") in poisonresponse:
									if poison_roll != 1 or poison_roll != 2:
										print_slow("	'Ew. Zlkaz, I really don't want to turn into that thing'\n")
										print_slow("	'If eating him will make us into humans we will not do that. Set him free, Udefrykte'\n")
										succes = True
									else:
										print_slow("	'Transform into humans? but when we ate elves we didn't transform into elves'\n")
										print_slow("	'I see your point, Udefrykte. I think he is lying. Prepare the fire; we are having human today'\n")
								elif "infect" in poisonresponse or "parasite" in poisonresponse:
									if poison_roll != 1 or poison_roll != 2 or poison_roll != 3:
										print_slow("'	I really don't want to be infected, Zolkaz. Remember what happened to Kraslos.\n")
										print_slow("'	That's probably just an old troll's tale. But one cannot be too sure. Set him free, Udefrykte\n")
									else:
										print_slow("	'Hmmm. Infected you say. I have heard that boiling the meat prevents that. Let's eat him, Udefrykte\n")
										print_slow("	'Can we boil him a little extra to be sure then?'\n")
										print_slow("	'Ok, not too much. I am getting pretty hungry'\n")
										succes = False
										break
								else:
									last_chance_luck = True
									break

								succes = True
								break
							else:
								print_slow("	'Poisonous? How stupid do you think we are. Let's eat him, Udefrykte.")
								succes = False
						elif ("regret" in response1 or "mistake" in response1) and regretresponse == True:
							if response1_roll == 4 or response1_roll == 5 or response1_roll == 6:
								print_slow("	'Regret eating you, you say. Why is that, puny human?'\n")
								regretresponse = False
								#breaker ikke, men man får en chance til
							else:
								print_slow("'	Regret eating you? You are merely a small pestilence going through our system. Prepare the fire, Udefrykte'\n")
						elif "not alone" in response1 or "friends" in response1:
							if response1_roll == 5 or response1_roll == 6:
								print_slow("	'What friends? I don't see any. What about you, Udefrykte?\n")
								print_slow("	'No, he is the only one here. But what if he is telling the truth?'\n")
								print_slow("	'We can ask him. What kind of friends do you have out here tiny human?'\n")
								friendresponse("What is your response to this?\n")
								friendsroll = die(1,7)
								if "wizard" in response1 or "warrior" in response1 or "fighter" in friendresponse:
									if friendsroll != 1:
										print_slow("	'We are not messing with those people. Let him go immediately, Udefrykte!'\n")
										print_slow("	'But Zolkaz. He could be lyi ...'\n")
										print_slow("	'Enough, Udefrykte. Let him go now. It is not worth the risk'\n")
										succes = True
										break
									else:
										print_slow("	'We will not be messing with those type of people. Udefrykte, Let him g- .. wait a minute'\n")
										print_slow("	'What is it, Zolkaz'\n")
										print_slow("	'He is lying, Udefrykte. I can see it in his eyes. He is alone. Look at him.'\n")
										succes = False
										break		
								elif "elf" in response1 or "elves" in response1:
									if friendsroll != 1 or friendsroll != 2 or friendsroll != 3:
										print_slow("	'Elves? Remember when we stumbled upon that group of elves, Zolkaz? We barely made it out alive'\n")
										print_slow("	'I know. But how can we be sure. and we don't even know how many there are '\n")
										print_slow("	'Please Zolkaz. Let us just give him back to the elves. Maybe we can tell the human to talk to the elves '\n")	
										print_slow("	'Okay. We will let you go. But tell the elves we don't want to fight them - except when we have no dinner '\n")
										succes = True
										break
									else:
										print_slow("	'Elves? We have killed plenty of elves. And why would they even help you. You're just a human\nPrepare the cauldron, Udefrykte. We are having human today'")
										succes = False
										break
								elif "human" in response1 or "mates" in response1:
									if friendsroll == 4 or friendsroll == 5 or friendsroll == 6:
										print_slow("	'Other humans. Zolkaz, I have heard that humans are not worth much on their own, but together they can be quite scary'\n")	
										print_slow("	'I'm not sure, Udefrykte. Look at him. he doesn't look that terrifying does he?\n")
										print_slow("	'Can we please just let him go. I don't want to risk it\n")
										print_slow("	'Okay Udefrykte. But only because we have a shed full of elves'\n")
										succes = True
										break		
									else:
										print_slow("	'Other humans? If they are as weak and tiny as you we will be fine. Even if you are in fact telling the truth.'\n")
										print_slow("	'Yea, That's just more food for us, right, Zolkaz'\n")
										print_slow("	'Right, Udefrykte. Start the fire'\n")
										succes = False
										break
								else:
									last_chance_luck = True	
									break	
							else:
								print_slow("	'I don't see or smell any other nearby. I think he is lying, Udefrykte'\n")
								print_slow("	'I think you are right, Zolkaz. Let us just eat him. I'm hungry anyways'\n")
						elif "vegan" in response1 or "vegetarian" in response1:
							if response1_roll == 6:
								print_slow("'	Stop eating meat you say. You may be right about that. How does that help us?'\n")
								veganresponse = input("What is your response to this?")
								veganroll = die(1,8)
								if "heart" in veganresponse or "healthy" in veganresponse:
									if veganroll == 1 or veganroll == 2 or veganroll == 3:
										print_slow("'	We might live longer if we are a bit healthier, Zolkaz.'\n")
										print_slow("'	Hmpf. We are trolls. Eating meat is what we do. '\n")
										print_slow("'	But maybe we should try it. Just for some time. We'll see how it feels'\n")
										print_slow("'	Okay, but we can still kill weak creatures. We let this one go, but next one is mine '\n")
										succes = True
										break
									else:
										print_slow("'	We don't need to be healthier. We are trolls. We do not listen to weaklings like you. \nPrepare the fire, Udefrykte '\n")
										succes = False
										break
								elif "happy" in veganresponse or "mood" in veganresponse:
									if veganroll == 1 or veganroll == 2:
										print_slow("'	You do look a bit unhappy, Zolkaz.'\n")
										print_slow("'	Hmpf. Don't listen to this human, Udefrykte. He is just saying what he can to survive'\n")
										print_slow("'	But Zolkaz. I feel like we should try it. It's worth a shot. Even for a troll you look pretty sad.\n")
										print_slow("'	We will try it. But only today. Udefrykte, let him go'\n")
										succes = True
										break
									else:
										print_slow("'	Are you hearing what he is saying, Udefrykte? You think I need your happines?\nYou know what would make me happy. Killing and eating you will put me in a great mood'\n")
										print_slow("'	Why have we not killed him yet, Udefrykte? I'm tired of listening to this weakling's lies'\n")
										succes = False
										break
								elif "environment" in veganresponse or "climate" in veganresponse:
									if veganroll == 1:
										print_slow("'	There have been less animals lately. \nYou know, Zolkaz; usually I would see many animals, but this morning I saw none'")
										print_slow("'	fewer*, but you are right about that, Udefrykte. That is why I am so hungry now.'\n")
										print_slow("'	But maybe if we tried eating fewer meat, there will be more meat. And then we can eat more meat'\n")
										print_slow("'	less*, but okay. We will let him go. Go on, Udefrykte'\n")
										succes = True
										break
									else:
										print_slow("	'You think we care about the environment? We are trolls. I will not listen to this lesser being anymore. Udefrykte, let's eat him '\n")
										succes = False
										break
								else:
									last_chance_luck = True
									break

							else:
								print_slow("	'Stop eating meat!? Udefrykte have you ever heard something that stupid.\nAre you taking us for idiots'\n")
								print_slow("	'Shall I prepare the cauldron, Zolkaz?'\n")
								print_slow("	'Yes, Udefrykte, and do not add anyhing other than meat. Not eating meat ... I have heard everything now'\n")
								succes = False
								break
						else:
							succes = False
							break
					if succes == False:
						input("...")
						print_slow("	'The cauldron is ready now, Zolkaz. We only need the last ingredients '\n")
						print_slow("One of the trolls, Zolkaz, approach you, with a pretty big knife in his hand.\n")
						print_slow("Just as he is about to cut you down, you give one last shot at coming out of this alive.\n")
						print_slow("'But what's the fun in just killing and eating me in cold blood. Shouldn't I at least get a chance to fight back, you say.\n")
						print_slow("The trolls look at each other, uncertain at what to say or do.\n")
						print_slow("Roll the dice to determine the trolls reaction, and thereby decide your faith")
						if last_chance_luck:
							last_chance = die(1,6)
						else:
							last_chance = die(1,5)
						if last_chance == 1:
							print_slow("	'I'm tired of your tricks little human. Just die knowing that you will make a great supper for me and Udefrykte '\n")
							sys.exit()
						print_slow("	'Fight back? Haha, don't make us laugh. But okay, we will give you a chance. Cut him down, Udefrykte '\n")
						Udefrykte_Zolkaz.appearing()
						a_fight_no_fightflee(class1,Udefrykte_Zolkaz)
						print_slow("After killing the trolls, you go to spot some vials near the cauldron.\n")
						print_slow("You decide to take a closer look.\n")
						hppot_trolls = Potion("large","hp",50)
						hppot_trolls.new_potion()
						potion_action(hppot_trolls)
						if class1.what_class == "Mage":
							manapot_trolls = Potion("small","mana",40)
							manapot_trolls.new_potion()
							potion_action(manapot_trolls)
						elif class1.what_class == "Fighter":
							hppot_trolls2 = Potion("small","hp",20)
							hppot_trolls2.new_potion()
							potion_action(hppot_trolls2)
					print_slow("You move on from the trolls, and continue on your way out the forest.\n")

						

				else:
					if trap2 == 4:
						print_slow("A net starts assembling underneath you, but you manage to react to it and move out the way. \nAlmost!\n")
						print_slow("You manage to move your body out the way, but your foot is stuck in the net.\n")
						if class1.what_class == "Mage":
							print_slow("You quickly make a small fireball and hit the net to get down from the trap")
						elif class1.what_class == "Fighter":
							print_slow("You get your sword out and cut the rope trap holding your leg.\n")
						print_slow("You fall to the ground but manage to bow your head. Your hit the ground directly on your shoulder.\n")
						class1.lose_hp(20)
						print_slow("You can hear deep voices coming from the wood, so you pick up the pace and continue on your way.\n")
					else:
						print_slow("A net assembles under you, but your quick reactions mean that you manage to roll beautifully out the way.\n")
						print_slow("Nothing good can come out of staying here for too long, so you pick up the pace, and continue on your way out.\n")
		
				input("...")
				print_slow("You made it out of the densely bushy road. \nYou can see to the right the end of where the other road would have led you.\n")


			elif crossroads_forest == "2":
				print_slow("You choose the clear road to the right.\n")
				print_slow("This road seems really peaceful, and you are glad you chose this path.\n")
				print_slow("You quickly regret saying that, as a giant brown bear suddenly stands in your path.\n")
				print_slow("It doesn't look friendly, but you know bears have a soft side.\n")
				a_fight_no_fightflee(class1,bear_forest,Bear_combat=True)
				print_slow("As the bear dies, it performs one last action as it leaps towards you.\n")
				print_slow("You manage to dodge it, but without looking where you are going, you fall into a hole in the ground.\n")
				print_slow("It's a pretty long drop, and suddenly you land on the ground.\n")
				print_slow("You try to keep yourself awake, but pass out from the fall.\n")
				input("...")
				print_slow("You wake up with a terrible headache and look around. You can't really see anything.\n")
				print_slow("You quickly realize you are not lying down but hanging from something.\n")
				print_slow("You try to move your hands and and legs, but without any luck.\n")
				print_slow("You try to look around again, and now you spot your gear lying on the ground.\n")
				print_slow("There is a lot of cobwebs around you. You try twisting your head towards your arms and legs.\n")
				print_slow("It is very difficult, but you manage to spot a lot of cobwebs trapping your arms and legs.\n")
				print_slow("It does not look like the usual cobweb from a normal spider. This must come out of one giant spider.\n")
				print_slow("Fearing you might get eaten alive - or worse - you take a look around and see if you can find anything useful to help you escape.\n")
				print_slow("First you spot a sharp rock near your left arm. You might be able to swing towards it and get your left arm free (1).\n")
				print_slow("Then you spot a shart object near your legs. Maybe you can try and wiggle your way to it. It might be useful (2).\n")
				print_slow("Lastly you could try and wriggle your way out (3).")
				spider_distance = 0
				web_escape = ""
				while web_escape != "1" and web_escape != "2" and web_escape != "3":
					web_escape = input("What do you want to do - 1/2/3")
				if web_escape == "3":
					print_slow("After attempting to wriggle your way out for several minutes, you realize that you haven't made any progress.\n")
					print_slow("You have to chose another option then. You feel the spider getting closer.\n")
					spider_distance += 1
				while web_escape != "1" and web_escape != "2":
					web_escape = input("What do you want to do - 1 = sharp rock near arm, 2 = sharp object near legs (1/2)")
				if web_escape == "2":
					print_slow("After several minutes, you manage to somehow get the sharp object between your feet.\n")
					print_slow("You know notice it is a knife. you try to cut the spiderweb, with your feet, \n")
					print_slow("but due to the difficulty of that and the fact that the knife is not really sharp, you are not really getting anywhere.\n")
					print_slow("Looks like you have to find another way out.")
					spider_distance += 1
				while web_escape != "1" and web_escape != "3":
					web_escape = input("What do you want to do - 1 = sharp rock near arm, 2 = wriggle your whole body (1/3)")
				if web_escape == "3":
					print_slow("After attempting to wriggle your way out for several minutes, you realize that you hacen't made any progress.\n")
					print_slow("You have to the. You feel the spider getting closer.\n")
					spider_distance += 1

				if web_escape == "1":
					print_slow("You try swinging towards it. You have hit it a few times, but it hasn't done much.\n")
					print_slow("You almost give up, as it is pretty hard work, but then you manage to cut off a big piece of web.\n")
					print_slow("You can now free your left arm. Now for the rest of the body.")
				print_slow("You manage to flee yourself completely now. You hurry up and grab your gear.\n")
				print_slow("Now to escape the cave\n")
				input("...")
				print_slow("*You now have to escape the cave with the spider. The cave is basically like a maze.\nYou will run into places where you have to choose which way to go. (starts with PATH:)\nThis will be a quick time event, so if you are too slow, there will be consequences.\nYou control with wasd (w = up, s = down, a = left, d=right) (remember to press enter after).\nObstacles might hinder you on your escape as well. Here you have to use wasd as well.\nIn this case they have different meanings (w = jump, s = duck, a = dodge left, d = dodge right) \n(remember to press enter after) (starts with OBSTACLE:)\nYour options decide if the spider catches up with you. If that happens, you will lose health. \nAfter the giant spider attacks you, you will gain some distance on it.\nIts damage will gradually increase, until you die.*")
				input("...")
				big_spider_full()
				print_slow("You see light ahead, and to your surprise you have made it to the cave's exit.\n")
				print_slow("You walk out, and look behind you. Seems like the spider is not following you out the cave.\n")
				print_slow("You keep walking, and after a while, you see that you have made it out of the clear road you took.\n")
				print_slow("You look to the left and see where the densely bushed road could have taken you.\n")
				print_slow("You thoughts of the big spider makes you wish that you had taken that road, though you know not what challenges that path had.\n")
				input("...")

			print_slow("You stop for a while to take a little break.\n")
			print_slow("You continue on your way again, with the thought of escaping this forest within not too long.\n")
			print_slow("Because of that, you carry on.\n")
			print_slow("After walking for a while, you suddenly hear a big scream, followed by a cry for help.\n")
			print_slow("'	Help, Help. Someone help us! \n... Don't you touch me with those filthy hands', a female voice screams further in the woods.\n")
			print_slow("You slowly walk forward, and spot a wagon. Then you spot the woman crying for help. You see a bunch of elves robbing her\n")
			print_slow("This doesn't look like the wood elves you met. It must be the dark elves, the wood elf mentioned.\n")
			print_slow("There is really no other way past, than through there. \nYou think about approaching, but spot a convenient bush to hide in to the left.\n")
			dark_elf_wagon = ""
			while dark_elf_wagon != "1" and dark_elf_wagon != "2":
				dark_elf_wagon = input("Do you want to confront the dark elves, or hide in the bush (1 = confront, 2 = hide in bush)? ")
			if dark_elf_wagon == "2":
				print_slow("You sneak over to the bush, and stick your head out the bush so you can see what's happening.\n")
				print_slow("You can't really see properly, so you decide to take a small step further.\n")
				print_slow("*KRRG*\n")
				print_slow("You look down, and see that you stepped on a small branch. \nYou then look up again, and your eyes meet with the eyes of one of the dark elves.\n")
				print_slow("He waves his hand, indicating that he wants you to come. It doesn't look like he is asking, based on the look in his eyes.\n")
				print_slow("It doesn't look like there are many places to run, so you step out the bush, and walk over to him.\n")
			else:
				print_slow("You notice one of the dark elves is away from the others.\n")
				print_slow("You take a deep breath, and walk towards him.\n")
			print_slow("	'Hey, you', he shouts, as he looks you dead in the eyes.\n")
			print_slow("You hurry up a bit. You look around, and see that their are 2 more elves - so 3 in total. \nThen there is the crying woman, and another man inside the wagon.\n")
			print_slow("	'You are the guy, whom my scout spotted in the woods', the dark elf says. \n")
			if allies_with_woodelves:
				print_slow("	'He said he saw you talking with one of the wood elves. He mentioned you gave him something as well - a note'\n")
				print_slow("	'He also described how you shook hands with him after talking to him' \n")
				print_slow("	'You are not welcome here, if you are friends with the wood elves! \nWhat say you in defence?'\n")
				dark_elf_fight = ""
				while dark_elf_fight != "1" and dark_elf_fight != "2" and dark_elf_fight != "3" and dark_elf_fight != "4":
					dark_elf_fight = input("1 = 'I was trying to infiltrate them' \n2 = 'I have no idea what you are talking about' \n3 = *attack him* \n4 = *say nothing* \n(1/2/3/4) ")
				if dark_elf_fight == "1":
					print_slow("	'Oh yea, so what useful information do you have then'\n")
					print_slow("'Well, uhm. I mean ..'")
					print_slow("'	That's what i thought. We do not like liars here.\n")
				elif dark_elf_fight == "2":
					print_slow("	'You think you can fool me? I trust my comrades with all my heart. So now you will die'\n")
				elif dark_elf_fight == "4":
					print_slow("	'Nothing? You will die then.'\n")
				print_slow("He calls his men, but have to leave one of them with the people in the wagon, to be sure they don't escape.\n")
				global dark_elf_dead
				dark_elf_dead = True
				

			else:
				if enemies_with_woodelves:
					print_slow("	'He saw you killing a wood elf, and there was another one lying dead next to him. Well done'\n")
					print_slow("	'He also say you picking something up from the dead wood elf. Can you show me what it was?'\n")
					dark_elf_note = ""
					while dark_elf_note != "1" and dark_elf_note != "2":
						dark_elf_note = input("Do you want to show him the note or not (1 = show note/2 = don't show note)")
					if dark_elf_note == "1":
						print_slow("Very good. This helps a lot that they did not get this note. Do you mind me asking what your name is?")
					else:
						print_slow("	'Okay, he must be seeing vision. Anyway, welcome. My name is Drazloz. The other two are Islas and Rwir. What's your name?'\n")
					dark_elf_dead = False

				else:
					print_slow("	'He saw you bending down near a dead wood elf. He said it looked like you took something from him'\n")
					print_slow("	'He then saw you talking to another wood elf.'\n")
					print_slow("	'We do not accept alliances with wood elves. Explain yourself please.'\n")
					dark_elf_explain = ""
					while dark_elf_explain != "1" and dark_elf_explain != "2" and dark_elf_explain != "3":
						dark_elf_note = input("What do you say? (type 1/2/3)\n1 = *show note* 'I got this from the dead wood elf. I did not tell the other one.\n 2 = *keep note* 'I was just checking to see if he was alive. I'm not friends with the wood elves'\n3 = *say nothing*")
					if dark_elf_note == "1":
						 print_slow("	'Oh, I see. This is really useful. You can consider yourself a friend with us dark elves.'\n")
						 print_slow("	'But don't let the name scare you. You probably don't know the whole story. \nI am Drazloz, the other two are Islas and Rwir. What is your name?'\n")
						 #global dark_elf_dead
						 dark_elf_dead = False
					elif dark_elf_note == "2":
						print_slow("	'Checking to see if he was alive?'\n")
						if die(1,6) != 6:
							print_slow("	'I think you are lying. I think you found something. \nBut if you are not telling us that means you are with the wood elves.'\n")
							#global dark_elf_dead
							dark_elf_dead = True
						else:
							print_slow("	'Okay. I believe you. I will spread the rumor to the other dark elves that you are one of us.'\n")
							print_slow("	'So my name is Drazloz. The other 2 are called Islas and Rwir. What are you called?'\n")
							#global dark_elf_dead
							dark_elf_dead = False
					else:
						print_slow("	'Nothing huh? I think you are with the wood elves. Islas, come over here. Rwir, stay with the girl.'\n")
						print_slow("	'Any last words, human?'\n")
						#global dark_elf_dead
						dark_elf_dead = True

				if dark_elf_dead:
					wagon_darkelves.appearing()
					a_fight_no_fightflee(class1,wagon_darkelves,dark_elf_combat=True)
					print_slow("After the fight, you look towards the last dark elf. He is gone.\n")
					print_slow("You see him running off in the distance.\n")
					print_slow("	'My hero, come here please', you hear from the wagon.\n")
					print_slow("You walk towards the wagon. You see the woman inside the wagon. The man is sitting next to her.\n")
					print_slow("	'Thank you kind sir. We are very grateful for what you have done.', he says.\n ")
					print_slow("	'Before you leave, we want to give you this. For saving us'.\n ")
					print_slow("You look down into the man's hand. You see him holding a hat.\n")
					print_slow("*This hat will increase the stats you regain after each battle*\n")
					take_hat = ""
					while take_hat != "y" and take_hat != "n":
						take_hat = input("Do you want to wear the hat - yes or no (y/n)? ")
					if take_hat == "y":
						if class1.what_class == "Mage":
							class1.mana_regen_rate += 10
							class1.hp_regen_rate += 5
							print_slow(f"You have increased your mana regen rate after battle by 10. You now regenerate {class1.mana_regen_rate} mana after every battle.\n")
							print_slow(f"You have increased your hp regen rate after battle by 5. You now regenerate {class1.hp_regen_rate} hp after every battle.\n")
						elif class1.what_class == "Fighter":
							class1.hp_regen_rate += 10
							print_slow(f"You have increased your hp regen rate after battle by 10. You now regenerate {class1.hp_regen_rate} hp after every battle.\n")
					else:
						print_slow("You did not take the hat. too bad.\n")
					lvl1_stage1 = False
					break

					

				if not dark_elf_dead:
					print_slow(f"	'{class1.name}'\n")
					print_slow(f"	'Well okay {class1.name}. I'm not sure you are familiar with what is going on in this forest are you? \nI mean you know we are not friends with the wood elves.'\n")
					print_slow(f"So, {class1.name}. Once upon a time all elves of birchwood forest lived in peace and harmony. \n Us dark elves have always had a little more violent take on most stuff, but didn't hurt any of our own kind.'\n")
					print_slow("	'So what happened was that for ages no one bothered bothering the elves living in the woods, so everything was fine'\n")
					print_slow("	'However, when a group of people; humans, like yourself, entered our forest, \nthe wood elves and dark elves had a different take on how we should handle the situation.'\n")
					print_slow("	'The dark elves wanted to cast them out, but the wood elves wanted to invite them in.'\n")
					print_slow("	'The problem is that the dark elves have always been outnumberd by the wood elves, so they had to let them in.'\n")
					print_slow("	'The first few weeks it went fine, but when the leader of the dark elves spotted one of them stealing, \nhe immediately took action, and chopped the guys head off'\n  ")
					print_slow("	'The wood elves wasn't very happy with this, but they let it slide.'\n")
					print_slow("	'Already now you could sense the hostility between the two species, but not enough to make them fight each other.\n'")
					print_slow("	'Later on, a dark elf - not the leader this time - spotted the humans torturing and killing a dark elf.'\n")
					print_slow("	'He did not hesitate either, and slayed all the humans. This was spotted by a wood elf.'\n ")
					print_slow("	'The dark elf, who was tortured and murdered was nowhere to be found. \nSo the wood elf only saw the dark elf killing the humans in cold blood.\n' ")
					print_slow("	'The wood elves had had enough. \nThey did not believe the dark elf, when he told them what he had seen the humans so.'\n")
					print_slow("	'They threw them out. Banishing them from their home.'\n")
					print_slow("	'The dark elves vowed to seek revenge, and after a few sabotages and minor battles, we were at war. \nAnd we have been that ever since.'\n")
					input("...")
					print_slow("	'Anyway, if you just continue along the path, you should be out the forest in about 5-10 minutes.'\n")
					print_slow("	'But before you go, I want to give you something'\n")
					print_slow("Drazloz hands you some boots.\n")
					print_slow("	'With these on you should be able to flee easier. Good luck out there.'\n")
					sneak_boots = ""
					while sneak_boots != "y" and sneak_boots != "n":
						sneak_boots = input("You want to put the boots on or not? (y/n) ")
					if sneak_boots == "y":
						print_slow (f"*{name} has equipped the boots* \n")
						class1.flee_skill +=1
						print_slow (f"You increased your chances of fleeing in battle. This only applies to battle where fleeing is actually an option.\n")
					elif sneak_boots == "n":
						print_slow("*You did not put the boots on. Too bad.* \n")
					lvl1_stage1 = False
					break




			#kan vælge at se på eller gå hen til dem
				#når man så går hen til dem er der forskellig reaktion baseret på wood elf encounter
					#Hvis du ender med at dræbe dem, kan du hjælpe hende der bliver røvet
						#får en reward
				#Hvis du bliver og kigger, ser de dig, og så er det bare ligesom du gik derhen
			#man møder senere en dark elf - han har set dig snakke med wood elf (eller dræbe ham)
				#de røver en vogn, derefter ser de dig.
				#Han vil angribe dig hvis du ikke viser noten fra woodelf scouten - ellers har han bare set dig dræbe en woodelf (måske 2), og så er I også venner

		elif formin == "mines" or formin == "Mines":
			print_slow(f"*{name} has entered the mines*")
			input(" ...")	
			print_slow(" \nWhen you arrive at the mines, you hear a strange noise, coming from behind." + "\n")
			print_slow(" Therefore, you hurry up and run into the mines." + "\n")
			print_slow(" Your loud foorsteps from running, awaken nearby orcs in the cave" + "\n")
			input(" ...")
			mineorc1.appearing()
			abc = True
			if class1.what_class == "Mage":
				print_slow ("*If you choose to flee, you might succeed, otherwise the enemy is guaranteed to go first." + "\n" "If you choose to fight instead, it is a 50/50 chance if you start or not*" + "\n")
			elif class1.what_class == "Fighter":
				print_slow ("*If you choose to flee, you might succeed, otherwise the enemy is guaranteed to go first." + "\n" "If you choose to fight instead, there is a 2/3 chance for you to start*" + "\n")
			a_fight(class1,mineorc1)



			input("...")
			print_slow("The orc is gone, but you are still in the mine. " + "\n")
			print_slow("After walking for a while, you reach a dead end. You can see a path going to the left." + "\n" "It looks really dark, but it is there." + "\n")
			print_slow("To the right you see another path. This is not as dark," + "\n" "but it seems to go back where you came from - at least the first big part of it" + "\n")
			input("...")
			minestage1 = True
			while minestage1:
				mine_r_or_l = input("Do you want to go left down the dark path, or right down the slow but brighter path (1 = left / 2 = right)? ")
				if mine_r_or_l == "1":
					print_slow ("You choose the darker path to the left" + "\n")
					print_slow ("After walking for a few minutes, you come across a small chest." + "\n" "It looks like it has not been opened for a while")
					input("...")
					minestageA1 = True
					# skal give liv til sidst. den er hurtigere, så når han kommer ud, ser han at det er mørkt, og sover, og får liv af det
					while minestageA1:
						while True:
							mineA_chest1 = input("Do you want to open the chest, or not (1 = open / 2 = do not open)? ") 
							if mineA_chest1 == "1":
								if class1.what_class == "Mage":
									print_slow (f"*{name.capitalize()} has opened the chest*" + "\n")
									global manapot_S1
									manapot_S1 = Potion("small","mana",40)
									manapot_S1.new_potion()
									potion_action(manapot_S1)
									break
								elif class1.what_class == "Fighter":
									print_slow (f"*{name.capitalize()} has opened the chest*" + "\n")
									print_slow (f"*{name} has found a ring*\n")
									print_slow (f"you can choose to put it on or not. It is your choice\n")
									while True:
										tiredness_ring = input("You want to put the ring on or not? (y/n) ")
										if tiredness_ring.lower() == "y":
											print_slow (f"*{name} has equipped the ring* \n")
											class1.tired_threshold += 1
											print_slow (f"Your tiredness_threshold is now permantly increased by 1. it is now at {class1.tired_threshold} \n")
											break
										elif tiredness_ring.lower() == "n":
											print_slow("*You did not put on the ring. too bad* \n")
											break
										else:
											continue
									break
							elif mineA_chest1 == "2":
								print(f"*{name.capitalize()} choose to not open the chest. You won't take the chance*")
								break

						print_slow ("You move on from the chest, and continue along the passage out of the cave" + "\n")
						print_slow ("You can hear voices up ahead, so you try to stay as silent as possible" + "\n")
						print_slow ("You see an indented part of the cave, and notice 3 goblin's standing over something that looks like a human corpse" + "\n")
						print_slow ("You just need to get 10 meters forward to be out of the goblin's line of sight" + "\n")
						print_slow ("It could be possible to sneak your way through, as there are some covers," + "\n" "where the goblin's shouldn't be able to see you" + "\n")
						print_slow ("You could also try to run, and hope they don't spot you" + "\n")
						MinestageA2 = True

						while MinestageA2:
							while True:
								escape_minegoblin = input("Do you want to try and make a run for it, or try sneaking you way through them (1 = run / 2 = sneak)? ")
								if escape_minegoblin == "1":
									print_slow ("You prepare to make a run for it." + "\n")
									print_slow ("The first few meters go smoothly, and they haven't noticed anything" + "\n")
									print_slow ("You are only 1 long step away, so you decide to make a long leap" + "\n")
									print_slow ("But just as you step on the ground before your leap, you step on a little rock, " + "\n")
									print_slow ("that you did not notice beforehand. This means that you twist your ancle slightly and fall to the ground" + "\n")
									input("...")
									print_slow ("BANG!" + "\n")
									print_slow ("You look behind you and see 3 goblins looking at you" + "\n")
									print_slow ("*The fall hurts you.*" + "\n")
									class1.lose_hp(5)
									input("...")
									break
								elif escape_minegoblin == "2":
									print_slow ("You look around to check if there is anyone other than the 3 goblins in the indented part of the cave" + "\n")
									print_slow ("You see no one, and start sneaking. The first few steps is going fine." + "\n")
									print_slow ("You now reach the first cover. Now you just need to sneak over to the other cover and then 1-2 steps," + "\n")
									print_slow ("and you are there. You take a deep breath and continue." + "\n")
									print_slow ("You managed to reach the last cover. Now for the last steps." + "\n")
									print_slow ("Just as you are supposed to take a step, you suddenly hear a noise" + "\n")
									input("...")
									print_slow ("CRUNCH!" + "\n")
									print_slow ("You look down, and see that you have stepped on a small branch that was almost impossible to see in the darkness" + "\n")
									print_slow ("You look behind you and see the 3 goblins looking right at you." + "\n")
									input("...")
									minegoblin1.appearing()
									break

							a_fight(class1,minegoblin1)
									
							input("...")
							print_slow ("The goblins are gone, but you are still in the mine." + "\n")
							print_slow ("After walking for a few more minutes, however, you see the exit up ahead." + "\n")
							print_slow ("You can see it is all dark outside and decide to wait until day to go out" + "\n")
							print_slow ("*Since you took the faster path in the mine, you sleep and regain some stats*" + "\n")
							class1.regen_after_fight()
							input("...")
							print_slow ("You wake up, feeling well rested, and exit the mine" + "\n")
							minestageA1 = False
							minestage1 = False
							lvl1_stage1 = False
							break

				elif mine_r_or_l == "2":
					print_slow ("You choose the slower path to the right." +"\n")
					print_slow ("After walking for a while, you come across a large open space." +"\n")
					print_slow ("In it, you see a large waterfall, ending in a river." +"\n")
					print_slow ("You can see the exit on the other side of the river." +"\n")
					print_slow ("You need to cross the river. Somehow ... " +"\n")
					print_slow ("Far to the left of you, you see a dilapidated bridge." +"\n")
					print_slow ("Just behind that, you can see a rowing boat, with a oar in it.." +"\n")
					minestageB1 = True
					while minestageB1:
						while True:
							mine_river1 = input ("How do you cross the river, boat or bridge (boat = 1 / bridge = 2)? ")
							if mine_river1 == "1":
								print_slow ("You move towards the boat. As you get closer, you can see that it is in surprisingly good condition." + "\n")
								print_slow ("You can only see 1 oar though, so it will not be an easy task crossing this river." + "\n")
								print_slow ("You push the boat out, and start rowing. The first few rows go smoothly." + "\n")
								print_slow ("Now it starts becoming difficult though, and you really need to put your back into it." + "\n")
								print_slow ("You reach the other side of the river, but you are completely out of breath. " + "\n")
								print_slow ("You stay on the shores for a while, trying to recover your strength" + "\n")
								print_slow ("*You used a lot of energy to cross the river*")
								class1.lose_hp(5)
								if class1.what_class == "Mage":
									class1.lose_mana(10)
								elif class1.what_class == "Fighter":
									class1.tiredness += 1
									print_slow(f"Your tiredness increases by 1. It is now at {class1.tiredness}. ")
								print_slow ("You move on towards the exit." + "\n")
								print_slow ("Here you spot 5 fairly big spiders. There is no way to get through the exit, without dealing with them first" + "\n")
								
								if attacks_first() == "enemy":
									turn = "enemy"
								else:
									turn = "player"
								break
							elif mine_river1 == "2":
								print_slow ("You move towards the bridge. You can see various loose boards, and empty spaces were there used to be boards." + "\n")
								print_slow ("You stand one step away from the bridge, with serious second thoughts." + "\n")
								print_slow ("As you take your first step, you hear creaky noises. You hang on to the bridge's rope handles firmly." + "\n")
								print_slow ("You decide to hurry up, and get this over with." + "\n")
								print_slow ("The creaky noises are very loud, but you finally make it accross the bridge in one piece." + "\n")
								print_slow ("As you look up, you see 5 big spiders staring angrily at you." + "\n")
								print_slow ("Guess there is no other way than through them ... " + "\n")
								print_slow ("*The spiders attack you before you can prepare properly*" + "\n")
								input("...")
								turn = "enemy"
								break
						minespider1.appearing()
						class1.attack(minespider1)
						a_fight_no_fightflee(class1,minespider1)

						input("...")
						print_slow ("The spiders are dead, so you continue towards the exit. " + "\n")
						print_slow ("Outside you can see the sun has just risen." + "\n")
						print_slow ("You sigh, as there is no time for a break now." + "\n")
						print_slow ("You walk out the cave and continue your journey" + "\n")
						minestageA1 = False
						minestage1 = False
						lvl1_stage1 = False
						break
		else:
			print_slow("you cannot go there. ")
			continue
	while not lvl1_stage1:
		print_slow("you made it through the first obstacle, but you know there is many more to come" + "\n")
		break


while playing:
	intro()
	level1()
	print("done with 1")
	playing = False
while not playing:
	print("no more play")
	sys.exit()