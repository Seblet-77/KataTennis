import random


class KataTennis:

	def __init__(self, p1Name, p2Name):
		self.p1Name = p1Name
		self.p2Name = p2Name
		self.p1Points = 0
		self.p2Points = 0

	def win_point_randomly(self):
		res = random.randint(0,1)
		if (res == 0):
			self.p1Points += 1
		else:
			self.p2Points += 1

	def show_score(self):
		result = ""
		dictScore = {
				0 : "0",
                1 : "15",
                2 : "30",
                3 : "40",
			}
		dictScoreAll = {
				0 : "0 All",
                1 : "15 All",
                2 : "30 All",
                3 : "40 All",
			}

		if (self.p1Points == self.p2Points):
			result = dictScoreAll.get(self.p1Points, "Deuce")
		elif (self.p1Points >= 4 or self.p2Points >= 4):
			diffPoints = self.p1Points - self.p2Points
			if (diffPoints == 1):
				result = "Advantage " + self.p1Name
			elif (diffPoints == -1):
				result = "Advantage " + self.p2Name
			elif (diffPoints >= 2 ):
				result = self.p1Name + " won game"
			elif (diffPoints <= -2):
				result = self.p2Name + " won game"
		else:
			result = dictScore.get(self.p1Points) + " - " + dictScore.get(self.p2Points)
		return result


def test_play_game(Game, p1Name, p2Name):
    game = KataTennis(p1Name, p2Name)

    while 1:
    	game.win_point_randomly()
    	print(game.show_score())
    	print(game.p1Points,game.p2Points)
    	print("")
    	if ((game.p1Points >= 4 or game.p2Points >= 4) and (game.p1Points - game.p2Points >= 2 or game.p1Points - game.p2Points <= -2)):
    		break


test_play_game(KataTennis, 'Nadal', 'Federer')


