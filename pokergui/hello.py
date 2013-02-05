from flask import Flask
from flask import render_template
from flask import url_for

import sys
sys.path.append('../libpoker/')
import poker

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/chentrainer')
def chenTrainer():
	chenDeck = poker.qDeck()
	chenDeck.shuffle()
	chenCards = (chenDeck.pop(), chenDeck.pop())
	return render_template('chen.html', chenCards = chenCards, chenValue = poker.chenFormula( chenCards[0], chenCards[1] ) )

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run(debug=True)