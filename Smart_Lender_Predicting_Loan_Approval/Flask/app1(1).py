import numpy as np
import pickle
import pandas
import os
from flask import Flask, request, render_template


app = Flask(__name__)
model = pickle.load(open('C:/Users/Tanmay Anand/OneDrive/Desktop/Smart_Lender_Predicting_Loan_Approval/Smart_Lender_Predicting_Loan_Approval/Flask/best_rf_model.pkl', 'rb'))
scale = pickle.load(open('C:/Users/Tanmay Anand/OneDrive/Desktop/Smart_Lender_Predicting_Loan_Approval/Smart_Lender_Predicting_Loan_Approval/Flask/scale1.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=["POST","GET"]) 
def predict() :
    return render_template("input.html")

@app.route('/submit',methods=["POST","GET"])
def submit():
    input_feature=[int(x) for x in request.form.values() ]  
    input_feature=[np.array(input_feature)]
    print(input_feature)
    names = ['Dependents', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Gender_Male', 'Married_Yes',
       'Education_Not Graduate', 'Self_Employed_Yes',
       'Property_Area_Semiurban', 'Property_Area_Urban']
    data = pandas.DataFrame(input_feature,columns=names)
    print(data)

    prediction=model.predict(data)
    print(prediction)
    prediction = int(prediction)
    print(type(prediction))
   
    if (prediction == 0):
       return render_template("output.html",result ="Loan wiil Not be Approved")
    else:
       return render_template("output.html",result = "Loan will be Approved")
if __name__=="__main__":
    
    port=int(os.environ.get('PORT',5000))
    app.run(debug=False)