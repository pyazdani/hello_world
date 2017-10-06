from flask import Flask, render_template

app = Flask(__name__)

# the @ symbol is noted as a decorator in python/flask
@app.route('/')
# this function is what will be executed when users visit localhost:5000
def MyPortfolio():
	#Tell our server to send index.html back to the client
	return render_template("index.html")


@app.route("/projects")
def Projects():
	return render_template("projects.html")

@app.route("/about")
def About():
	return render_template("about.html")



# tells our server to run
app.run(debug=True)

