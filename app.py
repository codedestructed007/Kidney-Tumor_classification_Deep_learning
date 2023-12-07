from src.cnnClassifier import logger
import os
from flask import Flask, redirect, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from src.cnnClassifier.pipeline.prediction import PredictionPipeline
from src.cnnClassifier.utils.common import decodeImage


class ClientApp:
    def __init__(self):
        self.filename = 'inputImage.jpg'
        self.classifier = PredictionPipeline(self.filename)


app = Flask(__name__)
CORS(app)




@app.route('/')
def home():
    return render_template('home.html')



@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        
        image = request.json['image']
        logger.info('Image has been analysing')
    
        decodeImage(image, clt_app.filename)
        logger.info('Image decoded')
        result = clt_app.classifier.predict()
        return result


if __name__ == '__main__':
    
    clt_app = ClientApp()
    app.run('0.0.0.0',port=8000,debug=True)
