import os
from deneme import center
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from uuid import uuid4

app = Flask(__name__)


UPLOAD_FOLDER = 'static/upload/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	
		flash('Image successfully uploaded and displayed')
		x,y= center(file)
		urn = uuid4()
		return render_template('upload.html', filename=filename, x=x,y=y,urn=urn)
	else:
		flash('Allowed image types are -> png, jpg, jpeg')
		return redirect(request.url)
	

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)



if __name__ == "__main__":
    app.run(debug=True)
