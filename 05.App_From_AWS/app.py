from flask import Flask
app = Flask(__name__)
@app.route("/welcome")
def hello():
	return "Welcome to Ashis Python Project!"
@app.route("/about")
def hello():
	return "This is my sample Python Project running from AWS EC2! Feel free to go to Welcome Page : http://13.127.26.92/welcome"
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)