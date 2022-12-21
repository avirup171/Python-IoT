from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def globalRoute():
    return "ALL OK"

@app.route('/telemetrysink', methods = ['POST'])
def telemtrySink():
    params=request.json
    
    return None