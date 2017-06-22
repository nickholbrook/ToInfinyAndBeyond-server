from flask import Flask
app = Flask(name)

@app.route("/")
def hello_world():
		return 'Welcome to To Infiny and Beyond!'
