from flask import Flask, request, jsonify
import util
# import waitress


app = Flask(__name__)
# @app.route('/hello')
# def hello():
#     return 'Hi'

# if __name__ == "__main__":
# #     print("Starting Python Flask Server For Home Price Prediction...")
# #     util.load_saved_artifacts()
#       app.run()




@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    ##total_sqft = int(request.form.get('total_sqft'))
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True,use_reloader=False)
# # if __name__ == "__main__":
# #     from waitress import serve
# #     serve(app, host="0.0.0.0", port=8080)