from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def handle_endpoint():
    # Access query parameters
    param1 = request.args.get('param1', default=None, type=str)
    param2 = request.args.get('param2', default=None, type=str)
    # You can set default values and types for the parameters

    # Use the query parameters in your response or processing
    return jsonify({'param1': param1, 'param2': param2}), 200

if __name__ == '__main__':
    app.run(debug=True)
