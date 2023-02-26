from flask import Flask, render_template

app = Flask('HydroGas SRL')


@app.route('/')
@app.route('/home')
def home():
    rendered_template = render_template('home.html')
    welcome = '<p>Welcome! This page is under construction.</p>'
    return rendered_template + welcome


@app.route('/portfolio')
def port():
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)
