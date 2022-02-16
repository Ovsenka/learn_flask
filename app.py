from distutils.log import debug
from flask import Flask, render_template, flash, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "12334823u5hdnkjxbnmvbi23u23u4235h235k"


@app.route("/")
def main():
    return render_template("practice.html", title="Hello")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/register")
def register():
    return render_template("register.html", title="Регистрация")

@app.route("/login")
def login():
    return render_template("login.html", title="Войти")

'''
@app.errorhandler(404)
def notfound():
    return render_template("error404.html", title="Страница не найдена")

@app.errorhandler(500)
def er():
    return "LOL"'''

if __name__ == "__main__":
    app.run()
