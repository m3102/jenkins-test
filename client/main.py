from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside 
        password = request.form.get('password')

        if username == 'root' and password == 'pass':      
            return render_template("login.html", username=username)
        else:
            return render_template("index.html")
    return render_template("index.html")
    

@app.route("/<name>")
def user(name):
	return f"Hello {name}"

if __name__ == "__main__":
	app.run()