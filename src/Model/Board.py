from Cell import Cell
import random, math

#================================================================
class Board:
#================================================================
# Methods
	#--------------------------------------------------------
	# - Board Constuctor
	#--------------------------------------------------------
	# * solutions : number of cells to leave as unsolved.
	# * basicOnly : whether to apply random transformations.
	#--------------------------------------------------------
	def __init__(self, solutions, randomize = True):
		solutions = max(0, min(81, solutions))

		self.generate(solutions, randomize)
		self.unsolved_ = solutions
		self.incorrect_ = solutions

	#--------------------------------------------------------
	# - Get Raw Board Array
	#--------------------------------------------------------
	# returns the current solution to the board as a raw
	# array of integers. A value of -1 represents NONE, or a
	# currently unsolved cell.
	#--------------------------------------------------------
	def getRaw(self):
		return [[cell.getAnswer() for cell in row] for row in self.board_]

	#--------------------------------------------------------
	# - Generate Game Board
	#--------------------------------------------------------
	# * solutions : number of cells to leave as unsolved.
	# * basicOnly : whether to apply random transformations.
	# creates a valid Sudoku board with some cells left
	# unsolved and mutable, and the rest answered.
	#--------------------------------------------------------
	def generate(self, solutions, randomize):
		self.board_ = []
		random.seed()

		# Generate base puzzle: known to be valid.
		# Generate each row
		for row in range(9):
			self.board_.append([])

			# Generate each cell
			for column in range(9):
				shift = ((row * 3) % 9) + math.floor(row / 3)
				number = int(((column + shift) % 9) + 1)

				cell = Cell(number)
				self.board_[row].append(cell)

		if randomize:
			# Randomly perturb the puzzle iteratively to generate a new puzzle
			for i in range(1000):
				self.perturb()

		# Randomly hide given solutions
		hidden = random.sample(range(81), solutions)
		
		for index in hidden:
			row = int(math.floor(index / 9))
			column = int(index % 9)
			
			self.board_[row][column].hideAnswer()

	#--------------------------------------------------------
	# - Print Board
	#--------------------------------------------------------
	# Outputs the current board's answer state to console.
	#--------------------------------------------------------
	def display(self):
		print()
		print(".-------------------------.")
		for row in self.getRaw():
			print(row)

		print("'-------------------------'")
		print()

	#--------------------------------------------------------
	# - Get Row
	#--------------------------------------------------------
	# * index : the row's index, counting top to bottom
	# returns a single 9-item row on the game board.
	# In a correct solution, each number should be unique.
	#--------------------------------------------------------
	def getRow(self, index):
		if index not in range(9):
			return None
		else:
			return self.board_[index]

	#--------------------------------------------------------
	# - Get Column
	#--------------------------------------------------------
	# * index : the column's index, counting left to right
	# returns a single 9-item column on the game board.
	# In a correct solution, each number should be unique.
	#--------------------------------------------------------
	def getColumn(self, index):
		if index not in range(9):
			return None
		else:
			return [self.board_[row][index] for row in range(9)]

	#--------------------------------------------------------
	# - Get 3x3 Block
	#--------------------------------------------------------
	# * x : the major column, counting left to right
	# * y : the major row, counting top to bottom
	# returns a 9-item 3x3 block on the board.
	# In a correct solution, each number should be unique.
	#--------------------------------------------------------
	def getBlock(self, x, y):
		if x not in range(3) or y not in range(3):
			return None
		else:
			return [self.board_[row + y * 3][3 * x : 3 * x + 3] for row in range(3)]

	#--------------------------------------------------------
	# - Get Individual Cell
	#--------------------------------------------------------
	# * x : the column or x-coordinate, from left to right
	# * y : the row or y-cooridnate, from top to bottom
	# returns the exact Cell located at (x, y)
	#--------------------------------------------------------
	def getCell(self, x, y):
		if x not in range(9) or y not in range(9):
			return None
		else:
			return self.board_[y][x]

	#--------------------------------------------------------
	# - Submit Answer to Cell
	#--------------------------------------------------------
	# * x : the column or x-coordinate, from left to right
	# * y : the row or y-cooridnate, from top to bottom
	# * answer : the answer guessed by the user.
	# sets the cell's given answer to the user's guess, and	
	# increments/decrements the number of cells yet to be
	# solved if the answer was incorrect/correct.
	# returns True if the user's guess was correct.
	#--------------------------------------------------------
	def submitAnswer(self, x, y, answer):
		if x not in range(9) or y not in range(9) or answer not in range(1, 10):
			return None
		else:
			self.unsolved_ -= 1
			oldStatus = self.board_[y][x].isCorrect()
			correct = self.board_[y][x].submitAnswer(answer)
			
			self.incorrect_ += oldStatus - correct
			return correct
	
	#--------------------------------------------------------
	# - Is This Row Correctly Solved?
	#--------------------------------------------------------
	# * index : the row's index, counting top to bottom
	# returns True if each number in the row is unique, and
	# False otherwise.
	#--------------------------------------------------------
	def isRowCorrect(self, index):
		if index not in range(9):
			return None
		else:		
			numbers = [cell.getAnswer() for cell in self.getRow(index)]

			if(None in numbers):
				return False

			numbers.sort()

			return numbers == list(range(1, 10))

	#--------------------------------------------------------
	# - Is This Column Correctly Solved?
	#--------------------------------------------------------
	# * index : the column's index, counting left to right
	# returns True if each number in the column is unique,
	# and False otherwise.
	#--------------------------------------------------------
	def isColumnCorrect(self, index):
		if index not in range(9):
			return None
		else:		
			numbers = [cell.getAnswer() for cell in self.getColumn(index)]

			if None in numbers:
				return False

			numbers.sort()

			return numbers == list(range(1, 10))

	#--------------------------------------------------------
	# - Is This Block Correctly Solved?
	#--------------------------------------------------------
	# * x : the major column, counting left to right (0~2)
	# * y : the major row, counting top to bottom (0~2)
	# returns True if each number in the 3x3 block is unique,
	# and False otherwise.
	#--------------------------------------------------------
	def isBlockCorrect(self, x, y):
		if x not in range(3) or y not in range(3):
			return None
		else:		
			numbers = [cell.getAnswer() for row in self.getBlock(x, y) for cell in row]

			if None in numbers:
				return False

			numbers.sort()

			return numbers == list(range(1, 10))

	#--------------------------------------------------------
	# - Is the Puzzle Solved?
	#--------------------------------------------------------
	# returns 'Correct' if the sudoku has been succesfully
	# solved, 'Incorrect' if solved but invalidly, and
	# 'Incomplete' otherwise.
	#--------------------------------------------------------
	def isSolved(self):
		if self.unsolved_ > 0:
			return 'Incomplete'
		else:
			 return 'Incorrect' if self.incorrect_ > 0 else 'Correct'

	#--------------------------------------------------------
	# - Is the Puzzle Valid?
	#--------------------------------------------------------
	# returns IF the sudoku is a valid board: no row, column
	# or block contains two of the same number. 
	#--------------------------------------------------------
	def isValid(self):
		for row in range(9):
			numbers = [cell.getSolution() for cell in self.getRow(row)]
			numbers.sort()

			if numbers != list(range(1, 10)):
				return False

		for column in range(9):
			numbers = [cell.getSolution() for cell in self.getColumn(column)]
			numbers.sort()

			if numbers != list(range(1, 10)):
				return False
		
		for x in range(3):
			for y in range(3):
				numbers = [cell.getSolution() for row in self.getBlock(x, y) for cell in row]
				numbers.sort()

				if numbers != list(range(1, 10)):
					return False

		return True

	#--------------------------------------------------------
	# - Swap Rows
	#--------------------------------------------------------
	# * y1 : index of first row to be swapped (0~8)
	# * y2 : index of second row to be swapped (0~8)
	# Swaps the cells in rows at y1 and y2.
	#--------------------------------------------------------
	def swapRows(self, y1, y2):
		if y1 not in range(9) or y2 not in range(9):
			return None
		elif y1 is not y2:
			self.board_[y1], self.board_[y2] = self.board_[y2], self.board_[y1]

	#--------------------------------------------------------
	# - Swap Columns
	#--------------------------------------------------------
	# * x1 : index of first column to be swapped (0~8)
	# * x2 : index of second column to be swapped (0~8)
	# Swaps the cells in columns at x1 and x2.
	#--------------------------------------------------------
	def swapColumns(self, x1, x2):
		if x1 not in range(9) or x2 not in range(9):
			return None
		elif x1 is not x2:
			for y in range(9):
				self.board_[y][x1], self.board_[y][x2] = self.board_[y][x2], self.board_[y][x1]

	#--------------------------------------------------------
	# - Swap Cells Along Minor Diagonal
	#--------------------------------------------------------
	# Swaps the all cells along the minor diagonal, from the
	# bottom-left to the top-right corner.
	#--------------------------------------------------------
	def swapMinorDiagonal(self):
		for x in range(9):
			for y in range(9):
				if x + y < 9:
					self.board_[y][x], self.board_[8 - x][8 - y] = self.board_[8 - x][8 - y], self.board_[y][x]
		
	#--------------------------------------------------------
	# - Swap Cells Along Major Diagonal
	#--------------------------------------------------------
	# Swaps the all cells along the major diagonal, from the
	# top-left to the bottom-right corner.
	#--------------------------------------------------------
	def swapMajorDiagonal(self):
		for x in range(9):
			for y in range(9):
				if x > y:
					self.board_[y][x], self.board_[x][y] = self.board_[x][y], self.board_[y][x]

	#--------------------------------------------------------
	# - Swap Columns of Blocks
	#--------------------------------------------------------
	# * x1 index of first block column to be swapped (0~2)
	# * x2 index of second block column to be swapped (0~2)
	# Swaps two major columns of blocks.
	#--------------------------------------------------------
	def swapBlockColumns(self, x1, x2):
		if x1 not in range(3) or x2 not in range(3):
			return None

		if x1 != x2:
			for x in range(3):
				self.swapColumns(x1 * 3 + x, x2 * 3 + x)

	#--------------------------------------------------------
	# - Swap Rows of Blocks
	#--------------------------------------------------------
	# * y1 index of first block row to be swapped (0~2)
	# * y2 index of second block row to be swapped (0~2)
	# Swaps two major rows of blocks.
	#--------------------------------------------------------
	def swapBlockRows(self, y1, y2):
		if y1 not in range(3) or y2 not in range(3):
			return None

		if y1 != y2:
			for y in range(3):
				self.swapRows(y1 * 3 + y, y2 * 3 + y)

	#--------------------------------------------------------
	# - Swap Digits
	#--------------------------------------------------------
	# * a the first unique digit to be swapped (1~9)
	# * b the second unique digit to be swapped (1~9)
	# Swaps all instances of a digit with all instances of
	# another.
	#--------------------------------------------------------
	def swapDigits(self, a, b):
		if a in range(1, 10) and b in range(1, 10) and a != b:
			for x in range(9):
				for y in range(9):
					if self.board_[y][x].getSolution() == a:
						self.board_[y][x].solution_ = b
						self.board_[y][x].answer_ = b
					elif self.board_[y][x].getSolution() == b:
						self.board_[y][x].solution_ = a
						self.board_[y][x].answer_ = a

	#--------------------------------------------------------
	# - Flip Horizontally
	#--------------------------------------------------------
	# Flips the board horizontally: 1st column swaps with 9th
	# 2nd with 8th, and so on.
	#--------------------------------------------------------
	def flipHorizontal(self):
		for x in range(4):
			self.swapColumns(x, 8 - x)

	#--------------------------------------------------------
	# - Flip Vertically
	#--------------------------------------------------------
	# Flips the board vertically: 1st row swaps with 9th, 2nd
	# with 8th, and so on.
	#--------------------------------------------------------
	def flipVertical(self):
		for y in range(4):
			self.swapRows(y, 8 - y)

	#--------------------------------------------------------
	# - Rotate Clockwise
	#--------------------------------------------------------
	# Rotates the board grid-wise in a clockwise direction
	#--------------------------------------------------------
	def rotate(self):
		self.board_ = [self.getColumn(x)[::-1] for x in range(9)]		

	#--------------------------------------------------------
	# - Perturb
	#--------------------------------------------------------
	# Initiates a random transformation on the board with
	# random parameters that retains the board's validity.
	# Possible transformations are:
	#	- Swap along major/minor diagonal
	#	- Swap two random regional columns/rows of blocks
	#	- Swap two random major block columns/rows
	#	- Swap two random unique digits
	#	- Rotate the board clock-wise
	#	- Flip the board horizontally/vertically
	# Returns a string indicating the transformation executed
	# and its parameters.
	#--------------------------------------------------------
	def perturb(self):
		transform = random.randint(1, 6)

		# Swap Regional Columns/Rows
		if(transform is 1):
			region = random.randint(0, 2)
			coord1 = random.randint(0, 1)
			coord2 = random.randint(coord1 + 1, coord1 + 2) % 3

			if random.randint(0, 1) == 0:
				self.swapColumns(region * 3 + coord1, region * 3 + coord2)
				return "Swap Regional - Columns " + str(region * 3 + coord1) + ", " + str(region * 3 + coord2)

			else:
				self.swapRows(region * 3 + coord1, region * 3 + coord2)
				return "Swap Regional - Rows " + str(region * 3 + coord1) + ", " + str(region * 3 + coord2)

		# Swap Along Major/Minor Diagonal
		elif(transform is 2):
			if random.randint(0, 1) == 0:
				self.swapMajorDiagonal()
				return "Swap Diagonal - Major"

			else:
				self.swapMinorDiagonal()
				return "Swap Diagonal - Minor"

		# Swap Major Block Columns/Rows
		elif(transform is 3):
			coord1 = random.randint(0, 1)
			coord2 = random.randint(coord1 + 1, coord1 + 2) % 3

			if random.randint(0, 1) == 0:
				self.swapBlockColumns(coord1, coord2)
				return "Swap Major - Columns " + str(coord1) + ", " + str(coord2)

			else:
				self.swapBlockRows(coord1, coord2)
				return "Swap Major - Rows " + str(coord1) + ", " + str(coord2)

		# Swap Two Digits
		elif(transform is 4):
			digits = random.sample(range(1, 10), 2)

			self.swapDigits(digits[0], digits[1])
			return "Swap Digits - " + str(digits[0]) + ", " + str(digits[1])

		# Flip Horizontally/Vertically
		elif(transform is 5):
			if random.randint(0, 1) == 0:
				self.flipHorizontal()
				return "Flip - Horizontal"

			else:
				self.flipVertical()
				return "Flip - Vertical"

		# Rotate Clockwise
		else:
			self.rotate()
			return "Rotate"

# Members
	board_ = []
	unsolved_ = 0
	incorret_ = 0
#================================================================
