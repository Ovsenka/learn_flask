from distutils.log import debug
from flask import Flask, render_template, flash, session, request, url_for, redirect, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "12334823u5hdnkjxbnm@#$!@!vbi2/ggr/24@#$@#$3u23u4235h235k"


@app.route("/")
def main():
    return render_template("practice.html", title="Hello")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/register")
def regist():
    return render_template("register.html", title="Регистрация")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST" and request.form['username'] == "testuser" and request.form['psw'] == "111":
        session['userLogged'] = request.form['username']
        return redirect(url_for("profile", username=session["userLogged"]))
    elif "userLogged" in session:
        return redirect(url_for("profile", username=session["userLogged"]))
    return render_template("login.html", title="Войти")
    
@app.route("/profile/<username>")
def profile(username):
    if "userLogged" not in session or session["userLogged"] != username:
        abort(401)
    return render_template("profile.html", user=username)


@app.errorhandler(404)
def notfound(err):
    return render_template("error404.html", title="Страница не найдена")

if __name__ == "__main__":
    app.run()
