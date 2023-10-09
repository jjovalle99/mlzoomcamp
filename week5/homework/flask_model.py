import pickle
from flask import Flask, request, jsonify

MODEL_PATH = "model1.bin"
DV_PATH = "dv.bin"

with open(DV_PATH, "rb") as dv_file, open(MODEL_PATH, "rb") as model_file:
    dv = pickle.load(dv_file)
    model = pickle.load(model_file)

app = Flask("credit")

@app.route("/predict", methods=["POST"])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    proba = model.predict_proba(X)[0, 1]
    prediction = model.predict(X)[0]

    result = {
        "prediction": bool(prediction),
        "probability": float(round(proba, 3))
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)