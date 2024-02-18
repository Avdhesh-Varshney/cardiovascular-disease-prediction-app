from flask import Flask, render_template, request 
import joblib 
import numpy as np

model = joblib.load('model.joblib')

app = Flask(__name__)

def category(age):
  if 18 <= age < 25:
    return 0
  elif 25 <= age < 30:
    return 1
  elif 30 <= age < 35:
    return 2
  elif 35 <= age < 40:
    return 3
  elif 40 <= age < 45:
    return 4
  elif 45 <= age < 50:
    return 5
  elif 50 <= age < 55:
    return 6
  elif 55 <= age < 60:
    return 7
  elif 60 <= age < 65:
    return 8
  elif 65 <= age < 70:
    return 9
  elif 70 <= age < 75:
    return 10
  elif 75 <= age < 80:
    return 11
  return 12

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

  data = np.array([[general_health, checkup, exercise, skin_cancer, other_cancer, depression, diabetes, arthritis, sex, category(age_category), height, weight, smoking_history, alcohol_consumption, fruit_consumption, green_vegetable_consumption, friedpatato_consumption]])

  pred = model.predict(data)
  res = f"{name}, Chances for CVD is around {round(float(pred[0]) * 100, 2)}%."
  if(pred > 0.5):
    res = f"{name}, Chances for CVD is around {round(float(pred[0]) * 100, 2)}%."
  return render_template('prediction.html', prediction_text=res)

if __name__ == '__main__':
  app.run(debug=True)

