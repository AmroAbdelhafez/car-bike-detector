from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import traceback

app = Flask(__name__)

# Use absolute paths for Docker stability
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the directory exists inside the container
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load your ONNX model (Ensure this is the Opset 12 version!)
model = YOLO('model.onnx', task='detect')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            file = request.files.get('image')
            if file and file.filename != '':
                # Save user upload
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Run Inference
                results = model(filepath)
                
                # Save the result image with boxes
                # FIX: Force the file to end in .jpg so OpenCV never crashes
                res_filename = 'result_image.jpg'
                res_path = os.path.join(app.config['UPLOAD_FOLDER'], res_filename)
                results[0].save(filename=res_path)
                
                return render_template('index.html', original=filename, result=res_filename)
        
        except Exception as e:
            # This will show you exactly WHAT is wrong if it crashes
            error_msg = traceback.format_exc()
            return f"<h1>App Crashed!</h1><pre>{error_msg}</pre>", 500
            
    return render_template('index.html')

if __name__ == '__main__':
    # Important: Catch the port from the environment (Render/Docker default is 10000)
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
