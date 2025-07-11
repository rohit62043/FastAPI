from fastapi import FastAPI,Path,HTTPException,Query
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional


app= FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]
    


def load_data():
    with open("patients.json", "r") as file:
        data=json.load(file)
    
    return data

def save_data(data):
    with open("patients.json", "w") as file:
        json.dump(data, file)
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

@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'patient created successfully'})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)
    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})



