import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
import base64
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)
CORS(app)


MODEL_PATH = os.path.join("model", "inference_model.keras")
model = load_model(MODEL_PATH)

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)

def predict_kidney_disease(image_path):
    # Preprocessing: Must match how you trained the model
    test_image = image.load_img(image_path, target_size=(224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    test_image = test_image / 255.0  # Normalization
    
    #  Inference
    result = model.predict(test_image)
    print(result)
    prediction = np.argmax(result, axis=1)
    print(prediction)
    
    classes = ["Normal",  "Tumor"]
    return classes[prediction[0]]

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        data = request.json['image']
        
        temp_filename = "input_image.jpg"
        decodeImage(data, temp_filename)
        
        result = predict_kidney_disease(temp_filename)
        
        return jsonify({"prediction": result})
    
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)