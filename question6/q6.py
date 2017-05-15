import random
import time

class Ship(object):
	def __init__(self, name):
		self.name = name
		self.shields = 80 
		self.hullStrength = 100
		self.laserPower = 20

	def _chooseShip(self, shipList):
		#find a ship thats alive and not itself
		someShip = None
		while someShip is None:
			randIndex = random.randint(0, len(shipList)-1)
			someShip = shipList[randIndex]
			if someShip == self or someShip.isDestroyed():
				someShip = None
		return someShip
	
	def shootShip(self, shipList):
		otherShip = self._chooseShip(shipList)
		otherShip.getShotAt(self.laserPower)	

	def getShotAt(self, dmg):
		print '\t', self.name, "is shot at."
		#check if there is still shields
		if self.shields > 0:
			self.shields -= dmg
			if self.shields < 0:
				#remove remainder from hull
				self.hullStrength += self.shields
				self.shields = 0;
		else:
			self.hullStrength -= dmg
			if self.hullStrength <= 0:
				print '\t', self.name, "has been destroyed."
	def isDestroyed(self):
		return self.hullStrength <= 0
	def __str__(self):
		return "Name: %s\nShields: %s\nHull Strength: %s" % (self.name, self.shields, self.hullStrength)

class Warship(Ship):
	def __init__(self, name):
		Ship.__init__(self, name)
		self.missilePower = 80

	def shootShip(self, shipList):
		otherShip = self._chooseShip(shipList)
		if random.random() <= 0.3: #30% chance to shoot missiles
			selectedWeapon = self.missilePower
			weaponName = "high-powered missiles"
		else:
			selectedWeapon = self.laserPower
			weaponName = "lasers"
		print "\t%s selects its %s." % (self.name, weaponName)
		otherShip.getShotAt(selectedWeapon)	

class Speeder(Ship):
	def __init__(self, name):
		Ship.__init__(self, name)
		self.dodgeChance = 0.5

	def getShotAt(self, dmg):
		if random.random() >= self.dodgeChance:
			super(Speeder, self).getShotAt(dmg)
		else:
			print '\t', self.name, "is shot at... but dodges the shot!"

if __name__ == "__main__":
	Ship1 = Ship("Ship 1")
	Ship2 = Ship("Ship 2")
	Ship3 = Ship("Ship 3")
	Warship1 = Warship("Warship 1")
	Speeder1 = Speeder("Speeder 1")

	allShips = [Ship1, Ship2, Ship3, Warship1, Speeder1]
	
	print "\n===================Space Battle Start==================="
	winnerIndex = None
	TurnNo = 0
	while winnerIndex is None:
		aliveShips = len(allShips)
		currentShip = allShips[random.randint(0, len(allShips)-1)]
		if not currentShip.isDestroyed():
			TurnNo += 1
			print "[Turn %s]\n\tIt is %s's turn." % (TurnNo, currentShip.name)
			currentShip.shootShip(allShips)
			
			print "\tCurrent status of ships:"
			for ship in allShips:
				if ship.isDestroyed():
					print '\t\t', ship.name, "is destroyed."
					aliveShips -= 1
				else:
					print '\t\t', ship.name, "is alive. Shields:", ship.shields, "Hull strength:", ship.hullStrength

			if aliveShips == 1:
				winnerIndex = allShips.index(currentShip)
		
	winner = allShips[winnerIndex]
	print "Winner is %s." % (winner.name)
	

	print "===================Space Battle End=====================\n"

















