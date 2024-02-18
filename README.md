<h1 align='center'>💥 Cardio Vascular Disease Prediction ML Model 💥</h1>

<h3>:zap: GOAL</h3>

- The aim of the project is to analyze and predict whether the person having the chances of CVD.

### :zap: **DATASET** 

- https://www.kaggle.com/datasets/alphiree/cardiovascular-diseases-risk-prediction-dataset


![Line](https://github.com/Avdhesh-Varshney/WebMasterLog/assets/114330097/4b78510f-a941-45f8-a9d5-80ed0705e847)


<div align='center'>

### :zap: **TECH STACK USED**

<a href="https://jupyter.org/" rel="noreferrer"> <img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" alt="jupyter-notebook" /> </a>
<a href="https://https://numpy.pydata.org/" rel="noreferrer"> <img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white" alt="numpy" /> </a>
<a href="https://pandas.pydata.org/" rel="noreferrer"> <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" /> </a>
<a href="https://matplotlib.org/" rel="noreferrer"> <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="matplotlib" /> </a>
<a href="https://scikit-learn.org/stable/" rel="noreferrer"> <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" /> </a>
<a href="https://flask.palletsprojects.com/en/3.0.x/" rel="noreferrer"> <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" alt="flask" /> </a>
<a href="https://www.w3schools.com/html/" rel="noreferrer"> <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="html5" /> </a>
<a href="https://www.w3schools.com/css/" rel="noreferrer"> <img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" alt="css3" /> </a>
<a href="https://www.w3schools.com/js/" rel="noreferrer"> <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="js" /> </a>
<a href="https://console.cloud.google.com/welcome?project=superb-tendril-373416" rel="noreferrer"> <img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white" alt="google-cloud" /> </a>

</div>

### :zap: **DESCRIPTION**

To analyze the dataset of the Cardio Vascular Disease Risk Prediction Dataset and build and train the model on the basis of different features and variables.

There are 19 features and 308854 entries in this dataset.

- **`General_Health`** - Would you say that in general your health is?
- **`Checkup`** - About how long has it been since you last visited a doctor for a routine checkup?
- **`Exercise`** - During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?
- **`Heart_Disease`** - Respondents that reported having coronary heart disease or mycardialinfarction
- **`Skin_Cancer`** - Respondents that reported having skin cancer
- **`Other_Cancer`** - Respondents that reported having any other types of cancer
- **`Depression`** - Respondents that reported having a depressive disorder (including depression, major depression, dysthymia, or minor depression)
- **`Diabetes`** - Respondents that reported having a diabetes. If yes, what type of diabetes it is/was.
- **`Arthritis`** - Respondents that reported having an Arthritis
- **`Sex`** - Respondent's Gender


![Line](https://github.com/Avdhesh-Varshney/WebMasterLog/assets/114330097/4b78510f-a941-45f8-a9d5-80ed0705e847)



### :zap: **LIBRARIES NEEDED**

1. Pandas
2. Numpy
3. Matplotlib
4. Sklearn
5. Sci-py
6. Seaborn
7. Joblib
8. Flask


### :zap: **HOW TO USE IT**

* Create a virtual environment using `python -m venv myenv`.
* To activate the virtual environment use `.\myenv\Scripts\activate`.
* If error occurs, use `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.
* Now, app.py is the flask app code. run the command `pip install -r requirements.txt` to install the required dependencies for the flask app.
* You may need to install additional libraries for running the jupyter notebooks.


### :zap: **WHAT I HAVE DONE**

* Load the dataset which contains 308854 entries in it and having 19 features in it.
* Performing EDA on the dataset to get insights of the dataset.
* Plotting different features graphs correspond to `target` feature and performing **univariate** and **bivariate** analysis.
* Analyse the dataset by using correlation and plot the bar plot i.e., how much it is related to `target` feature.
* Reduce the parameters and split the dataset into input and target features.
* Split the parameters into training and testing sets.
* Train the different models and get their accuracies and MSE & R2 scores even after tuning the hyper-parameters.
* Even build a neural network and tune the parameters of their, but Neural network gives 91.91% accuracy.
* Dump the model into `.joblib` extension file and create a front-end for it.
* Also creating a `requirements.txt` file for the model and website build-up.
* Create a front-end using **FLASK** framework and create a user-friendly template.
* Website can takes input and pass to the backend of the model and model will predict and provide the user a best result as of accuracy is around ***91.91%***.



### :zap: **Visualization and EDA of different attributes**

<table align='center'>
  <tr align='center'>
    <td align='center'>Alcohol Consumption</td>
    <td align='center'>
      <img alt="graph" src="/static/images/Alcohol_Consumption_distribution.png" >
    </td>
    <td align='center'>
      <img alt="graph" src="/static/images/Alcohol_Consumption_bivariant_distribution.png" >
    </td>
  </tr>

  <tr align='center'>
    <td align='center'>Body Mass Index</td>
    <td align='center'>
      <img alt="heatmap" src="/static/images/BMI_distribution.png" >
    </td>
    <td align='center'>
      <img alt="graph" src="/static/images/BMI_bivariant_distribution.png" >
    </td>
  </tr>

  <tr align='center'>
    <td align='center'>Fried Patato Consumption</td>
    <td align='center'>
      <img alt="graph" src="/static/images/FriedPotato_Consumption_distribution.png" >
    </td>
    <td align='center'>
      <img alt="graph" src="/static/images/FriedPotato_Consumption_bivariant_distribution.png" >
    </td>
  </tr>

  <tr align='center'>
    <td align='center'>Fruit Consumption</td>
    <td align='center'>
      <img alt="graph" src="/static/images/Fruit_Consumption_distribution.png" >
    </td>
    <td align='center'>
      <img alt="graph" src="/static/images/Fruit_Consumption_bivariant_distribution.png" >
    </td>
  </tr>

  <tr align='center'>
    <td align='center'>Correlation</td>
    <td align='center'>
      <img alt="graph" src="/static/images/target_correlation.png" >
    </td>
    <td align='center'>
      <img alt="graph" src="/static/images/correlation_heatmap.png" >
    </td>
  </tr>
</table>


### :zap: **CONCLUSION**

- Neural Network model show promising performance with **91.91%** accuracy of the model.
- Created a user-friendly front-end framework using **FLASK** and integrate it to the model.

#### :zap: **Outputs**

<table align='center'>
  <tr align='center'>
    <td align='center'>
      <img alt='Fraud' src='/static/images/characteristic_curve.png' >
    </td>
  </tr>
</table>


![Line](https://github.com/Avdhesh-Varshney/WebMasterLog/assets/114330097/4b78510f-a941-45f8-a9d5-80ed0705e847)

<div align="center">

### :zap: **PROJECT CREATOR & ADMIN**

  <table>
  <tr>
    <td align="center">
      <a href="https://github.com/Avdhesh-Varshney">
        <img src="https://github.com/Avdhesh-Varshney/CPMasterLog/assets/114330097/0b13fac7-e59d-40be-ac14-b76a28174e85" width=185px height=175px />
      </a></br> 
      <h4 style="color:red;"><a href="https://github.com/Avdhesh-Varshney">Avdhesh Varshney</a></h4>
      <a href="https://www.linkedin.com/in/avdhesh-varshney-5314a4233/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
      </a>
  </tr>
  </table>
</div>


![Line](https://github.com/Avdhesh-Varshney/WebMasterLog/assets/114330097/4b78510f-a941-45f8-a9d5-80ed0705e847)

<div align="center">
  <h3>Show some &nbsp;❤️&nbsp; by &nbsp;🌟&nbsp; this repository!</h3>
  <img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="60"> <em><b>I love connecting with different people</b> so if you want to say <b>hi, I'll be happy to meet you more!</b> :)</em>
</div>

<a href="#top"><img src="https://img.shields.io/badge/-Back%20to%20Top-red?style=for-the-badge" align="right"/></a>

