from flask import Flask,request, url_for, redirect, render_template
import os
import sys
from flask import request
from random import randint
from werkzeug.utils import secure_filename
# from flask.ext.session import Session

app = Flask(__name__)
# sess = Session()

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'log'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def hloworld():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_file', methods=['POST'])
def upload_file():
    
    # check if the post request has the file part
    if 'file' not in request.files:        
        result = {
            'result' : 0,    
            'error' : 'file not available',
        }
        return render_template('result.html', result=result)
    
    file = request.files['file']
    
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':        
        result = {
            'result' : 0,    
            'error' : 'file not available',
        }
        return render_template('result.html', result=result)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        print('filepath : ', filepath)
        
        result = {
            'result' : 1,
            'error' : '0',
            'image_location' : filepath
        }
        return render_template('result.html', result = result, filepath = filepath)
    
    #return content
    return render_template('result.html', user=user)

if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 6021))
    
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    # sess.init_app(app)
    
    app.run(host= host, port = port, use_reloader = False)
    