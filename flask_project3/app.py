from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/first')
def first():
    return render_template('first.html')
FAI.run(debug=True)