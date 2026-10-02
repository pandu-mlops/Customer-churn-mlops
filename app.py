from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("model/churn_model.pkl")


@app.route("/")
def home():
    return "Customer Churn Prediction API is running!"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    # Convert input data into a DataFrame
    input_data = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get probability
    probability = model.predict_proba(input_data)[0][1]

    # Convert prediction to Yes/No
    churn = "Yes" if prediction == 1 else "No"

    return jsonify({
        "churn": churn,
        "probability": round(float(probability), 4)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)