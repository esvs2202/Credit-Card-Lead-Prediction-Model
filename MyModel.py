# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingClassifier
import pickle
# import warnings
# warnings.filterwarnings('ignore')
# Reading the train data set
df1 = pd.read_csv('clean_train_data.csv')
#resampling
df1 = df1.sample(frac=1)
# Dividing the datasets into X (containing predictor variables) and y(target variable)
X = df1.drop('Is_Lead', axis=1)
y = df1['Is_Lead']

Scaler = MinMaxScaler()

X.loc[:, ['Age', 'Region_Code', 'Occupation', 'Channel_Code', 'Vintage',
       'Credit_Product', 'Avg_Account_Balance']] = Scaler.fit_transform(X.loc[:, ['Age', 'Region_Code', 'Occupation', 'Channel_Code', 'Vintage',
       'Credit_Product', 'Avg_Account_Balance']])

#Fitting model using Gradient Boosting algorithm
gbm = GradientBoostingClassifier()
model = gbm.fit(X, y)
# Saving model to disk
pickle.dump(model, open('Naa_model.pkl', 'wb'))
