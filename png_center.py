import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from deneme import center
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

from uuid import uuid4

UPLOAD_FOLDER = 'static/upload/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
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
		return render_template('upload.html', filename="a"+filename, x=x,y=y)
	else:
		flash('Allowed image types are -> png, jpg, jpeg')
		return redirect(request.url)
	

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)



if __name__ == "__main__":
    app.run(debug=True)


    #print(liste[109264:])  # 109264 - 109268 eleman aralığını görmek için 


    # cv2.imshow("deneme", img)
    # cv2.waitKey()
