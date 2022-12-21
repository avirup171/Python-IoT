from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/sum', methods=['GET','POST'])
def sumCalculate():
    value_a=request.args.get('value_a')
    value_b=request.args.get('value_b')
    sum=operations.sum(value_a,value_b)
    return str(sum)

@app.route('/queryparams',methods=['GET'])
def paramsDemo():
    name=request.args.get('name')
    return name

@app.route('/postparams', methods=['POST'])
def postParamsDemo():
    params=request.json
    value_a=params["value_a"]
    value_b=params["value_b"]
    sum=operations.sum(value_a,value_b)
    return str(sum)

if __name__=='__main__':
    app.run()