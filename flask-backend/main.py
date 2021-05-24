from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

# add as the root route
@app.route("/")
def index():
    return render_template("index.html", penguin="Hello CT!")


if __name__ == "__main__":
    """
    Run python -u main.py and open to localhost:8080 to see template.
    Run python -u run_program.py to test the program
    """
    app.run(host="127.0.0.1", port=8080, debug=True)