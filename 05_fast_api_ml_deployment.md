# FastAPI ML Project: From Fundamentals to Full Deployment

## 🎥 Video Series Overview

- Hosted by Nitesh as part of a **FastAPI tutorial playlist**.
- 6 videos cover **FastAPI fundamentals**.
- Built a small project: **Patient Management System** with full CRUD APIs.

---

## ⚙️ Covered Fundamentals

- What are APIs and their real-world use
- Why use **FastAPI**
- HTTP methods: GET, POST, PUT, DELETE
- Path & query parameters, request bodies
- Intro to **Pydantic** for input validation

---

## 🤖 Serving Machine Learning Model via FastAPI

> Data Scientists build models in notebooks, but need to make them accessible to end-users.

### Video Structure (3-Part):
1. Build & export ML model
2. Create FastAPI endpoint to serve predictions
3. Build frontend using Streamlit

---

## 🧠 ML Model: Insurance Premium Prediction

### Objective:
- Predict premium category (**High / Medium / Low**) based on personal & lifestyle data.

### Features:
- Age, Height, Weight, Income, City, Smoker, Occupation

### Feature Engineering:
- BMI = weight / height^2
- Age groups (Young, Adult, Senior)
- Lifestyle Risk (based on BMI + smoker)
- City Tier (1, 2, 3 based on city name)

### Model:
- Trained Random Forest Classifier via scikit-learn pipeline
- Saved model as `model.pkl`

---

## 🔧 FastAPI Backend: `/predict` Endpoint

### Setup:
- Created `app.py`
- Loaded `model.pkl`
- Created Pydantic model `UserInput`
- Used POST method to accept **raw inputs** (age, weight, etc.)

### Computed Fields in Pydantic:
- `bmi`, `lifestyle_risk`, `age_group`, `city_tier`

### Prediction Logic:
- Convert validated user input to DataFrame
- Call `model.predict(df)`
- Return prediction as JSON

### Sample Output:
```json
{"prediction": "Low"}
```

---

## 🧪 Testing the API

- Started FastAPI using `uvicorn`
- Accessed Swagger UI (`/docs`)
- Passed test data to `/predict`
- Validated outputs by changing inputs (e.g. smoker → medium/high risk)

---

## 🌐 Streamlit Frontend

### Purpose:
- UI to collect input → send to API → display result

### Features:
- Number inputs for Age, Height, Weight, Income
- Dropdowns for Smoker & Occupation
- Text input for City
- Button to trigger API call

### Backend Call:
- Used `requests.post()` to send form data to FastAPI `/predict`
- Display prediction from JSON response

---

## 🏁 Project Flow Summary

1. Build ML model in notebook
2. Serve model via FastAPI with validation
3. Add Streamlit frontend to interact with API

---

## 🎯 Conclusion & Next Steps

- Covers full ML API deployment cycle
- Next videos will focus on:
  - Dockerizing FastAPI app
  - Deploying on AWS

> "Like & Subscribe" reminder by the host 🎉

