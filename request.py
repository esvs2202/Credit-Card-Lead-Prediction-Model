import requests

url = 'http://127.0.0.1:5000/predict_lead'

r = requests.post(url,json={'Gender': 'Male', 'Age': 25, 'Region Code': 'RG250', 'Occupation': 'Salaried', 'Channel Code': 'X1',
                            'Vintage period in months': 36, 'Having any Credit Product ?': 'Yes', 'Average Account Balance': 100000,
                            'Is an active customer ?': 'Yes'})

print(r.json())