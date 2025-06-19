# 📘 FastAPI Playlist – Clean Notes

## 🔍 What is an API?

- **API (Application Programming Interface)**: A mechanism that allows software components (e.g., frontend & backend) to communicate using:

  - **Protocols** like HTTP
  - **Data formats** like JSON

- **How it works**:
  - The frontend sends a request.
  - The API delivers this request to the backend.
  - The backend processes it and returns a response via the API.
  - The frontend displays the result.

---

## 🍽️ Restaurant Analogy

- **Frontend**: Customer placing an order
- **Backend**: Kitchen preparing food
- **API**: Waiter transferring orders and dishes
- **Menu**: Defines valid operations (endpoints)
- **Dish Presentation**: Represents the data format (e.g., JSON)

---

## 🏗️ Monolithic Architecture vs API Architecture

### 🧱 Monolithic Architecture (Before APIs)

- Frontend and backend are tightly coupled.
- Example: Old IRCTC-like systems had the frontend, backend, and database in a single app.
- Hard to maintain, scale, or expose to third-party apps.

### ❌ Problems

- Insecure to share backend or database directly.
- External integration is nearly impossible.
- Code changes affect the entire system.

---

## 🔧 API-Based Architecture

- Backend and frontend are **decoupled**.
- API layer exposes backend functionality via public **endpoints**.
- External apps interact securely through API URLs (e.g., `/trains?from=A&to=B`).

---

## ✅ Benefits of API Architecture

- Secure and controlled access to backend functionality.
- One backend serves multiple frontends (web, Android, iOS).
- Easier to maintain and scale.
- Uses standard protocols (**HTTP**) and formats (**JSON**).

---

## 🤖 APIs in Machine Learning & AI

- ML/DL apps use trained models instead of databases.
- Backend loads the model and serves predictions via API.
- Example: ChatGPT backend providing predictions through a web API.

### ML API Workflow

1. Frontend sends user query to API.
2. API forwards the request to backend.
3. Backend loads ML model and makes prediction.
4. API sends result back as JSON.

---

## 🔄 Multi-Platform Support with APIs

- One backend can serve:
  - Website
  - Android App
  - iOS App
- Avoids duplicating models or backends.
- Commonly used by companies like Uber, Amazon, Zomato.

---

## 🧠 Key Takeaways

- APIs connect software components using:
  - **HTTP protocols**
  - **JSON data formats**
- Benefits include:
  - Scalable ML deployment
  - Multi-platform support
  - Secure third-party access
