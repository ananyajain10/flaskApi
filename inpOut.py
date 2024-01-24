from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/input', methods = ['POST'])

def get_input():
    data = request.get_json()

    return jsonify(
        {"message": "Input received"}
    )
@app.route('/output', methods = ['GET'])
def get_output():
    output_data = {"result": "Output Data"}
    return jsonify(output_data)

if __name__ == '__main__':
    app.run(debug=True)