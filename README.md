# Credit-Card-Lead-Prediction-Model
Hello all 😊, 

This is one of my personal projects in my Data Science journey and the data source:- https://www.kaggle.com/sajidhussain3/jobathon-may-2021-credit-card-lead-prediction?select=train.csv and conducted this as a job a thon by Analytics Vidhya during May 2021.- https://datahack.analyticsvidhya.com/contest/job-a-thon-2/#MySubmissions

I build a classification model to predict whether a particular bank customer is a lead for offering him/her a credit card or no, using Gradient Boosting algorithm. Achieved training accuracy as 0.8211431685409529 and validation accuracy as 0.8117780959070984.

After building the model, first I deployed it in my local system using flask framework and then deployed in Heroku ( a PaaS ) using gunicorn (a python Web Server Gateway Interface (WSGI) HTTP server).

`Brief Description`:

<ins>Problem Statement:</ins> 

Happy Customer Bank is a mid-sized private bank that deals in all kinds of banking products, like Savings accounts, Current accounts, investment products, credit products, among other offerings.

The bank also cross-sells products to its existing customers and to do so they use different kinds of communication like tele-calling, e-mails, recommendations on net banking, mobile banking, etc. 

In this case, the Happy Customer Bank wants to cross sell its credit cards to its existing customers. The bank has identified a set of customers that are eligible for taking these credit cards.

Now, the bank is looking for your help in identifying customers that could show higher intent towards a recommended credit card, given:

- Customer details (gender, age, region etc.)
- Details of his/her relationship with the bank (Channel_Code,Vintage, 'Avg_Asset_Value etc.) 

Solution steps I followed:

1. 
