from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open(r"C:\Users\YASHWITHA\OneDrive\Desktop\Student_Performance_Early_Warningsystem\models\Student_risk_model.pkl","rb"))
model_coulumns = pickle.load(open(r"C:\Users\YASHWITHA\OneDrive\Desktop\Student_Performance_Early_Warningsystem\models\model_coulumns.pkl","rb"))

@app.route("/", methods = ["GET", "POST"])
def home():
    prediction = None
    message = None
    math = " "
    reading = " "
    writing = " "
    if request.method == "POST":
        try:
            math = int(request.form.get("math", 0))
            reading = int(request.form.get("reading", 0))
            writing = int(request.form.get("writing", 0))

            data = pd.DataFrame([[math,reading,writing]],columns = ["math score","reading score", "writing score"])
            #data = data.reindex(columns=model_coulumns,fill_value=0)
            data = pd.DataFrame(columns=model_coulumns)
            data.loc[0] = 0

            data.at[0, "math score"] = math
            data.at[0, "reading score"] = reading 
            data.at[0, "writing score"] = writing 
            
            pred = model.predict(data)
            prediction = pred[0]

            #Risk message logic
            if prediction:
                if prediction == "High Risk":
                    message = "Immidiate Academic support required"
                elif prediction == "Medium Risk":
                    message = "Monitor the Student's Progress"
                else:
                    message = "Student Performing Well"
        except Exception as e:
            print(e)
            prediction = "Error"
            message = str(e)
    return render_template("index.html",prediction=prediction, message=message,math=math,reading=reading,writing=writing)
if __name__=="__main__":
    app.run(debug=True)

       
       

       
        
