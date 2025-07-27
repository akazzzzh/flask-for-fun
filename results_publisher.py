from flask import Flask, redirect, url_for,render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("dummy.html")

@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score>=40:
        res = "PASS"
    else:
        res = "FAIL"
    exp = {'score':score, 'res':res }
    return render_template("success_file.html",result = exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "Marks scored is: " + str(score) + " — So you're failed"

@app.route('/results/<int:marks>')
def results(marks):
    if marks < 30:
        return redirect(url_for('fail', score=marks))   
    else:
        return redirect(url_for('success', score=marks))  
@app.route('/submit',methods = ['POST','GET'])
def submit():
    avg = 0
    if request.method =='POST':
        Fundamentals_of_Cryptography = float(request.form['Fundamentals_of_Cryptography'])
        Data_Visualization = float(request.form['Data_Visualization'])
        Soft_Computing = float(request.form['Soft_Computing'])
        Cloud_Computing = float(request.form['Cloud_Computing'])
        avg = ( Fundamentals_of_Cryptography+Data_Visualization +Soft_Computing+Cloud_Computing)/4
        if avg>=40:
            return redirect(url_for('success',score= avg))
        else:
            return redirect(url_for('fail',score = avg))
    return "Please submit the form via POST"

if __name__ == "__main__":
    app.run(debug=True)
