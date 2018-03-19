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

@app.route('/histogram_plot')
@nocache
def histogram_plot():
    return render_template('histogram_plot.html')

@app.route('/dot_plot')
@nocache
def dot_plot():
    return render_template('dot_plot.html')

@app.route('/box_plot')
@nocache
def box_plot():
    return render_template('box_plot.html')

@app.route('/parallel_coordinate_plot')
@nocache
def parallel_coordinate_plot():
    return render_template('parallel_coordinate_plot.html')

@app.route('/scatter_plot_matrix')
@nocache
def scatter_plot_matrix():
    return render_template('scatter_plot_matrix.html')

@app.route('/mosaic_plot')
@nocache
def mosaic_plot():
    return render_template('mosaic_plot.html')

@app.route('/bar_chart')
@nocache
def bar_chart():
    return render_template('bar_chart.html')

@app.route('/about')
@nocache
def about():
    return render_template('about.html')

@app.route('/resources')
@nocache
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
	app.run(debug=True)