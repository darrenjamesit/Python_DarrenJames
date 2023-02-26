from flask import Flask, render_template

app = Flask('HydroGas SRL')


@app.route('/')
@app.route('/home')
def home():
    return render_template('')


@app.route('/portfolio')
def port():
    return 'Coming soon.'


if __name__ == '__main__':
    app.run(debug=True)
