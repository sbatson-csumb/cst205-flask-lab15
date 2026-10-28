from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    classmates = [
        ("Sam", "TTYL", "Talk to You Later"),
        ("Nate", "EGBDF", "Every Good Boy Deserves Fudge (some music acronym idk)"),
        ("James", "FUBAR", "Effed Up Beyond Regcognition")
    ]

    html = ""

    for name, acronym, meaning in classmates:
        html += f"<p>{name}: {acronym} ({meaning})</p>"

    return html


@app.route("/sam")
def sam():
    return render_template(
        "template.html",
        acronym="LMAO"
    )


@app.route("/image")
def image():
    return render_template(
        "image.html",
        image_url="https://picsum.photos/id/237/600/400"
    )