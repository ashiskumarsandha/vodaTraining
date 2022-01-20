from flask import Flask
app = Flask(__name__)
@app.route("/welcome")
def hello():
	return "Welcome to Ashis Python Project!"
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)