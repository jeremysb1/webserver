from flask import Flask, render_templates, url_for
app = Flask(__name__)


@app.route('/<username>/<int:post_id>')
def yo(username=None, post_id=None):
	return render_template('index.html', name=username, post_id=post_id)

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/blog')
def blog():
	return 'not hotdog'

@app.route('/blog/2020/donkey')
def blog2():
	return 'you are a space donkey'