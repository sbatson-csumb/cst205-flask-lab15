import os
import random
from PIL import Image
from image_info import image_info
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

def negative(image):
    result = Image.new("RGB", image.size)

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            new_pixel = (255 - r, 255 - g, 255 - b)
            result.putpixel((x, y), new_pixel)

    return result


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


#@app.route("/image")
#def image():
#    return render_template(
 #       "image.html",
 #       image_url="https://picsum.photos/id/237/600/400"
 #   )

@app.route("/image")
def image():
    return render_template("image.html")

@app.route("/details")
def details():
    return render_template(
        "dictionary.html",
        image_info=image_info
    )

@app.route("/random")
def random_image():
    image_names = [
        "img1.jpg",
        "img2.jpg",
        "img3.jpg"
    ]

    selected_name = random.choice(image_names)
    selected_path = os.path.join("static", "images", selected_name)

    original = Image.open(selected_path).convert("RGB")
    negative_image = negative(original)

    output_path = os.path.join(
        "static",
        "generated",
        "negative.jpg"
    )

    negative_image.save(output_path)

    return render_template(
        "random.html",
        image_name="generated/negative.jpg",
        original_name=selected_name
    )

@app.route("/bootstrap")
def bootstrap_page():
    return render_template("bootstrap.html")