from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    data = {'message': 'Hello, World!'}
    return jsonify(data)

@app.route('/api', methods=['POST'])
def post_data():
    content = request.get_json()
    message = content['message']
    response = {'message': f'You sent: {message}'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
