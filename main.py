from flask import Flask,render_template,request

#WSGI
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome to praxis {your_name}"

@app.route('/checking_req',methods=['POST','GET'])
def get_req_parameters():
    name= request.args.get("student_name")
    roll_no =request.args.get("roll_no")
    return f"Student name is {name} and roll number is {roll_no}",206

if __name__ == "__main__":
    app.run(debug =True)