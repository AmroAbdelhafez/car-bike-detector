from flask import Flask, render_template, request
from ultralytics import YOLO
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load your ONNX model
model = YOLO('model.onnx', task='detect')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Save user upload
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            
            # Run Inference
            results = model(filepath)
            
            # Save the result image with boxes
            res_filename = 'result_' + file.filename
            res_path = os.path.join(UPLOAD_FOLDER, res_filename)
            results[0].save(filename=res_path)
            
            return render_template('index.html', original=file.filename, result=res_filename)
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
