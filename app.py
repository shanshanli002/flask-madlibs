from flask import Flask
from flask import request, render_template
from stories import *
app = Flask(__name__)

words = {}

@app.route('/')
def home(): 
 
    print(words)
    return render_template('base.html')

@app.route('/story')
def add_story():
    words = {
    "place": request.args.get("place"), 
    "noun": request.args.get("noun"),
    "verb": request.args.get("verb"),
    "adjective": request.args.get("adjective"), 
    "plural_noun": request.args.get("plural-noun")
    } 
    
    userstory = story.generate(words)
    return render_template('story.html',userstory=userstory, words=words)