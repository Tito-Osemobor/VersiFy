from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home ():
  return render_template("index.html")

@app.route("/practice", methods=["POST"])
def lyrics ():
  return render_template("practice.html")

if __name__ == "__main__":
  app.run(debug=True)