from flask import Flask, render_template, request, jsonify
import pickle

model = pickle.load(open('rand_forrest.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

app = Flask(__name__)

def convert_yn_to_int(value):
    return 1 if value == "yes" else 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods = ["POST"])
def makeArray():
    data = [
        encoder.fit_transform([request.form.get("gen")])[0], 
        float(request.form.get("age")), 
        convert_yn_to_int(request.form.get("hypertension")), 
        convert_yn_to_int(request.form.get("heart_disease")), 
        encoder.fit_transform([request.form.get('ever_married')])[0], 
        encoder.fit_transform([request.form.get("work_type")])[0],
        encoder.fit_transform([request.form.get("Residence_type")])[0], 
        float(request.form.get("glucose")), 
        float(request.form.get("bmi")), 
        encoder.fit_transform([request.form.get("smoke")])[0]
    ]

    results = model.predict([data])

    print(results)

    return render_template('result.html', value=str(results[0]))
