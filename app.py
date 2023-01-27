from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config['SECRET_KEY'] = "secretSauce123"
debug = DebugToolbarExtension(app)

@app.route("/")
def show_form():
    prompts = story.prompts 
    return render_template("homePage.html", prompts = prompts)

@app.route("/story")
def show_story():
    output = story.generate(request.args)
    return render_template("showStory.html", output = output)