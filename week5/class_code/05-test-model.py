import pickle
from flask import Flask, request, jsonify

app = Flask("churn")

MODEL_PATH = 'churn-model.bin'

with open(MODEL_PATH, 'rb') as model_file:
    dv, model = pickle.load(model_file)

@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    churn = y_pred >= 0.5

    result = {
        "churn_probability": float(y_pred),
        "churn": bool(churn)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
   