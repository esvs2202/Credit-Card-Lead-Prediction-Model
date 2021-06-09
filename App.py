import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from flask import Flask, request, jsonify, render_template
import pickle
from MyModel import *

app = Flask(__name__)
model = pickle.load(open('Naa_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # features = [float(x) for x in request.form.values()]
    # # int_features = [x for x in request.form.values()]
    # final_features = [np.array(features)]
    features = [x for x in request.form.values()]

    final_features = []
    d1 = {'X1': 0, 'X2': 1, 'X3': 2, 'X4': 3}
    d2 = {'RG250': 0, 'RG251': 1, 'RG252': 2, 'RG253': 3, 'RG254': 4, 'RG255': 5, 'RG256': 6,
          'RG257': 7, 'RG258': 8, 'RG259': 9, 'RG260': 10, 'RG261': 11, 'RG262': 12,
          'RG263': 13, 'RG264': 14, 'RG265': 15, 'RG266': 16, 'RG267': 17, 'RG268': 18,
          'RG269': 19, 'RG270': 20, 'RG271': 21, 'RG272': 22, 'RG273': 23, 'RG274': 24,
          'RG275': 25, 'RG276': 26, 'RG277': 27, 'RG278': 28, 'RG279': 29,
          'RG280': 30, 'RG281': 31, 'RG282': 32, 'RG283': 33, 'RG284': 34}

    for i in features:
        if i == 'Male':
            final_features.append(1)
        elif i == 'Female':
            final_features.append(0)
        elif 'RG' in i:
            final_features.append(d2.get(i))
        elif i == 'Salaried':
            final_features.append(2)
        elif i == 'Self-Employed':
            final_features.append(3)
        elif i == 'Entrepreneur':
            final_features.append(0)
        elif i == 'Other':
            final_features.append(1)
        elif 'X' in i:
            final_features.append(d1.get(i))
        elif i == 'Yes':
            final_features.append(2)
        elif i == 'No':
            final_features.append(0)
        elif i == "Not Known":
            final_features.append(1)
        elif i == 'True':
            final_features.append(1)
        elif i == 'False':
            final_features.append(0)
        else:
            final_features.append(i)

    final_features = np.array(final_features).reshape(-1, 9)
    df3 = pd.DataFrame(final_features)
    df3.iloc[:, 1:8] = Scaler.transform(df3.iloc[:, 1:8])
    arr = np.array(df3).reshape(-1, 9)
    prediction = model.predict(arr)

    output = prediction[0]
    if output == 0:
        return render_template('index.html', prediction_text="This Customer is not a Lead")
    elif output == 1:

        return render_template('index.html', prediction_text="This Customer is a Lead")


if __name__ == "__main__":
    app.run(debug=True)
