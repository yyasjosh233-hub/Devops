from flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to the Flask Web Application!"

# Example API route
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello from Flask API",
        "status": "success"
    })

# Run the server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)