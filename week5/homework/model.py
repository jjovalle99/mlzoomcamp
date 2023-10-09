import pickle

MODEL_PATH = "model1.bin"
DV_PATH = "dv.bin"

with open(DV_PATH, "rb") as dv_file, open(MODEL_PATH, "rb") as model_file:
    dv = pickle.load(dv_file)
    model = pickle.load(model_file)

client = {"job": "retired", "duration": 445, "poutcome": "success"}

if __name__ == "__main__":
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    print(f"Credit probability: {y_pred:.3f}")