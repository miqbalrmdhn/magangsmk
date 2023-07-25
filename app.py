from flask import Flask, request, jsonify, render_template
import pickle
import numpy as  np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    height = float(request.form["heightInput"])
    weight = float(request.form["weightInput"])
    gender = float(request.form["genderInput"])
    bmi = weight / (height/100)**2

    # Bentuk array fitur untuk prediksi
    features = np.array([[gender, height, weight, bmi]])

# Extremely Weak
# 1 - Weak
# 2 - Normal
# 3 - Overweight
# 4 - Obesity
# 5 - Extreme Obesity

    # Lakukan prediksi menggunakan model
    prediction = model.predict(features)
    if(prediction == 1):
        return render_template("index.html", prediction_text = "Sangat Kurus")
    elif(prediction == 2):
        return render_template("index.html", prediction_text = "Normal")
    elif(prediction == 3):
        return render_template("index.html", prediction_text = "Kelebihan Berat Badan")
    elif(prediction == 4):
        return render_template("index.html", prediction_text = "Obesitas")
    elif(prediction == 5):
        return render_template("index.html", prediction_text = "Sangat Obesitas")

if __name__ == "__main__":
    app.run(debug=True)