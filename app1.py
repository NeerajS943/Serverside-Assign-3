from flask import Flask
app=Flask(__name__)

# creating main route, with name and dynamic name paths 

@app.route("/")
def index():
    return f"Hello Kane Williamson"

@app.route("/name")
def sample():
    return f"<h1>Hello, welcome to the new page</h1>"

@app.route("/<name>")
def sample2(name):
    return f"<h1>Hey, {name}</h1>"