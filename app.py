import os
from flask import Flask, render_template, request
from ultralytics import YOLO

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# SAFETY NET: Force Python to create the uploads folder if it doesn't exist!
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load your ONNX model
model = YOLO('model.onnx', task='detect')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Safely get the file from the form
        file = request.files.get('image')
        
        # Make sure a file was actually uploaded
        if file and file.filename != '':
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Save original image
            file.save(filepath)
            
            # Run YOLO model on the image
            results = model(filepath)
            
            # Save the new image with the bounding boxes
            res_filename = 'result_' + filename
            res_path = os.path.join(app.config['UPLOAD_FOLDER'], res_filename)
            results[0].save(filename=res_path)
            
            return render_template('index.html', original=filename, result=res_filename)
            
    return render_template('index.html')

if __name__ == '__main__':
    # Render assigns a dynamic port, so we catch it here
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
