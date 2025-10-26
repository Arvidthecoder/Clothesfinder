from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API is running! Use /find_item with POST method."})

@app.route('/find_item', methods=['POST'])
def find_item():
    data = request.get_json()
    query = data.get("query", "")
    return jsonify({"query": query, "results": [f"Testprodukt för '{query}'"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
