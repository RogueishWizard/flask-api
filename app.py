import time
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def get_current_time():
    return { 'time': time.time() }

@app.route('/hello')
@app.route('/hello/<name>')
def get_greeting(name=None):
    return render_template('hello.html',name=escape(name))

if __name__ == '__main__':
    app.run(debug=True)
