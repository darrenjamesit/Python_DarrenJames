from flask import Flask, render_template, request
app = Flask('Students')

st = {
    23: {'fname': 'Dana', 'lname': 'Popescu', 'class': '9b'},
    2: {'fname': 'Ion', 'lname': 'Pop', 'class': '10c'},
    31: {'fname': 'Gelu', 'lname': 'Ionescu', 'class': '10c'},
    15: {'fname': 'Geta', 'lname': 'Ionescu', 'class': '9b'},
}
x = list(st.values())
y = [d['class'] for d in x]


@app.route('/')
@app.route('/home/')
def home():
    return "This is the main page."


@app.route('/students/')
def all_students():
    return render_template('students.html', title='Students', students=st)


@app.route('/student/<int:stud_id>')
def student(stud_id):
    return render_template('stud_id.html', students=st, stud_id=stud_id)


@app.route('/class/<class_name>')
def clas(class_name):
    return render_template('class.html', students=st, class_name=class_name, x=x, y=y)


@app.route('/search', methods=['GET', 'POST'])
def search():
    print(request.form)
    print(dict(request.form))
    print(request.form.get('fname'))
    return render_template('search.html', search=request.form)


if __name__ == '__main__':
    app.run(debug=True)