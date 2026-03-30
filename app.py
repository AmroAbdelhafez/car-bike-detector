import os
import traceback
from flask import Flask, render_template, request
from ultralytics import YOLO

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Force create the folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load your ONNX model
model = YOLO('model.onnx', task='detect')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            file = request.files.get('image')
            if file and file.filename != '':
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                results = model(filepath)
                
                res_filename = 'result_' + filename
                res_path = os.path.join(app.config['UPLOAD_FOLDER'], res_filename)
                results[0].save(filename=res_path)
                
                return render_template('index.html', original=filename, result=res_filename)
        
        except Exception as e:
            # If ANYTHING fails, print the exact error to the web page!
            error_details = traceback.format_exc()
            return f"<h1>App Crashed! Here is the exact error:</h1><pre>{error_details}</pre>", 500
            
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
