import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../Model")

from bottle import run, route, view, app
from bottle import request, redirect, template, response
from bottle import static_file, error, debug
from Board import Board
from functools import wraps
import json

# Make this a Session variable.
game_board = None

#----------------------------------------------------------------
def validate(func):
#----------------------------------------------------------------
# Validation decorator which wraps routes requiring a valid
# game. If no session/game exists, route is redirected to '/new'
#----------------------------------------------------------------
	@wraps(func)
	def call(*args, **kwargs):
		if not game_exists():
			return redirect('/start')
		return func(*args, **kwargs)
	return call

#----------------------------------------------------------------
def play(game_board=None):
#----------------------------------------------------------------
# Returns a template displaying a Sudoku game board
#----------------------------------------------------------------
	if game_board is None:
		game_board = Board(40, True)
	

	raw_map = game_board.getRaw()
	board_map = {}

	# Translate raw 2-D digit/None array into coord : number
	# mapping. Blank (solvable) cells are simply excluded
	# from the map.
	for y in range(9):	
		for x in range(9):
			if raw_map[y][x] != None:
				id = chr(ord('a')+y) + str(x+1)
				isMutable = game_board.getCell(x,y).isMutable()
				board_map[id] = (raw_map[y][x], isMutable)
	

	sess = request.environ.get('beaker.session')
	sess['game_board'] = game_board

	return template('index', board=board_map)

#----------------------------------------------------------------
def resume():
#----------------------------------------------------------------
# If returning user with previous game, gets game_board
# from session and begins play on previous game
#----------------------------------------------------------------
	sess = request.environ.get('beaker.session')
	game_board = sess['game_board']
	

	return play(game_board)

#----------------------------------------------------------------
def end():
#----------------------------------------------------------------
# Ends a game by retrieving current session and deleting
# Redirects to index for new game creation
#----------------------------------------------------------------
	sess = request.environ.get('beaker.session')
	sess.delete()
	return redirect('/')

#----------------------------------------------------------------	
def game_exists():
#----------------------------------------------------------------
# Checks session for valid cookie and existence of game_board
#----------------------------------------------------------------
	sess_id = request.cookies.get('beaker.session.id', False)
	if not sess_id:
		return False
	sess = request.environ.get('beaker.session')
	if 'game_board' not in sess:
		return False
	return True
	

#----------------------------------------------------------------
def update():
#----------------------------------------------------------------
# Receives API call with cell_id and value
# Submits a user's input to the board
# Sends response True if the guess was correct, False otherwise
#----------------------------------------------------------------
#----------------------OLD NOTES---------------------------------
# * cell_id : the character-int pair (row-column) where the guess
#	was made.
# * value : the user's guess (1~9) for the cell's solution.
# Submits a user's input to the board.
# Returns True if the guess was correct, and False otherwise.
#----------------------------------------------------------------
	correct = False
		

	try:
		try:
			cell_id = request.forms.get('id')
			value = request.forms.get('value')
		except:
			raise ValueError

	except ValueError:
		response.status = 400
		return

	sess = request.environ.get('beaker.session')
	game_board = sess['game_board']

	if game_board is not None:
		# Translate coordinates back to 2-D array.
		x = int(cell_id[1]) - 1
		y = ord(cell_id[0]) - ord('a')

		answer = int(value)
		

		# Submit the user's answer to the board.
		correct = game_board.submitAnswer(x, y, answer)

		# return 200 Success
		response.headers['Content-Type'] = 'application/json'
		return json.dumps({'id': cell_id,'correct': correct})

#----------------------------------------------------------------
def status():
#----------------------------------------------------------------
	sess = request.environ.get('beaker.session')
	game_board = sess['game_board']

	status_map = []
	
	for y in range(9):	
		for x in range(9):
			id = chr(ord('a')+y) + str(x+1)
			isCorrect = game_board.getCell(x,y).isCorrect()
			isMutable = game_board.getCell(x,y).isMutable()
			value = game_board.getCell(x,y).getAnswer()
			
			if value:
				status_map.append((id, isMutable, isCorrect))
	
	if game_board is not None:
		status = game_board.isSolved()


		# return 200 Success
		response.headers['Content-Type'] = 'application/json'
		return json.dumps({'status': status, 'status_map': status_map})