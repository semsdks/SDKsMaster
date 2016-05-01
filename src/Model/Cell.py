#================================================================
class Cell:
#================================================================
# Methods:
	#--------------------------------------------------------
	# - Cell Constructor
	#--------------------------------------------------------
	# * solution : the correct answer for this cell.
	#--------------------------------------------------------
	def __init__(self, solution):
		self.answer_ = solution
		self.solution_ = solution
		self.mutable_ = False

	#--------------------------------------------------------
	# - Get Current Given Answer
	#--------------------------------------------------------
	# returns the current answer for this cell, as given by
	# the user or provided by default.
	#--------------------------------------------------------
	def getAnswer(self):
		return self.answer_

	#--------------------------------------------------------
	# - Submit Answer
	#--------------------------------------------------------
	# sets the cell's given answer to the user's guess IF the
	# cell is mutable.
	# returns True if the user's guess was correct.
	#--------------------------------------------------------
	def submitAnswer(self, answer):
		if(self.mutable_):
			self.answer_ = answer
		return self.isCorrect()

	#--------------------------------------------------------
	# Hide Given Solution
	#--------------------------------------------------------
	# sets the cell's answer to None given and makes it
	# mutable, allowing this cell to be solved by the user.
	#--------------------------------------------------------
	def hideAnswer(self):
		self.answer_ = None
		self.mutable_ = True

	#--------------------------------------------------------
	# - Is This Cell Mutable ?
	#--------------------------------------------------------
	# returns True if this cell is to be solved by the user,
	# and False if it is a provided answer.
	#--------------------------------------------------------
	def isMutable(self):
		return self.mutable_

	#--------------------------------------------------------
	# - Is This Cell Correct ?
	#--------------------------------------------------------
	# returns True if the answer given and the true solution
	# match, and False otherwise.
	#--------------------------------------------------------
	def isCorrect(self):
		return self.answer_ == self.solution_

	#--------------------------------------------------------
	# - Get Correct Solution
	#--------------------------------------------------------
	# returns the true solution to this cell.
	#--------------------------------------------------------
	def getSolution(self):
		return self.solution_

# Members:
	answer_ = None
	solution_ = None
	mutable_ = False
#================================================================
