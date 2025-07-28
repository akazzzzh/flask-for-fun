from flask import Flask, render_template, request
from model import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        marks = request.form['marks']
        new_student = Student(name=name, marks=float(marks))
        db.session.add(new_student)
        db.session.commit()
        return f"Student {name} added successfully!"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
