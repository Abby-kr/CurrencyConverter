from flask import Flask,jsonify
import requests
import json

app = Flask(__name__)

@app.route('/home',methods = ['GET'])
def home():
    request = requests.get(url)
    json_data = json.loads(request.content)
    print(json_data)



if __name__=='__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    home()