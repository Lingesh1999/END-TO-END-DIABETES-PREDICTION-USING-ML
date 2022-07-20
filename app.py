import numpy as np
import pickle
import dash
from dash import html
from dash.dependencies import Input,Output,State
import dash_bootstrap_components as dbc
import warnings 
warnings.filterwarnings("ignore")


app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SUPERHERO])

app.layout = html.Div([dbc.Col(
    html.H4("Diabetes Predictor", style = {"color" : "gold"}), width = {"offset" : 4}),
    html.Br(),
    dbc.Row(
    [
        dbc.Label("Pregnancies", html_for="example-email-row", width = 
                                    {"size" : 2, "offset" : 3}),
        dbc.Col(
            dbc.Input(
         type = "number",size = "sm", max=10, min = 0, step = 1,
                id="a0", placeholder="no.of Pregnancies", value = 0
                ), width = {"size" : 4, "offset" : 0})]),
                       
    dbc.Row(
    [
        dbc.Label("Glucose", html_for="example-email-row", width = 
                                    {"size" : 2, "offset" : 3}),
        dbc.Col(
            dbc.Input(
                type="number" ,size = "sm",
                id="a1", placeholder="Enter Glucose Level" , value = 0
                ), width = {"size" : 4, "offset" : 0})]),
                       
    dbc.Row(
    [
        dbc.Label("Insulin", html_for="example-email-row", width = 
                                    {"size" : 2, "offset" : 3}),
        dbc.Col(
            dbc.Input(
                type="number", size = "sm",
                id="a2", placeholder="Enter Insulin Level", value = 0
                ), width = {"size" : 4, "offset" : 0})]),
                       
    dbc.Row(
    [
        dbc.Label("BloodPressure", html_for="example-email-row", width = 
                                    {"size" : 3, "offset" : 2}),
        dbc.Col(
            dbc.Input(
                type="number", size = "sm",
                id="a3", placeholder="Enter BP Level", value=0
                ), width = {"size" : 4, "offset" : 0})]),
    
    dbc.Row(
    [
        dbc.Label("SkinThickness", html_for="example-email-row", width = 
                                    {"size" : 3, "offset" : 2}),
        dbc.Col(
            dbc.Input(
                type="number", size = "sm",
                id="a4", placeholder="Enter SKinThickness", value = 0
                ), width = {"size" : 4, "offset" : 0})]),
    
      dbc.Row(
    [
        dbc.Label("BMI", html_for="example-email-row", width = 
                                    {"size" : 2, "offset" : 3}),
        dbc.Col(
            dbc.Input(
                type="number", size = "sm",min = 10,
                id="a5", placeholder="Enter BMI value", value = 10
                ), width = {"size" : 4, "offset" : 0})]),
                       
      dbc.Row(
    [
        dbc.Label("Diabetes Pedigree Function", html_for="example-email-row", width = 
                                    {"size" : 5, "offset" : 0}),
        dbc.Col(
            dbc.Input(
                type="number", size = "sm",max = 2.47, min = 0.47,
                id="a6", placeholder="Enter in 0.47-2.47 ", value = .47
                ), width = {"size" : 4, "offset" : 0})]),
                       
    dbc.Row(
    [
        dbc.Label("Age", html_for="example-email-row", width = 
                                    {"size" : 2, "offset" : 3}),
        dbc.Col(
            dbc.Input(
                type="number", size = "sm", min=1,
                id="a7", placeholder="Enter Your Age", value = 1
                ), width = {"size" : 4, "offset" : 0})]),
    
    dbc.Col(
        dbc.Button(
                ["Predict", dbc.Badge(color="light", text_color="primary")],
                id = "submit_results",color="primary", n_clicks=0), 
                width={"size" : 3, "offset" : 6}),
    
    html.Br(),
    html.Div(id = "win"),    
])

@app.callback(
    [Output('win', 'children')],
    [Input('submit_results', 'n_clicks')],
    [State('a0', 'value'),
     State('a1', 'value'),
     State('a2', 'value'),
     State('a3', 'value'),
     State('a4', 'value'),
     State('a5', 'value'),
     State('a6','value'),
     State('a7','value')])

def predict_diabetes(n_clicks, a0, a1, a2, a3, a4, a5, a6, a7):

    file = "prediction.pkl"
    classifier = pickle.load(open(file, "rb"))
    user_input = np.array([[a0,a1,a2,a3,a4,a5,a6,a7]])
    pred_model = classifier.predict(user_input)

    if n_clicks > 0: 
        if pred_model < 0.5:
            return [html.Div("You have no diabetes.Remainder : But make sure to check the doctor.")]
        elif pred_model >= 0.5:
            return [html.H6("You have the required symptoms of diabetes.Remainder : Please make sure to check the doctor.")]
        
    else:
        return [html.Div("please enter all the values to check Diabetes.")]
    

if __name__ == "__main__":
    app.run_server(debug = False, port = 8125)