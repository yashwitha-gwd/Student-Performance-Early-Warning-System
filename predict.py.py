import pandas as pd
import pickle

# Load trained model
model = pickle.load(open(r"C:\Users\YASHWITHA\OneDrive\Desktop\Student_Performance_Early_Warningsystem\models\Student_risk_model.pkl","rb"))

# Load training columns
model_columns = pickle.load(open(r"C:\Users\YASHWITHA\OneDrive\Desktop\Student_Performance_Early_Warningsystem\models\model_coulumns.pkl","rb"))

# New student data
student_data = {
    
    "math score":99,
    "reading score":95,
    "writing score":94
}

# Convert to DataFrame
data = pd.DataFrame([student_data])

# Convert categorical values to dummy variables
for col in model_columns:
    if col not in data.columns:
        data[col] = 0
data = data[model_columns]

# Match training columns


# Predict risk
prediction = model.predict(data)

print("Predicted Risk Level:", prediction[0])

risk = prediction[0]
if risk == "High Risk":
    print("Alert: Student needs immediate academic support")
elif risk == "Medium Risk":
    print("Monitor the student performance")
else:
    print("Student performing well")



