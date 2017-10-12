import os

from flask import Flask, render_template, request, jsonify
from IPython import embed
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    UPLOAD_FOLDER=os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
))

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload',methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify(
            {
                'message': 'No file is not uploaded'
            }
        )
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(
            {
                'message': 'Upload successful.',
                'location': app.config['UPLOAD_FOLDER'] + filename
            }
        )
    else:
        return jsonify(
            {
                'message': 'Uploaded file is not a valid image.'
            }
        )

if __name__ == "__main__":
    app.run(port=5000)

