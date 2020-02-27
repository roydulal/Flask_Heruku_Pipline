from flask import Flask
app =Flask(__name__)
@app.route("/")
def index():
    return "My fast Flask setup"
if __name__ == "__main__":
    app.run(use_reloader=True)