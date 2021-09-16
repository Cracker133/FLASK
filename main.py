from flask import Flask

#WSGI
app = Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return "Welcome to Praxis"

@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome to praxis {your_name}"

if __name__ == "__main__":
    app.run(debug =True)