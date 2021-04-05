# imports flask library 
from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretz"

# debug = DebugToolbarExtension(app)

# imports Madlibs functionality from stories.py
from stories import story

# app routes for Madlibs game 

@app.route('/')
def home_form():
    """Renders form for Madlib entry."""
    prompts = story.prompts

    return render_template('home.html', prompts=prompts)

@app.route('/story', methods=['POST'])
def show_story():
    """Shows story after words are entered into Madlib form."""
    text = story.generate(request.args)

    return render_template("story.html", text=text)