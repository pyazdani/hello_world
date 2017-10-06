from flask import Flask, render_template

app = Flask(__name__)

# the @ symbol is noted as a decorator in python/flask
@app.route('/')
# this function is what will be executed when users visit localhost:5000
def hello_world():
	#Tell our server to send index.html back to the client
	return render_template("index.html")
# tells our server to run
app.run(debug=True)