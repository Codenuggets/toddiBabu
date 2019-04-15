import os

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__, static_url_path="/static")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("img/general", filename)


@app.route('/weddings/<filename>')
def wedding_image(filename):
    return send_from_directory("img/weddings", filename)


@app.route('/bands/<filename>')
def band_image(filename):
    return send_from_directory("img/bands", filename)


@app.route('/')
def get_gallery():
    image_names = os.listdir('./img/general')
    print(image_names)
    return render_template("./gallery.html", image_names=image_names)


@app.route('/about')
def get_about():
    return render_template('about.html')


@app.route('/weddings')
def get_wedding():
    image_names = os.listdir('./img/weddings')
    return render_template('weddings.html', image_names=image_names)


@app.route('/bands')
def get_bands():
    image_names = os.listdir('./img/bands')
    return render_template('bands.html', image_names=image_names)


@app.route('/clients')
def get_clients():
    return render_template('clients.html')


@app.route('/contact')
def get_contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(port=8888, debug=True)
