from flask import Flask, request, jsonify,render_template
import util

app = Flask(__name__)
@app.route('/')
def home():
    return  render_template('index.html') 
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        locations = util.get_location_names()
        response = jsonify({'locations': locations})
    except Exception as e:
        response = jsonify({'error': str(e)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form.get('total_sqft',0))
        location = request.form.get('location','')
        bhk = int(request.form.get('bhk',0))
        bath = int(request.form.get('bath',0))

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        response = jsonify({'estimated_price': estimated_price})
    except Exception as e:
        response=jsonify({'error':str(e)})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
