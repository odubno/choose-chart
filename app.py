from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/quantitative')
def quantitative():
    return render_template('quantitative.html')

@app.route('/qualitative')
def qualitative():
    return render_template('qualitative.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)