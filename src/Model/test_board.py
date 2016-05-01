from Board import Board
import unittest, random, math


class Test_Board(unittest.TestCase):
	board = None

	def setUp(self):
		self.board = Board(10, False)

	def tearDown(self):
		pass

	#--------------------------------------------------------------------------------
	def test_01_board_is_created_with_9x9_elements(self):
	#--------------------------------------------------------------------------------
		raw_board = self.board.getRaw()
		
		self.assertEqual(len(raw_board), 9, "Board was not created with 9 rows")
		self.assertEqual(len(raw_board[0]), 9, "Board was not created with 9 columns")

	#--------------------------------------------------------------------------------
	def test_02_board_elements_are_either_a_digit_or_None(self):
	#--------------------------------------------------------------------------------
		for row in self.board.getRaw():
			for cell in row:
				self.assertTrue(type(cell) is int or type(cell) is type(None), "Cell is neither an integer, nor None (blank), but a " + str(type(cell))),

				# Test that any integer cells are within 1~9
				if type(cell) == 'int': 
					self.assertIn(cell, range(1, 10), "Cell is out of range")
		

	#--------------------------------------------------------------------------------
	def test_03_board_has_10_unsolved_cells(self):
	#--------------------------------------------------------------------------------
		unsolved = 0

		for row in self.board.getRaw():
			for cell in row:
				if(type(cell) == type(None)):
					unsolved += 1

		self.assertEqual(unsolved, 10, "The number of solutions was not equal to the constructor argument.")
		
	#--------------------------------------------------------------------------------
	def test_04_board_is_initially_unsolved(self):
	#--------------------------------------------------------------------------------
		self.assertEqual(self.board.isSolved(), 'Incomplete', "Board was not created incomplete")

	#--------------------------------------------------------------------------------
	def test_05_get_row_returns_an_actual_row_from_the_board(self):
	#--------------------------------------------------------------------------------
		row = self.board.getRow(4)

		for column in range(9):
			self.assertEqual(row[column], self.board.board_[4][column], "A cell in getRow did not match the board's original data.")

		# Row should be 9-cells in length
		self.assertEqual(len(row), 9, "Returned row is of abnormal length")

		# Calling an index out of range (0~8) should return None
		self.assertEqual(self.board.getRow(-1), None, "Calling row with index -1 did not produce a row of None")
		self.assertEqual(self.board.getRow(9), None, "Calling row with index 9 did not produce a row of None")

	#--------------------------------------------------------------------------------
	def test_06_get_column_returns_an_actual__column_from_the_board(self):
	#--------------------------------------------------------------------------------
		column = self.board.getColumn(6)

		# Column should be 9-cells in length
		self.assertEqual(len(column), 9, "Returned column is of abnormal length")

		for row in range(9):
			self.assertEqual(column[row], self.board.board_[row][6], "A cell in getColumn did not match the board's original data.")

		# Calling an index out of range (0~8) should return None
		self.assertEqual(self.board.getColumn(-1), None, "Calling column with index -1 did not produce a column of None")		
		self.assertEqual(self.board.getColumn(9), None, "Calling column with index 9 did not produce a column of None")		

	#--------------------------------------------------------------------------------
	def test_07_get_block_returns_an_actual_block_from_the_board(self):
	#--------------------------------------------------------------------------------
		block = self.board.getBlock(2, 1)

		# Block should be 3x3-cells in dimension
		self.assertEqual(len(block), 3, "Returned block has abnormal number of rows")
		self.assertEqual(len(block[0]), 3, "Returned block has abnormal number of columns")

		for row in range(3):
			for column in range(3):
				self.assertEqual(block[row][column], self.board.board_[3 + row][6 + column], "A cell in getColumn did not match the board's original data.")

		# Calling an either index out of range (0~2, 0~2) should return None
		self.assertEqual(self.board.getBlock(-1, 0), None, "Calling block with coords (-1, 0) did not produce a block of None")		
		self.assertEqual(self.board.getBlock(3, 0), None, "Calling block with coords (3, 0) did not produce a block of None")		
		self.assertEqual(self.board.getBlock(0, -1), None, "Calling block with coords (0, -1) did not produce a block of None")		
		self.assertEqual(self.board.getBlock(0, 3), None, "Calling block with coords (0, 3) did not produce a block of None")		

	#--------------------------------------------------------------------------------
	def test_08_get_cell_returns_an_actual_cell_from_the_board(self):
	#--------------------------------------------------------------------------------
		row = random.randint(0, 8)
		column = random.randint(0, 8)

		self.assertEqual(self.board.getCell(column, row), self.board.board_[row][column], "Cell(" + str(row) + ", " + str(column) + ") did not match the board's original data.")

		# Calling either index out of range (0~8, 0~8) should return None
		self.assertEqual(self.board.getBlock(-1, 0), None, "Calling cell with coords (-1, 0) did not produce a cell of None")		
		self.assertEqual(self.board.getBlock(9, 0), None, "Calling cell with coords (9, 0) did not produce a cell of None")		
		self.assertEqual(self.board.getBlock(0, -1), None, "Calling cell with coords (0, -1) did not produce a cell of None")		
		self.assertEqual(self.board.getBlock(0, 9), None, "Calling cell with coords (0, 9) did not produce a cell of None")				

	#--------------------------------------------------------------------------------
	def test_09_submit_answer_sets_the_value_of_a_cell(self):
	#--------------------------------------------------------------------------------
		x = None
		y = None

		for row in range(9):
			for column in range(9):
				if self.board.getCell(column, row).isMutable():
					x = column
					y = row
					break
		
		self.assertNotEqual(x, None, "Failed to find a mutable cell.")
		self.assertNotEqual(y, None, "Failed to find a mutable cell.")

		guess = random.randint(1, 9)

		self.board.submitAnswer(x, y, guess)
		self.assertEqual(self.board.getCell(x, y).getAnswer(), guess, "failed to submit answer " + str(guess) + " to (" + str(x) + ", " + str(y) + ")")

		# submitting outside either index range (0~8) or answer range (1~9) results in None
		self.assertEqual(self.board.submitAnswer(-1, 0, guess), None, "submitted bad answer " + str(guess) + " to (-1, 0)")
		self.assertEqual(self.board.submitAnswer(9, 0, guess), 	None, "submitted bad answer " + str(guess) + " to (9, 0)")
		self.assertEqual(self.board.submitAnswer(0, -1, guess), None, "submitted bad answer " + str(guess) + " to (0, -1)")
		self.assertEqual(self.board.submitAnswer(0, 9, guess),  None, "submitted bad answer " + str(guess) + " to (0, 9)")
		self.assertEqual(self.board.submitAnswer(x, y, 0), 	None, "submitted bad answer 0 to (" + str(x) + ", " + str(y) + ")")
		self.assertEqual(self.board.submitAnswer(x, y, 10),	None, "submitted bad answer 10 to (" + str(x) + ", " + str(y) + ")")
		
		# submitting correct answer should yield True
		guess = self.board.getCell(x, y).getSolution()
		self.assertTrue(self.board.submitAnswer(x, y, guess))

		# submitting an incorrect answer should yield False
		guess = (guess + 5) % 9 + 1
		self.assertFalse(self.board.submitAnswer(x, y, guess))

	#--------------------------------------------------------------------------------
	def test_10_board_is_complete_when_all_filled(self):
	#--------------------------------------------------------------------------------
		unsolved = []

		for row in range(9):
			for column in range(9):
				if self.board.getCell(column, row).isMutable():
					unsolved.append((column, row))

		self.assertEqual(len(unsolved), 10, "Number of mutable cells different than constructor argument")

		# fill the board with correct answers
		for cell in unsolved:						
			solution = self.board.getCell(cell[0], cell[1]).getSolution()
			self.board.submitAnswer(cell[0], cell[1], solution)

		# a fully completed board with all correct solutions should return 'Correct'
		self.assertEqual(self.board.isSolved(), 'Correct', "Board was not found to be correctly completed.")

		# submit an incorrect answer
		solution = self.board.getCell(unsolved[0][0], unsolved[0][1]).getSolution()
		incorrect = (solution + 5) % 9 + 1

		self.board.submitAnswer(unsolved[0][0], unsolved[0][1], incorrect)

		# a fully completed board with an incorrect solution should return 'Incorrect'
		self.assertEqual(self.board.isSolved(), 'Incorrect', "Perturbed complete board not found to be incorrect.")

	#--------------------------------------------------------------------------------
	def test_11_board_correctness_checks(self):
	#--------------------------------------------------------------------------------
		# generate a totally clued-in basic board (no transformations applied), which should be entirely correct.
		test = Board(0, False)

		self.assertEqual(test.isSolved(), 'Correct', 'Totally clued-in (solved) board is not correct')

		# check row correctness
		for y in range(9):
			self.assertTrue(test.isRowCorrect(y), "Row " + str(y) + " is invalid: " + str([cell.getAnswer() for cell in test.getRow(y)]))

		# check column correctness
		for x in range(9):
			self.assertTrue(test.isColumnCorrect(x), "Column " + str(x) + " is invalid: " + str([cell.getAnswer() for cell in test.getColumn(x)]))

		# check block correctness
		for x in range(3):
			for y in range(3):
				self.assertTrue(test.isBlockCorrect(x, y), "Block at (" + str(x) + ", " + str(y) + ") is invalid: " + str([[cell.getAnswer() for cell in row] for row in test.getBlock(x, y)]))

		# randomly hide a cell
		x = random.randint(0, 8)
		y = random.randint(0, 8)
		bx = math.floor(x / 3)
		by = math.floor(y / 3)

		test.getCell(x, y).hideAnswer()

		# hidden (blank) cells should make the resident row, column and block incorrect
		self.assertFalse(test.isRowCorrect(y), "Perturbed row " + str(y) + " is still valid: " + str([cell.getAnswer() for cell in test.getRow(y)]))
		self.assertFalse(test.isColumnCorrect(x), "Perturbed column " + str(x) + " is still valid: " + str([cell.getAnswer() for cell in test.getColumn(x)]))
		self.assertFalse(test.isBlockCorrect(bx, by), "Perturbed block at (" + str(bx) + ", " + str(by) + ") is still valid: " + str([[cell.getAnswer() for cell in row] for row in test.getBlock(bx, by)]))

		# Submit a bad answer
		solution = test.getCell(x, y).getSolution()
		incorrect = (solution + 5) % 9 + 1


		test.submitAnswer(x, y, incorrect)

		# Incorrect cells should make the resident row, column and block incorrect
		self.assertFalse(test.isRowCorrect(y), "Perturbed row " + str(y) + " is still valid: " + str([cell.getAnswer() for cell in test.getRow(y)]))
		self.assertFalse(test.isColumnCorrect(x), "Perturbed column " + str(x) + " is still valid: " + str([cell.getAnswer() for cell in test.getColumn(x)]))
		self.assertFalse(test.isBlockCorrect(bx, by), "Perturbed block at (" + str(bx) + ", " + str(by) + ") is still valid: " + str([[cell.getAnswer() for cell in row] for row in test.getBlock(bx, by)]))

	#--------------------------------------------------------------------------------
	def test_12_board_validity_checks(self):
	#--------------------------------------------------------------------------------
		# generate a totally clued-in basic board (no transformations applied), which should be entirely correct.
		test = Board(0, False)

		# check board validity
		self.assertTrue(test.isValid(), "Board found to be invalid.")

		# A board with two solution numbers in the same row should be invalid
		memory = test.getCell(3, 4).solution_
		test.getCell(3, 4).solution_ = test.getCell(7, 4).solution_

		self.assertFalse(test.isValid(), "Board not properly invalidated on row: " + str([cell.getSolution() for cell in test.getRow(4)]))

		# Replace valid value - should re-instate validity
		test.getCell(3, 4).solution_ = memory

		self.assertTrue(test.isValid(), "Board found to be invalid.")

		# A board with two solution numbers in the same column should be invalid
		memory = test.getCell(5, 4).solution_
		test.getCell(5, 4).solution_ = test.getCell(1, 4).solution_

		self.assertFalse(test.isValid(), "Board not properly invalidated on column: " + str([cell.getSolution() for cell in test.getColumn(5)]))

		# Replace valid value - should re-instate validity
		test.getCell(5, 4).solution_ = memory

		self.assertTrue(test.isValid(), "Board found to be invalid.")

		# A board with two solution numbers in the same block should be invalid
		memory = test.getCell(5, 5).solution_
		test.getCell(5, 5).solution_ = test.getCell(3, 4).solution_

		self.assertFalse(test.isValid(), "Board not properly invalidated on block: " + str([cell.getSolution() for row in test.getBlock(1, 1) for cell in row]))

		# Replace valid value - should re-instate validity
		test.getCell(5, 5).solution_ = memory

		self.assertTrue(test.isValid(), "Board found to be invalid.")

	#--------------------------------------------------------------------------------
	def test_13_swap_columns(self):
	#--------------------------------------------------------------------------------
		test = Board(0, False)

		x1 = random.randint(0, 4)
		x2 = random.randint(5, 8)

		col1 = [cell.getSolution() for cell in test.getColumn(x1)]
		col2 = [cell.getSolution() for cell in test.getColumn(x2)]

		# swap col1 and col2
		test.swapColumns(x1, x2)

		self.assertEqual(col1, [cell.getSolution() for cell in test.getColumn(x2)], "Swap of column: " + str(col1) + " and column 2: " + str(col2) + " failed.")
		self.assertEqual(col2, [cell.getSolution() for cell in test.getColumn(x1)], "Swap of column: " + str(col1) + " and column 2: " + str(col2) + " failed.")

		# swapping with out-of-range indices should result in None
		self.assertEqual(test.swapColumns(3, -1), None, "Swapping columns 3 and -1 did not return None")
		self.assertEqual(test.swapColumns(4, 9), None, "Swapping columns 4 and 9 did not return None")

	#--------------------------------------------------------------------------------
	def test_14_swap_rows(self):
	#--------------------------------------------------------------------------------
		test = Board(0, False)

		y1 = random.randint(0, 4)
		y2 = random.randint(5, 8)

		row1 = [cell.getSolution() for cell in test.getRow(y1)]
		row2 = [cell.getSolution() for cell in test.getRow(y2)]

		# swap row1 and row2
		test.swapRows(y1, y2)

		self.assertEqual(row1, [cell.getSolution() for cell in test.getRow(y2)], "Swap of row: " + str(row1) + " and row 2: " + str(row2) + " failed.")
		self.assertEqual(row2, [cell.getSolution() for cell in test.getRow(y1)], "Swap of row: " + str(row1) + " and row 2: " + str(row2) + " failed.")

		# swapping with out-of-range indices should result in None
		self.assertEqual(test.swapRows(3, -1), None, "Swapping row 3 and -1 did not return None")
		self.assertEqual(test.swapRows(4, 9), None, "Swapping row 4 and 9 did not return None")

	#--------------------------------------------------------------------------------
	def test_15_swap_along_diagonals(self):
	#--------------------------------------------------------------------------------
		test1 = Board(0, False)
		test2 = Board(0, False)
		control = Board(0, False)
	
		test1.swapMajorDiagonal()

		# Board should remain valid
		self.assertTrue(test1.isValid(), "Board invalidated following swap along major diagonal.")

		# Cells should match the originals which are diagonally across and equi-distant
		# to the main diagonal.

		for x in range(9):
			for y in range(9):
				self.assertEqual(control.getCell(x, y).getSolution(), test1.getCell(y, x).getSolution(), "Control cell (" + str(x) + ", " + str(y) + ") does not equate to cell (" + str(y) + ", " + str(x) + ") after major diagonal swap.")

		test2.swapMinorDiagonal()

		# Board should remain valid
		self.assertTrue(test2.isValid(), "Board invalidated following swap along minor diagonal.")

		# Cells should match the originals which are diagonally across and equi-distant
		# to the minor diagonal.

		for x in range(9):
			for y in range(9):
				self.assertEqual(control.getCell(x, y).getSolution(), test2.getCell(8 - y, 8 - x).getSolution(), "Control cell (" + str(x) + ", " + str(y) + ") does not equate to cell (" + str(8 - y) + ", " + str(8 - x) + ") after minor diagonal swap.")

		# Swapping twice on the same diagonal should result in the original board.
		test1.swapMajorDiagonal()
		self.assertEqual(control.getRaw(), test1.getRaw(), "Swapping twice on the main diagonal caused an effective difference.")

		test2.swapMinorDiagonal()
		self.assertEqual(control.getRaw(), test2.getRaw(), "Swapping twice on the minor diagonal caused an effective difference.")

	#--------------------------------------------------------------------------------
	def test_16_swap_major_columns_of_blocks(self):
	#--------------------------------------------------------------------------------
		control = Board(0, False)
		test = Board(0, False)

		x1 = random.randint(0, 1)
		x2 = random.randint(x1+1, x1+2) % 3

		test.swapBlockColumns(x1, x2)

		# Swapping two columns of blocks should let the board remain valid.
		self.assertTrue(test.isValid(), "Swapping major columns " + str(x1) + " and " + str(x2) + " invalidated the board.")

		# Swapping major columns essentially keeps the blocks the same, but swaps their horizontal region.
		for y in range(3):
			self.assertEqual([cell.getSolution() for row in control.getBlock(x1, y) for cell in row], [cell.getSolution() for row in test.getBlock(x2, y) for cell in row], "Control block at (" + str(x1) + ", " + str(y) + ") did not equate to block at (" + str(x2) + ", " + str(y) + ") after major column swap")

		# Swapping twice on the same major columns should result in the original board.
		test.swapBlockColumns(x2, x1)
		self.assertEqual(control.getRaw(), test.getRaw(), "Swapping twice on the same major block columns caused an effective difference.")

		# Swapping indices out of range should yield None
		self.assertEqual(test.swapBlockColumns(-1, 1), None, "Swapping columns -1 and 1 did not return None")
		self.assertEqual(test.swapBlockColumns(1, 3), None, "Swapping columns 1 and 3 did not return None")


	#--------------------------------------------------------------------------------
	def test_17_swap_major_rows_of_blocks(self):
	#--------------------------------------------------------------------------------
		control = Board(0, False)
		test = Board(0, False)

		y1 = random.randint(0, 1)
		y2 = random.randint(y1+1, y1+2) % 3

		test.swapBlockRows(y1, y2)

		# Swapping two rows of blocks should let the board remain valid.
		self.assertTrue(test.isValid(), "Swapping major rows " + str(y1) + " and " + str(y2) + " invalidated the board.")

		# Swapping major rows essentially keeps the blocks the same, but swaps their vertical region.
		for x in range(3):
			self.assertEqual([cell.getSolution() for row in control.getBlock(x, y1) for cell in row], [cell.getSolution() for row in test.getBlock(x, y2) for cell in row], "Control block at (" + str(x) + ", " + str(y1) + ") did not equate to block at (" + str(x) + ", " + str(y2) + ") after major row swap")

		# Swapping twice on the same minor rows should result in the original board.
		test.swapBlockRows(y2, y1)
		self.assertEqual(control.getRaw(), test.getRaw(), "Swapping twice on the same major block rows caused an effective difference.")

		# Swapping indices out of range should yield None
		self.assertEqual(test.swapBlockRows(-1, 1), None, "Swapping rows -1 and 1 did not return None")
		self.assertEqual(test.swapBlockRows(1, 3), None, "Swapping rows 1 and 3 did not return None")

	#--------------------------------------------------------------------------------
	def test_18_swap_unique_digits(self):
	#--------------------------------------------------------------------------------
		control = Board(0, False)
		test = Board(0, False)

		s = random.sample(range(1, 10), 2)
		a = s[0]
		b = s[1]

		test.swapDigits(a, b)

		# Swapping all instances of two specific digits should retain board validity.
		self.assertTrue(test.isValid(), "Swapping digits " + str(a) + " and " + str(b) + " invalidated the board.")
		
		# After swapping, any cell which was 'a' should now be 'b', and vice-versa.
		for x in range(9):
			for y in range(9):
				if control.getCell(x, y).getSolution() == a:
					self.assertEqual(test.getCell(x, y).getSolution(), b, "Control cell (" + str(x) + ", " + str(y) + ") => " + str(a) + ", but test cell is " + str(control.getCell(x, y).getSolution()) + " after swapping digits " + str(a) + " and " + str(b))

		# Swapping twice on the same two digits should result in the original board.
		test.swapDigits(a, b)
		self.assertEqual(control.getRaw(), test.getRaw(), "Swapping twice on the same digits caused an effective difference.")

	#--------------------------------------------------------------------------------
	def test_19_flip_board_horizontally(self):
	#--------------------------------------------------------------------------------
		control = Board(0, False)
		test = Board(0, False)

		test.flipHorizontal()

		# Flipped board should retain validity.
		self.assertTrue(test.isValid(), "Flipping board horizontally invalidated it.")

		# First column of flipped board should be same as last of original. 2nd same as 8th, etc.
		for x in range(9):
			self.assertEqual([cell.getSolution() for cell in control.getColumn(x)], [cell.getSolution() for cell in test.getColumn(8 - x)], "Control column " + str(x) + " did not equate to column " + str(8 - x) + " after flipping horizontally")
		
		# Flipping the board horizontally twice should result in the original board.
		test.flipHorizontal()
		self.assertEqual(control.getRaw(), test.getRaw(), "Flipping horizontally twice caused an effective difference.")

	#--------------------------------------------------------------------------------
	def test_20_flip_board_vertically(self):
	#--------------------------------------------------------------------------------
		control = Board(0, False)
		test = Board(0, False)

		test.flipVertical()

		# Flipped board should retain validity.
		self.assertTrue(test.isValid(), "Flipping board vertically invalidated it.")

		# First row of flipped board should be same as last of original. 2nd same as 8th, etc.
		for y in range(9):
			self.assertEqual([cell.getSolution() for cell in control.getRow(y)], [cell.getSolution() for cell in test.getRow(8 - y)], "Control row " + str(y) + " did not equate to row " + str(8 - y) + " after flipping vertically")
		
		# Flipping the board vertically twice should result in the original board.
		test.flipVertical()
		self.assertEqual(control.getRaw(), test.getRaw(), "Flipping vertically twice caused an effective difference.")

	#--------------------------------------------------------------------------------
	def test_21_swapping_regional_columns_retains_validity(self):
	#--------------------------------------------------------------------------------
		test = Board(0, False)

		for i in range(20):
			x = random.randint(0, 2)
			c1 = random.randint(0, 1)
			c2 = random.randint(c1+1, c1+2) % 3

			test.swapColumns(x * 3 + c1, x * 3 + c2)
		
			# Swapping two columns in the same major block column should retain validity
			self.assertTrue(test.isValid(), "Swapping columns " + str(x * 3 + c1) + " and " + str(x * 3 + c2) + " within region " + str(x) + " invalidated the board.")

	#--------------------------------------------------------------------------------
	def test_22_swapping_regional_rows_retains_validity(self):
	#--------------------------------------------------------------------------------
		test = Board(0, False)

		for i in range(20):
			y = random.randint(0, 2)
			r1 = random.randint(0, 1)
			r2 = random.randint(r1+1, r1+2) % 3

			test.swapRows(y * 3 + r1, y * 3 + r2)
		
			# Swapping two rows in the same major block row should retain validity
			self.assertTrue(test.isValid(), "Swapping row " + str(y * 3 + r1) + " and " + str(y * 3 + r2) + " within region " + str(y) + " invalidated the board.")

	#--------------------------------------------------------------------------------
	def test_23_rotate_board_clockwise(self):
	#--------------------------------------------------------------------------------
		control = Board(0, False)
		test = Board(0, False)

		test.rotate()

		# Rotated board should retain validity.
		self.assertTrue(test.isValid(), "Rotating board clockwise invalidated it.")

		# Cell at (x, y) should now be at (8 - y, x) in the clockwise rotated board.
		for y in range(9):
			for x in range(8 - y):
				self.assertEqual(control.getCell(x, y).getSolution(), test.getCell(8 - y, x).getSolution(), "Control cell (" + str(x) +", " + str(y) + ") did not equate to cell (" + str(8 - y) + ", " + str(x) + ") after clockwise rotation.")

		# Rotating the board 360 degrees should result in the original board.
		test.rotate()
		test.rotate()
		test.rotate()
		self.assertEqual(control.getRaw(), test.getRaw(), "Rotating the board 360 degrees caused an effective difference.")

	#--------------------------------------------------------------------------------
	def test_24_randomly_perturb_board(self):
	#--------------------------------------------------------------------------------
		for i in range(20):
			test = Board(0, False)
			control = test.getRaw()

			executed = test.perturb()

			# Perturbing the board should retain its validity.
			self.assertTrue(test.isValid(), "Perturbing the board with transformation: <" + executed + "> invalidated it.")
			# Perturbing the board should change its state.
			self.assertNotEqual(test.getRaw(), control, "Perturbing the board with transformation: <" + executed + "> had no effect on it.")

		compound = Board(0, False)

		for i in range(100):
			compound.perturb()

			# Compound perturbance should retain board validity.
			self.assertTrue(test.isValid(), "Perturbing the board with transformation: <" + executed + "> invalidated it during compound perturbance.")

	#--------------------------------------------------------------------------------
	def test_25_board_is_well_formed(self):
	#--------------------------------------------------------------------------------
		for i in range(50):
			test = Board(i)

			# All randomly generated boards should be valid.
			self.assertTrue(test.isValid(), "Randomly generated board with " + str(81 - i) + " clues is invalid.")

if __name__ == "__main__":
	unittest.main(verbosity = 2)
