from flask import Flask, render_template, request 
import joblib 
import numpy as np

model = joblib.load('cvd_model.joblib')
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
  name = request.form.get('name')
  general_health = int(request.form.get('general_health'))
  checkup = int(request.form.get('checkup'))
  exercise = int(request.form.get('exercise'))
  skin_cancer = int(request.form.get('skin_cancer'))
  other_cancer = int(request.form.get('other_cancer'))
  depression = int(request.form.get('depression'))
  diabetes = int(request.form.get('diabetes'))
  arthritis = int(request.form.get('arthritis'))
  sex = int(request.form.get('sex'))
  age_category = int(request.form.get('age_category'))
  height = float(request.form.get('height'))
  weight = float(request.form.get('weight'))
  smoking_history = int(request.form.get('smoking_history'))
  alcohol_consumption = float(request.form.get('alcohol_consumption'))
  fruit_consumption = float(request.form.get('fruit_consumption'))
  green_vegetable_consumption = float(request.form.get('green_vegetables_consumption'))
  friedpatato_consumption = float(request.form.get('fried_potato_consumption'))

  data = np.array([[general_health, checkup, exercise, skin_cancer, other_cancer, depression, diabetes, arthritis, sex, age_category, height, weight, smoking_history, alcohol_consumption, fruit_consumption, green_vegetable_consumption, friedpatato_consumption]])

  pred = model.predict(data)
  res = f"Hello {name}!\n Based from the Machine Learning model, your risk of developing Cardiovascular Disease (CVD) is: {round(float(pred[0]) * 100, 2)}%."
  return render_template('prediction.html', prediction_text=res)

if __name__ == '__main__':
  app.run(debug=True)
