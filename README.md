# Credit-Card-Lead-Prediction-Model
Hello all 😊, 

This is one of my personal projects in my Data Science journey and the data source:- https://www.kaggle.com/sajidhussain3/jobathon-may-2021-credit-card-lead-prediction?select=train.csv and conducted this as a job a thon by Analytics Vidhya during May 2021.- https://datahack.analyticsvidhya.com/contest/job-a-thon-2/#MySubmissions

I build a classification model to predict whether a particular bank customer is a lead for offering him/her a credit card or no, using Gradient Boosting Classifier algorithm. Achieved training accuracy as 0.8050 and validation accuracy as 0.8036.

After building the model, first I deployed it in my local system using flask framework and then deployed in Heroku ( a PaaS ) using gunicorn (a python Web Server Gateway Interface (WSGI) HTTP server).

`Brief Description`:

<ins>Problem Statement:</ins> 

Happy Customer Bank is a mid-sized private bank that deals in all kinds of banking products, like Savings accounts, Current accounts, investment products, credit products, among other offerings.

The bank also cross-sells products to its existing customers and to do so they use different kinds of communication like tele-calling, e-mails, recommendations on net banking, mobile banking, etc. 

In this case, the Happy Customer Bank wants to cross sell its credit cards to its existing customers. The bank has identified a set of customers that are eligible for taking these credit cards.

Now, the bank is looking for your help in identifying customers that could show higher intent towards a recommended credit card, given:

- Customer details (gender, age, region etc.)
- Details of his/her relationship with the bank (Channel_Code,Vintage, 'Avg_Asset_Value etc.) 

<ins>Solution steps I followed:</ins>

1. Loaded the data set in Jupyter note book and did data cleaning as follows:
    a) Imputed missing values in "Credit_Product" with "Not Known", which indicates that there's no information w.r.t. a customer having any credit product or no.
    b) Ignored "ID" column as it is not useful for our analysis.
    c) Visualized our target column "Is_Lead" and found that there was a class imbalance. To resolve this issue, I used "resample" module from sklean.utils and performed                  resampling operation thus making our data unbiased.
    d) Next, I converted all the 6 categorical columns to numerical columns using "LabelEncoder" module from sklearn.preprocessing.
    e) Then, 70% of data set is split into training set while the remaining 30% into testing set.
    f) Next, except the columns having binary values, scaled all the other columns using a "MinMaxScaler" from sklearn.preprocessing, making our data ready for model building.

2. Experimented with various Machine learning algorithms (all with default parameters) :
   a) Logistic regression - training accuracy: 0.7107 & validation accuracy: 0.7103
   b) Random Forest Classifier - training accuracy: 0.7810 & validation accuracy: 0.7785
   c) AdaBoost Classifier - training accuracy: 0.7967 & validation accuracy: 0.7954
   d) Gradient Boosting Classifier - training accuracy: 0.8050 & validation accuracy: 0.8036
   e) XGBoost Classifier - training accuracy: 0.8211 & validation accuracy: 0.8117.
   
   From all the above 5 algorithms, I chose Gradient boosting classifier algorithm for building the application because the XGBoost classifer caused a trouble in my PyCharm        resulting in hanging 😂, otherwise it is a best one to go. 

3. Next, I created a flask application and integrated my front-end html file and the model file which was stored in my local disk using pickel module.

4. Then deployed in Heroku and ran using gunicorn module. 


