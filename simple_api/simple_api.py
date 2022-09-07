from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

app = Flask(__name__)

info =  { 'battery_status':0  }


@app.route('/api/info', methods=['GET'])
def get_products():
    return jsonify({'info': info})

@app.route('/api/info', methods=['POST'])
def post_product():
    #check if request has required attributes and is json data.
    if not request.json:
        abort(400)
    battery_status = request.json.get('battery_status', "") #this is not required. if not available get blank string
    #create new product
    info['battery_status'] = battery_status
    return jsonify({'info': info})

@app.route('/')
def index():
  return 'You have reached the default route. Congratulations!'
  

@app.route('/hello')
def say_hello():
  return 'Hello World!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')