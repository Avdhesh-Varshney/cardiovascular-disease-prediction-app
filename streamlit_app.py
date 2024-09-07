import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_resource
def load_model():
  model = joblib.load('cvd_model.joblib')
  return model

GH = {'Fair': 1, 'Poor': 3, 'Good': 2, 'Very Good': 4, 'Excellent': 0}
CH = {'Never': 1, 'Within the past year': 4, 'Within the past 2 years': 2, 'Within the past 5 years': 3, '5 or more years ago': 0}
EX = {'No': 0, 'Yes': 1}
SC = {'No': 0, 'Yes': 1}
OC = {'No': 0, 'Yes': 1}
DP = {'No': 0, 'Yes': 1}
DI = {'No': 0, 'No, pre-diabetes or borderline diabetes': 1, 'Yes': 2, 'Yes, but female told only during pregnancy': 3}
AR = {'No': 0, 'Yes': 1}
SEX = {'Female': 0, 'Male': 1}
AGE_CATEGORY = {'18-24': 0, '25-29': 1, '30-34': 2, '35-39': 3, '40-44': 4, '45-49': 5, '50-54': 6, '55-59': 7, '60-64': 8, '65-69': 9, '70-74': 10, '75-79': 11, '80+': 12}
SH = {'No': 0, 'Yes': 1}

def app(model):
  predict = st.container()
  with predict:
    st.subheader('Fill out the Following:')
    name = st.text_input('Enter your name:')

    st.write('**Demographic and Screening Questions**')
    Age_Category = st.selectbox('In what Age category do you belong?', ['Select One'] + list(AGE_CATEGORY.keys()))
    Sex = st.selectbox('Sex',('Select One','Male','Female'))

    Height = st.selectbox('How tall are you?',('Feet and Inches','Centimeters'))
    if Height == 'Feet and Inches':
      Feet = st.selectbox('Feet',('Feet',3,4,5,6,7),label_visibility="collapsed")
      Inches = st.selectbox('Inches',('Inches',0,1,2,3,4,5,6,7,8,9,10,11),label_visibility="collapsed")
      if Feet != 'Feet' and Inches != 'Inches':
        Height_cm = ((Feet * 12) + Inches) * 2.54
    else:
      Height_cm = st.number_input('How tall are you in cm?',min_value=25,max_value=300,step=10)

    Weight_kg = st.number_input('Weight (kg)',min_value=25.00,max_value=300.00,step=10.00)
    Smoking_History = st.radio('Have you smoked at least 100 cigarettes in your entire life?',('No','Yes'),horizontal=True)

    st.write('**Health Status**')
    General_Health = st.selectbox('Would you say that in general, your health is', ['Select One'] + list(GH.keys()))

    st.write('**Health Care Access**')
    Checkup = st.selectbox('About how long has it been since you last visited a doctor for a routine checkup?', ['Select One'] + list(CH.keys()))

    st.write('**Exercise**')
    Exercise = st.radio('During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?', ('Yes','No'),horizontal=True)

    st.write('**Health Conditions**')
    st.write('Has a doctor, nurse, or other health professional ever told you that you had any of the following? For each, tell me Yes or No.')
    Depression = st.radio('(Ever told) (you had) a depressive disorder (including depression, major depression, dysthymia, or minor depression)?', ('No','Yes'),horizontal=True)
    Diabetes = st.radio('(Ever told) (you had) diabetes?', ('No','Yes'),horizontal=True)
    Arthritis = st.radio('(Ever told) (you had) some form of arthritis, rheumatoid arthritis, gout, lupus, or fibromyalgia?', ('No','Yes'),horizontal=True)
    Skin_Cancer = st.radio('(Ever told) (you had) skin cancer?', ('No','Yes'),horizontal=True)
    Other_Cancer = st.radio('(Ever told) (you had) any other types of cancer?', ('No','Yes'),horizontal=True)

    st.write('**Food and Drink Consumption**')
    Alcohol_Consumption = st.slider('During the past 30 days, how many days \
                            did you have at least one drink of any alcoholic beverage such \
                            as beer, wine, a malt beverage or liquor?',
                            0, 30,step=1)

    st.write('Now think about the foods you ate during the past month, that is, the past 30 days, including meals and snacks.')

    fruit = st.selectbox('Not including juices, how often did you eat fruit?',('Select One','Per Day',
                                                                            'Per Week',
                                                                            'Per Month'))

    if fruit == 'Per Day':
      fruit_day = st.selectbox('Day',('How many times do you eat fruit per day?',0,1,2,3,4,5),label_visibility="collapsed")
      if fruit_day != 'How many times do you eat fruit per day?':
        Fruit_Consumption = fruit_day*30
    
    elif fruit == 'Per Week':
      fruit_week = st.selectbox('Day',('How many times do you eat fruit per week?',0,1,2,3,4,5),label_visibility="collapsed")
      if fruit_week != 'How many times do you eat fruit per week?':
        Fruit_Consumption = fruit_week *4
    
    elif fruit == 'Per Month':
      fruit_month = st.selectbox('Day',('How many times do you eat fruit per month?',0,1,2,3,4,5),label_visibility="collapsed")
      if fruit_month != 'How many times do you eat fruit per month?':
        Fruit_Consumption = fruit_month

    green_veg = st.selectbox('How often did you eat a green leafy or lettuce salad, with or without other vegetables?',('Select One','Per Day', 'Per Week', 'Per Month'))

    if green_veg == 'Per Day':
      green_veg_day = st.selectbox('Day',('How many times do you eat Green Vegetables per day?',0,1,2,3,4,5),label_visibility="collapsed")
      if green_veg_day != 'How many times do you eat Green Vegetables per day?':
        Green_Vegetables_Consumption = green_veg_day*30
    
    elif green_veg == 'Per Week':
      green_veg_week = st.selectbox('Day',('How many times do you eat Green Vegetables per week?',0,1,2,3,4,5),label_visibility="collapsed")
      if green_veg_week != 'How many times do you eat Green Vegetables per week?':
        Green_Vegetables_Consumption = green_veg_week *4
    
    elif green_veg == 'Per Month':
      green_veg_month = st.selectbox('Day',('How many times do you eat Green Vegetables per month?',0,1,2,3,4,5),label_visibility="collapsed")
      if green_veg_month != 'How many times do you eat Green Vegetables per month?':
        Green_Vegetables_Consumption = green_veg_month

    fried = st.selectbox('How often did you eat any kind of fried potatoes, including French fries, home fries, or hash browns?',('Select One','Per Day', 'Per Week', 'Per Month'))

    if fried == 'Per Day':
      fried_day = st.selectbox('Day',('How many times do you eat Fried Potatoes per day?',0,1,2,3,4,5),label_visibility="collapsed")
      if fried_day != 'How many times do you eat Fried Potatoes per day?':
        FriedPotato_Consumption = fried_day*30
    
    elif fried == 'Per Week':
      fried_week = st.selectbox('Day',('How many times do you eat Fried Potatoes per week?',0,1,2,3,4,5),label_visibility="collapsed")
      if fried_week != 'How many times do you eat Fried Potatoes week?':
        FriedPotato_Consumption = fried_week *4
    
    elif fried == 'Per Month':
      fried_month = st.selectbox('Day',('How many times do you eat Fried Potatoes per month?',0,1,2,3,4,5),label_visibility="collapsed")
      if fried_month != 'How many times do you eat Fried Potatoes per month?':
        FriedPotato_Consumption = fried_month
    
    submit = st.button('Predict')

  results = st.container()
  with results:
    st.subheader('Results')
    if submit:
      input_values = [General_Health,Checkup,Exercise,Skin_Cancer,
                  Other_Cancer,Depression,Diabetes,Arthritis,
                  Sex,Age_Category,Height_cm,Weight_kg,
                  Smoking_History,Alcohol_Consumption,Fruit_Consumption,
                  Green_Vegetables_Consumption,FriedPotato_Consumption
      ]
      df = pd.DataFrame([input_values])
      df.columns = ['General_Health',
      'Checkup',
      'Exercise',
      'Skin_Cancer',
      'Other_Cancer',
      'Depression',
      'Diabetes',
      'Arthritis',
      'Sex',
      'Age_Category',
      'Height_(cm)',
      'Weight_(kg)',
      'Smoking_History',
      'Alcohol_Consumption',
      'Fruit_Consumption',
      'Green_Vegetables_Consumption',
      'FriedPotato_Consumption']
      st.dataframe(df)

      decoded_values = [GH[General_Health],CH[Checkup],EX[Exercise],SC[Skin_Cancer],
                  OC[Other_Cancer],DP[Depression],DI[Diabetes],AR[Arthritis],
                  SEX[Sex],AGE_CATEGORY[Age_Category],float(Height_cm),float(Weight_kg),
                  SH[Smoking_History],float(Alcohol_Consumption),float(Fruit_Consumption),
                  float(Green_Vegetables_Consumption),float(FriedPotato_Consumption)
      ]
      try:
        data = np.array([decoded_values])
        pred = model.predict(data)

        st.write(f'Hello, {name}!')
        st.write('Based from the Machine Learning model, your risk of developing Cardiovascular Disease (CVD) is:')

        if pred[0] < 0.5:
          risk = 'LOW'
          st.success(f'**{risk}**')
        else:
          risk = 'HIGH'
          st.error(f'**{risk}**')
        
        st.warning('Disclaimer: **The results from this test are not intended to diagnose or treat any disease, or offer personal medical advice.** The model was only trained in 300,000 data and with personal attributes only. Moreover, the analysis of this models states that it is likely to classify certain attributes such as the sex of the person, their general health status, and being diabetic as high importance in determining if the person is at risk or not.')
        
        st.info('Accuracy: The Machine Learning Model used for prediction was first evaluated in an unknown data consisting of 60,000 records, The model correctly classified 79.18 % of people with CVDs and 73.46 % of people that is healthy. However, only 21 % of the predicted by the model out of all predicted that are at risk is correctly classified. The model takes into consideration the cost of misclassifying at risk people as healthy. That is why the model is more likely to classify people at risk.')

        details = st.expander(label='More Details',expanded=False)
        with details:
          st.write('According to the ML model:')
          st.write('The Probability that it will classify you as at risk for CVDs are:')
          st.info(pred[0])
          st.write('The Probability that it will classify you as at no risk for CVDs are:')
          st.info(1-pred[0])
          st.write('Note: If the Probability it will classify you at risk is over 0.5, then the model will classify you as at risk for CVDs')
        
        st.balloons()

      except:
        st.error('Enter valid values to show the results')

def main():
  st.title('CVD Risk Prediction App')
  model = load_model()
  app(model)

if __name__ == '__main__':
  main()
