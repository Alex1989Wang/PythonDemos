from flask.ext.bootstrap import Bootstrap
from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config["SECRET_KEY"] = "Alex1989Wang.foxmail.com"
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name.")
        session["name"] = form.name.data
        return redirect(url_for("index"))
    return render_template("index.html", form=form, name=session.get("name"), current_time=datetime.utcnow())

@app.route("/user/<name>")
def user(name):
    html_result = render_template("user.html", name=name)
    print(html_result)
    return html_result

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

class NameForm(Form):
    name = StringField("What's your name?", validators=[Required()])
    submit = SubmitField("Submit")

if __name__ == "__main__":
    app.run(port=9999, debug=True)