# FastAPI Project Enhancement: Insurance Premium Prediction API

## 🌟 Introduction & Recap
- Recaps previous work: Built an insurance premium classification ML model (Random Forest) served through a FastAPI API with `/predict` endpoint.
- Created a Streamlit frontend for interaction.
- Prediction categories: **High, Medium, Low** based on personal/lifestyle data.
- This video begins step 1 of 3 improvements:
  1. Improve API (current focus)
  2. Dockerize
  3. Deploy on AWS

---

## 📁 Project Structure Improvements
- Original project had ML model, notebooks, and API code all in one cluttered folder.
- Created new dedicated project folder: `insurance_premium_prediction/`
  - Subfolders:
    - `model/` for `model.pkl`
    - `schema/` for Pydantic models
    - `config/` for tier city lists
- Ensures clean separation and easier Dockerization.

---

## 📄 Dependency Management
- Used `pip freeze > requirements.txt` to export dependencies.
- Removed unused libraries (e.g. `streamlit`, `requests`) to reduce image size.
- Created and activated a virtual environment.
- Installed dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

---

## 🚫 Bug Fix: Case Sensitivity in City Input
- Issue: 'mumbai' vs 'Mumbai' misclassified due to tier detection.
- Solution: Added **Pydantic validator** on city field to:
  - Strip whitespace
  - Convert to title case

---

## 📞 Added New Endpoints
- `/` (Home): Human-readable message ("API is live").
- `/health`: Machine-readable status for cloud infra like ELB/Kubernetes.
  - Returns:
    ```json
    {"model_loaded": true, "model_version": "1.0.0"}
    ```

---

## 🏁 Refactoring for Production
### Separation of Concerns
- Split code across multiple files for maintainability:

**File Breakdown:**
- `app.py`:
  - Contains only FastAPI routing and endpoint definitions.
- `schema/user_input.py`:
  - Holds `UserInput` Pydantic model.
- `config/city_tier.py`:
  - Contains Tier-1 and Tier-2 city lists.
- `model/predict.py`:
  - Handles model loading and predictions.
  - Function `predict_output(user_input_dict)` returns prediction.

---

## ⚠️ Error Handling
- Added `try-except` block around prediction:
  - Catches and logs exceptions.
  - Returns JSON with status code `500` and error message.

---

## 🔢 Output Enhancement: Confidence Scores
- Modified prediction output to include:
  - Predicted category
  - Confidence of predicted category
  - Probabilities for all classes

**Example Output:**
```json
{
  "prediction": "High",
  "confidence": 0.82,
  "class_probabilities": {
    "Low": 0.05,
    "Medium": 0.13,
    "High": 0.82
  }
}
```

---

## 📝 Response Model (Output Validation)
- Defined `PredictionResponse` model in `schema/prediction_response.py`
  - Validates API output before sending to client.
  - Fields:
    - `prediction`: `str`
    - `confidence`: `float`
    - `class_probabilities`: `Dict[str, float]`
- Ensures:
  - Clean documentation
  - Valid response structure
  - Auto-error on incorrect return format

---

## ✅ Final Outcome of API Enhancements
- ✔ Structured folder organization
- ✔ Input and output validation
- ✔ Health and root endpoints
- ✔ Computed fields & preprocessing
- ✔ Exception handling
- ✔ Confidence scores for predictions
- ✔ Separation of concerns (clean codebase)

---

## 🚀 Next Step
- Dockerize the improved FastAPI application
- Deploy on AWS cloud

> "Subscribe & Like" reminder from the speaker!

