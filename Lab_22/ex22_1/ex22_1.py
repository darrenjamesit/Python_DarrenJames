from flask import Flask, render_template
app = Flask('Students')

st = {
    23: {'fname': 'Dana', 'lname': 'Popescu', 'class': '9b'},
    2: {'fname': 'Ion', 'lname': 'Pop', 'class': '10c'},
    31: {'fname': 'Gelu', 'lname': 'Ionescu', 'class': '10c'},
    15: {'fname': 'Geta', 'lname': 'Ionescu', 'class': '9b'},
}


@app.route('/')
@app.route('/home/')
def home():
    return "This is the main page."


@app.route('/students/')
def all_students():
    return render_template('students.html', title='Students', students=st)


@app.route('/student/<int:stud_id>')
def student(stud_id):
    return render_template('stud_id.html', student=st.get(stud_id))


if __name__ == '__main__':
    app.run(debug=True)