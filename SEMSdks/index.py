from bottle import get, put, post, request, redirect, run, route, view, app, hook, template, static_file, error, debug
import json
from bottle import default_app, route

app = app()

@route('/')
@validate
def index():
    return play()

@route('/start')
def new_game():
    if game_exists():
        redirect('/')
    return play()

@post('/modify')
@validate
def update():
    return update()

@route('/stop')
@validate
def endgame():
    return end()

@route('/status')
@validate
def status():
    return status()

@route('/<filename:path>')
def static(filename):
    return static_file(filename, root='static/')

def main():
    run(app=application, reloader=True)

if __name__ == "__main__":
    main()
