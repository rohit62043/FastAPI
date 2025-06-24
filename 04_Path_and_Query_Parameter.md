# 📘 FastAPI Detailed Notes – Path & Query Parameters, HTTP Status Codes

## 🔹 Introduction to Path and Query Parameters

FastAPI allows dynamic interaction with endpoints through **path** and **query parameters**, enabling precise control over API behavior and responses.

### What Are Path Parameters?

- Path parameters are dynamic parts of the endpoint URL used to **identify specific resources** (e.g., `/patient/P01`).
- They are essential when accessing or modifying data related to a **specific record**.
- Example use cases: View details of one patient, delete a specific record, update a profile.

```python
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    return {"message": f"Patient ID is {patient_id}"}
```

---

## 🔸 Creating Dynamic Endpoints with Path Parameters

- FastAPI enables creation of endpoints where **only specific data is shown**, such as a particular patient record.
- Path segments (e.g., `/view/3`) are replaced dynamically, enabling **resource-specific actions**.
- These parameters ensure that only the relevant data is retrieved from the database.

```python
@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    data = load_data()  # Assume this loads from JSON
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")
```

---

## 🧪 Enhancing with Metadata and Validation

Using FastAPI’s `Path()` utility, we can:

- Add **descriptions**, **examples**, and **validation** (e.g., regex, length limits).
- Provide clearer documentation for clients.

```python
from fastapi import Path

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str = Path(..., description="Enter the patient ID", example="P01")):
    # Logic here
```

---

## ⚠️ HTTP Status Codes – Meaning & Use

Each API response carries a **status code** indicating the result:

| Code | Meaning                            |
| ---- | ---------------------------------- |
| 200  | OK – Success                       |
| 201  | Created – New resource added       |
| 204  | No Content – Success but no data   |
| 400  | Bad Request – Invalid input        |
| 401  | Unauthorized – Login required      |
| 403  | Forbidden – Access denied          |
| 404  | Not Found – Resource doesn’t exist |
| 500+ | Server-side errors                 |

### Example Use

```python
from fastapi import HTTPException

if patient_id not in data:
    raise HTTPException(status_code=404, detail="Patient not found")
```

---

## 🧰 Error Handling in FastAPI

Use `HTTPException` to raise structured error responses:

```python
raise HTTPException(status_code=404, detail="Patient not found")
```

This avoids returning incorrect success codes (like 200 for failed lookup).

---

## 🔍 Query Parameters – Adding Flexibility

Query parameters add dynamic behavior **without altering the route path**.

### Use Cases

- Sorting: `/sort?sort_by=height&order=descending`
- Filtering: `/patients?city=Delhi`

### Properties

- Optional by nature.
- Passed after `?` in the URL, with multiple values separated by `&`.

```python
from fastapi import Query

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort by height, weight or BMI"),
                  order: str = Query("ascending", description="Sort order: ascending or descending")):
    # Logic here
```

---

## 🧮 Implementing Sorting with Query Parameters

- Two parameters used:
  - `sort_by`: Required; values like height, weight, BMI.
  - `order`: Optional; default is `ascending`.

```python
valid_fields = ["height", "weight", "bmi"]
if sort_by not in valid_fields:
    raise HTTPException(status_code=400, detail="Invalid sort field")

reverse = True if order == "descending" else False
sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=reverse)
return sorted_data
```

---

## ✅ Summary – Key Takeaways

| Feature           | Purpose                                                                  |
| ----------------- | ------------------------------------------------------------------------ |
| Path Parameters   | Required, used to **identify** and access specific resources             |
| Query Parameters  | Optional, used to **extend functionality** like sorting, filtering, etc. |
| HTTP Status Codes | Improve communication by signaling success or failure                    |
| Error Handling    | Structured responses via `HTTPException` for failed requests             |

---

🎓 **Learning Source**: [CampusX FastAPI Playlist](https://www.youtube.com/watch?v=lRArylZCeOs\&list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ\&index=5)

📄 **Notes Repository**: [GitHub - FastAPI Notes](https://github.com/rohit62043/FastAPI/blob/main/03_pydantic_detailed_notes.md)

---

\#️⃣ **Hashtags**:\
\#FastAPI #BackendDevelopment #WebAPI #PythonLearning #CampusX #RESTAPI #PathParameters #QueryParameters #HTTPErrors #APIDesign #SoftwareEngineering

