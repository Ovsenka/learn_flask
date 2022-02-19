from distutils.log import debug
from flask import Flask, render_template, flash, session, request, url_for, redirect, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "12334823u5hdnkjxbnm@#$!@!vbi2/ggr/24@#$@#$3u23u4235h235k"

users = []

@app.route("/")
def main():
    print(session)
    return render_template("practice.html", title="Hello")

@app.route("/index")
def index():
    print(session)
    return render_template("practice.html", title="Hello")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST" and request.form["psw"] == request.form["psw-repeat"]:
        print(request.form["optionsRadios"])
        session['user_logged'] = request.form['username']
        print(session)
        users.append((request.form['username'], request.form["psw"]))
        return redirect(url_for("profile", username=session["user_logged"]))
    elif "user_logged" in session:
        return redirect(url_for("profile", username=session["user_logged"]))
    return render_template("register.html", title="Регистрация")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST" and request.form['username'] == "1" and request.form['psw'] == "111":
        session['user_logged'] = request.form['username']
        return redirect(url_for("profile", username=session["user_logged"]))
    elif "user_logged" in session:
        return redirect(url_for("profile", username=session["user_logged"]))
    return render_template("login.html", title="Войти")
    
@app.route("/profile/<username>")
def profile(username):
    if "user_logged" not in session or session["user_logged"] != username:
        abort(401)
    return render_template("profile.html", user=username, is_logged=True)

@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "user_logged" in session:
        del session["user_logged"]
        return redirect(url_for("index"))


@app.errorhandler(404)
def notfound(err):
    return render_template("error404.html", title="Страница не найдена")

if __name__ == "__main__":
    app.run()
