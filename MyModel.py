# Importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.preprocessing import MinMaxScaler, StandardScaler
# from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
# import xgboost as xgb
from sklearn.ensemble import GradientBoostingClassifier
import pickle
# Reading the train data set
df1 = pd.read_csv('train_s3TEQDk.csv')
df2 = df1.drop('ID', axis=1)

#Missing value imputation
df2['Credit_Product'].fillna("Not Known",inplace=True)

# separate minority and majority classes
not_lead = df2[df2.Is_Lead==0]
lead = df2[df2.Is_Lead==1]

# upsample minority
lead_upsampled = resample(lead,
                          replace=True, # sample with replacement
                          n_samples=len(not_lead), # match number in majority class
                          random_state=27) # reproducible results

# combine majority and upsampled minority
upsampled = pd.concat([not_lead, lead_upsampled])

df2 = upsampled

# Let's convert these categorical columns into numerical
label_encoder = LabelEncoder()
#Let's convert these categorical columns into numerical
df2['Gender']=label_encoder.fit_transform(df2['Gender'])
df2['Credit_Product']=label_encoder.fit_transform(df2['Credit_Product'])
df2['Is_Active'] = label_encoder.fit_transform(df2['Is_Active'])
df2['Occupation'] = label_encoder.fit_transform(df2['Occupation'])
df2['Region_Code'] = label_encoder.fit_transform(df2['Region_Code'])
df2['Channel_Code'] = label_encoder.fit_transform(df2['Channel_Code'])


# Dividing the datasets into X (containing predictor variables) and y(target variable)
X = df2.drop('Is_Lead', axis=1)
y = df2['Is_Lead']

# Divide the X,y into train and validation sets respectively

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.3, random_state = 4,shuffle = True)


# Let's do feature scaling for the numerical columns using Standard Scaler
#Scaling all the columns except those which are binary
cols = ['Age', 'Region_Code', 'Occupation', 'Channel_Code', 'Vintage',
       'Credit_Product', 'Avg_Account_Balance']
Scaler = MinMaxScaler()

X_train.loc[:, ['Age', 'Region_Code', 'Occupation', 'Channel_Code', 'Vintage',
       'Credit_Product', 'Avg_Account_Balance']] = Scaler.fit_transform(X_train.loc[:, ['Age', 'Region_Code', 'Occupation', 'Channel_Code', 'Vintage',
       'Credit_Product', 'Avg_Account_Balance']])
# Transforming validation data as well

X_val.loc[:, ['Age', 'Region_Code', 'Occupation', 'Channel_Code', 'Vintage',
       'Credit_Product', 'Avg_Account_Balance']] = Scaler.transform(X_val.loc[:, ['Age', 'Region_Code', 'Occupation', 'Channel_Code', 'Vintage',
       'Credit_Product', 'Avg_Account_Balance']])

# Building model using logistic regression algorithm
#Fitting model
# xgclf = xgb.XGBClassifier()

# model = xgclf.fit(X_train, y_train)
gbm = GradientBoostingClassifier()
model = gbm.fit(X_train, y_train)
# log_reg = LogisticRegression()


# Saving model to disk
pickle.dump(model, open('Naa_model.pkl', 'wb'))

#Function for scaling and predictions
# def predict_cheyi(testinstance):
#     scaler = MinMaxScaler()
#     scaler.fit(X_train)
#     testingData= scaler.transform(testinstance)
#     return model.predict(testingData)