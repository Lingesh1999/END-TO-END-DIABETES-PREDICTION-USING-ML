## End-To-End Diabetes Prediction Using ML:


### Table of Content
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Learning Objective](#Learning-Objective)
  * [Technical Aspect](#technical-aspect)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Run](#run)
  * [License](#license)


### Overview 
In this project, the objective is to predict whether the person has Diabetes or not based on various features suach as 
- Pregnancies
- Insulin Level
- Age
- BMI.
The data set that has used in this project has taken from the [kaggle](https://www.kaggle.com/) . "This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage." and used a simple [random forest classifier](https://en.wikipedia.org/wiki/Random_forest).   


### Motivation
The motivation was to experiment  with end to end machine learning project and get some idea about deployment platform like [Heroku](https://g.co/kgs/yvsR77) and offcourse this "
Diabetes is an increasingly growing health issue due to our inactive lifestyle. If it is detected in time then through proper medical treatment, adverse effects can be prevented. To help in early detection, technology can be used very reliably and efficiently. Using machine learning we have built a predictive model that can predict whether the patient is diabetes positive or not.".
This is also sort of fun to work on a project like this which could be beneficial for the society. 

### Learning Objective
The Main objective of this project is to experiment all 
this process mentioned below:

- Descriptive Analysis 
- Data Visualizations 
- Data Preprocessing 
- Data Modelling 
- Model Evaluation 
- Model Deployment 

### Technical Aspect 

- Training a machine learning model using scikit-learn. 
- Building and hosting a  web app using plotly dash 
and to deploy it on Heroku. 
- A user has to put details like Number of Pregnancies, Insulin Level, Age, BMI etc . 
- Once it get all the fields information , the prediction is displayed below the page. 

### Technologies Used  
![Heroku]("E:\Machine learning projects\project2\END-TO-END-DIABETES-PREDICTION-USING-ML\Resources\heroku logo.png")
![scikit-learn]("E:\Machine learning projects\project2\END-TO-END-DIABETES-PREDICTION-USING-ML\Resources\OIP.jpg")
![pandas]("E:\Machine learning projects\project2\END-TO-END-DIABETES-PREDICTION-USING-ML\Resources\pandas logo.png")
![plotly]("E:\Machine learning projects\project2\END-TO-END-DIABETES-PREDICTION-USING-ML\Resources\plotly.png")
![python-jupyter_notebook-numpy]("E:\Machine learning projects\project2\END-TO-END-DIABETES-PREDICTION-USING-ML\Resources\70-701501_jupyter-python-and-numpy-logos-python-jupyter-logo.png")

### Installation 
- Clone this repository and unzip it.
- Begin a new virtual environment with Python 3 and activate it.
- Install the required packages using pip install -r requirements.txt
- Execute the command: python app.py
- Note : This is not built using flask.It is built using
plotly dash which has backened of flask.
- Note2 : The dataset used for the project is inside the 
resources folder or can be found on kaggle.