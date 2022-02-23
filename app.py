from distutils.log import debug
from flask import Flask, render_template, flash, session, request, url_for, redirect, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "12334823u5hdnkjxbnm@#$!@!vbi2/ggr/24@#$@#$3u23u4235h235k"

users = {}

@app.route("/")
def main():
    print(users)
    if "user_logged" in session:
        is_logged = True
    else:
        is_logged = False
    return render_template("practice.html", title="Hello", is_logged=is_logged)

@app.route("/index")
def index():
    print(session)
    if "user_logged" in session:
        is_logged = True
    else:
        is_logged = False
    return render_template("practice.html", title="Hello", is_logged=is_logged)

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/about")
def about():
    return render_template("about.html", title="о сайте")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST" and request.form["psw"] == request.form["psw-repeat"]:
        session['user_logged'] = request.form['username']
        users[request.form['username']] = ( request.form["psw"], request.form["optionsRadios"], request.form["age"])
        return redirect(url_for("profile", username=session["user_logged"]))
    elif "user_logged" in session:
        return redirect(url_for("profile", username=session["user_logged"]))
    return render_template("register.html", title="Регистрация")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(users)
        if users[request.form['username']][0] == request.form['psw']:
            session['user_logged'] = request.form['username']
            return redirect(url_for("profile", username=session["user_logged"]))
    elif "user_logged" in session:
        return redirect(url_for("profile", username=session["user_logged"]))
    return render_template("login.html", title="Войти")
    
@app.route("/profile/<username>")
def profile(username):
    if "user_logged" not in session or session["user_logged"] != username:
        abort(401)
    return render_template("profile.html", user=username, sex=users[session["user_logged"]][1], age=users[session["user_logged"]][2], title=username, is_logged=True)

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
