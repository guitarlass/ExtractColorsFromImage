from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap5
import os
import extract_colors as ec

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():
    colors = []
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
        else:
            image = request.files['image']
            path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(path)
            if path:
                colors = ec.get_colors(path, 10)
                # image = ec.load_image(path)
                # colors = ec.extract_colors(image, 15)
                # ec.plot_colors(colors)
    return render_template('index.html', colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
