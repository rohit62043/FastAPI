from fastapi import FastAPI,Path,HTTPException,Query
import json


app= FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        data=json.load(file)
    
    return data
@app.get("/")
def hello():
    return {"message": "Patient Management System"}

@app.get("/about")
def about():
    return {"message": "Fully Funtional Patient Managemenr api."}

@app.get("/view")
def view():
    data = load_data()
    return {"patients": data}

@app.get("/view/{patient_id}")  
def view_patient(patient_id: str = Path(..., description="The ID of the patient to view",example="P001")):
    data = load_data()
    if patient_id in data:
            return {"patient": data[patient_id]}
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort patients by 'height' or 'weight'", example="weight"), order:str=Query(...,description="Order of sorting: 'asc' for ascending or 'desc' for descending", example="asc")):
    data=load_data()
    valid_feilds = ['height', 'weight','BMI']
     
    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_feilds)}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Use 'asc' for ascending or 'desc' for descending")
    
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=(order == 'desc'))
    return {"sorted_patients": sorted_data}

