from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from nocache import nocache

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
@nocache
def index():
	return render_template('index.html')

@app.route('/quantitative')
@nocache
def quantitative():
    return render_template('quantitative.html')

@app.route('/qualitative')
@nocache
def qualitative():
    return render_template('qualitative.html')

@app.route('/about')
@nocache
def about():
    return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)