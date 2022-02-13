from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

print(__name__)

@app.route("/")
def on_main():
    return render_template("practice.html", title="Главная страница")

if __name__ == "__main__":
    app.run()
