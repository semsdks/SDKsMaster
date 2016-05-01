
from bottle import run, route, view, app, hook
from bottle import get, put, post, request, redirect, template
from bottle import static_file, error, debug
from functools import wraps
from beaker.middleware import SessionMiddleware
import json
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/src/Controller")
from BoardController import *

from bottle import default_app, route


app = app()
session_opts = {
    'session.auto': True,
    'session.cookie_expires': True,
    'session.encrypt_key': 'please use a random key and keep it secret!',
    'session.timeout': 3600 * 24,  # 1 day
    'session.type': 'cookie',
    'session.validate_key': True,
    'session.httponly': True,
}
application = SessionMiddleware(app, session_opts)


@route('/')
@validate
def index():
    return resume()

@route('/start')
def new_game():
    if game_exists():
        redirect('/')
    return play()

@post('/modify')
@validate
def update_handler():
    return update()

@route('/stop')
@validate
def end_game():
    return end()

@route('/status')
@validate
def game_status():
    return status()

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')


def main():
    debug(True)
    run(app=application, quiet=False, reloader=True)

if __name__ == "__main__":
    main()
