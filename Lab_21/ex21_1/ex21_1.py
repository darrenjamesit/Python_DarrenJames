from flask import Flask
app = Flask('HydroGas SRL')


@app.route('/')
@app.route('/home')
def home():
    return 'Welcome! This page is under construction'


@app.route('/portfolio')
def port():
    return 'Coming soon.'


if __name__ == '__main__':
    app.run(debug=True)
