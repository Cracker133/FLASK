from flask import Flask,render_template,request

#WSGI
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome to praxis {your_name}"


if __name__ == "__main__":
    app.run(debug =True)