from flask import Flask, render_templates, url_for
app = Flask(__name__)


@app.route('/')
def yo():
	return render_template('index.html')

@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/components.html')
def component():
	return render_template('components.html')

@app.route('/works.html')
def works():
	return render_template('works.html')

@app.route('/contact.html')
def contact():
	return render_template('contact.html')