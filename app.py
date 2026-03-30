from flask import Flask, render_template, request, url_for
from ultralytics import YOLO
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load your ONNX model
model = YOLO('model.onnx', task='detect')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            results = model(filepath)
            
            res_filename = 'result_' + filename
            res_path = os.path.join(app.config['UPLOAD_FOLDER'], res_filename)
            results[0].save(filename=res_path)
            
            return render_template('index.html', original=filename, result=res_filename)
            
    return render_template('index.html')

if __name__ == '__main__':
    # Opening doors to Docker and explicitly using 5001
    app.run(host='0.0.0.0', port=5001, debug=True)
