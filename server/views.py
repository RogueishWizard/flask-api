from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def index_html():
    return render_template('index.html')
