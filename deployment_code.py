# importing essential libraries required for the model:
import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#loading the dataset stored in the Resources folder:
df = pd.read_csv(r"Resources\diabetes.csv")

# first change BMI 's values where it is 0
# only change the values for people who gave birth
# others can be real time models so mostly they have low BMI'S
# so giving them 10.
df["BMI"] = df["BMI"].mask((df["BMI"] == 0) & (df["Pregnancies"] > 0),
            df["BMI"].median())

df["BMI"] = df["BMI"].mask((df["BMI"] == 0), 10)

#Now replacing the other features 0 with NaN:

col = ["Insulin","Glucose","BloodPressure","SkinThickness"]

def replace_0(col):
    for i in col:
        df[i] = df[i].replace(0, np.NaN)

replace_0(col = col)

for i in col:
    df.loc[(df["Outcome"]==0) & (df[i].isnull()),i] = df[df["Outcome"]==0][i].median()
    df.loc[(df["Outcome"]==1) & (df[i].isnull()),i] = df[df["Outcome"]==1][i].median()

# dataset has less than 1000 records removing outliers will 
# affect prediction so replacing the outliers with the 
# upper and lower limit:
def outlier_threshold(dataframe, variable):

    q1 = dataframe[variable].quantile(0.10)
    q3 = dataframe[variable].quantile(0.90)
    inter_quantile_range = q3 - q1
    upper_limit = q3 + (1.5 * inter_quantile_range)
    lower_limit = q1 - (1.5 * inter_quantile_range)
    return upper_limit, lower_limit

#to check outliers present or not:
def outliers_present_or_not(dataframe, variable):

    upper_limit, lower_limit = outlier_threshold(dataframe, variable)
    if dataframe[(dataframe[variable] < lower_limit) | (dataframe[variable] > upper_limit)].any(axis = None):
        #to check print the statement below else use pass
        #print(variable, " yes.")
        pass


for i in df.columns[:-1]:
    outliers_present_or_not(df, i)


#replacing the outliers with the upper and lower limit.There are multiple ways
# to handle outliers i prefer replacing it with limits here:

def replacing_outliers(dataframe, columns):
    for variable in columns:
        upper_limit, lower_limit = outlier_threshold(dataframe, variable)
        dataframe.loc[(dataframe[variable] > upper_limit), variable] = upper_limit
        dataframe.loc[(dataframe[variable] < lower_limit), variable] = lower_limit


replacing_outliers(df, df.columns[:-1])

#Model-Building:
x = df.drop("Outcome", axis = 1)
y = df["Outcome"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state = 120)

# using train test split instead of cross validation
# is because of the prediction to be given to the user
# input , incase of cross val we get score only.

# Using RandomForestClassifier because it gives overall good results:
model = RandomForestClassifier(n_estimators=200)
model.fit(x_train,y_train)

#save the file in the pickle format and use them for the app:
file = "prediction.pkl"
pickle.dump(model, open(file, "wb"))