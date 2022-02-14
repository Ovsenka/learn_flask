from distutils.log import debug
from flask import Flask, render_template, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "12334823u5hdnkjxbnmvbi23u23u4235h235k"


@app.route("/")
def main():
    return render_template("practice.html", title="Авторизация")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.errorhandler(404)
def notfound():
    return render_template("error404.html", title="Страница не найдена")

if __name__ == "__main__":
    app.run()
