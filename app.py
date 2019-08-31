import pickle
import numpy as np
import json
import pandas as pd
import boto3
from flask import Flask, request, render_template

#Flask application adapted from the following: https://github.com/tanujjain/deploy-ml-model.git
BUCKET = 'rhombuscandidate'

model = None
app = Flask(__name__, template_folder='.')
key = 0

def load_model():
    global model 
    with open('trained_model.pkl', 'rb') as f:
        model = pickle.load(f)
        print(type(model))

def upload_prediction(Prediction, key):
    
    data = str(Prediction)
    s3 = boto3.resource('s3')
    s3.Bucket(BUCKET).put_object(Key="Output/" + "output_" + str(key) + ".txt", Body=data)
    


@app.route('/')
def home_endpoint():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def get_prediction():
    if request.method == 'POST' :
        data = request.json
        key = request.headers.get('file')
        key = key[key.find("Input/")+len("Input/"):key.rfind(".json")]
        print(type(model))
        print(type(data)) #debug
        X = pd.DataFrame(data)
        print(X) #debug
        prediction = model.predict(X)

        print(type(prediction))
        upload_prediction(prediction, key)
    return str(prediction) #returns as scientific notation


if __name__ == '__main__' :
    load_model()
    app.run(host='0.0.0.0', port = 4848)
    print('Listening on port 4848')