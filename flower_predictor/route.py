from flower_predictor import app
from flower_predictor.colour import show_colours
from flower_predictor.flower import Flower,search_flowers_by_colour
from flask import render_template,request
import os


ALLOWED_EXTENSIONS = set(['jpg', 'jpeg','png'])

@app.route('/')
def hlo_world():
    return render_template("index.html")


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
        filename = "file.jpg"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename )
        file.save(filepath)

        colours = show_colours(filepath)

        flowers = {}

        for colour in colours:
            f = search_flowers_by_colour(colour)
            flowers[colour] = [{'name':flower.name,'image':flower.image} for flower in f ]

        print('filepath : ', filepath)
        
        result = {
            'result' : 1,
            'error' : '0',
            'image_location' : filepath[17:]
        }
        return render_template('result.html', result = result, colours=colours,flowers=flowers)
    
    #return content
    return render_template('result.html', result = {
            'result' : 0,
            'error' : 'jjjjjj',
            'image_location' : "filepath"
        })

