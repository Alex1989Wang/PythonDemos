from flask.ext.bootstrap import Bootstrap
from flask import Flask
from flask import render_template
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    html_result = render_template("user.html", name=name)
    print(html_result)
    return html_result

if __name__ == "__main__":
    app.run(port=9999, debug=True)