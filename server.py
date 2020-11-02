from flask import Flask, render_templates, url_for
app = Flask(__name__)


@app.route('/')
def yo():
	return render_template('index.html')

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/blog')
def blog():
	return 'not hotdog'

@app.route('/blog/2020/donkey')
def blog2():
	return 'you are a space donkey'