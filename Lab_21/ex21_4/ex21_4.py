from flask import Flask, render_template

app = Flask('HydroGas SRL')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/portfolio')
def port():
    return render_template('portfolio.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
