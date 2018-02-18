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

@app.route('/categorical')
@nocache
def categorical():
    return render_template('categorical.html')

@app.route('/nominal')
@nocache
def nominal():
    return render_template('nominal.html')

@app.route('/ordinal')
@nocache
def ordinal():
    return render_template('ordinal.html')

@app.route('/continuous')
@nocache
def continuous():
    return render_template('continuous.html')

@app.route('/discrete')
@nocache
def discrete():
    return render_template('discrete.html')

@app.route('/scatter_plot')
@nocache
def scatter_plot():
    return render_template('scatter_plot.html')

@app.route('/about')
@nocache
def about():
    return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)