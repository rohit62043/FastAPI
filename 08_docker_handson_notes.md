# 🐳 Introduction to Docker – Detailed Notes

## 📺 Overview
**Speaker:** Nitish  
**Platform:** YouTube

The session introduces Docker as a **universal tool** across software roles including **development, web development, data science, ML engineering, and DevOps**. Docker is positioned as a **high-demand skill** for jobs and interviews. The video covers Docker from **beginner to intermediate** level, divided into theory and practical segments.

---

## 🧪 Hands-On Projects (Detailed)

### ✅ Project 1: Flask Application Dockerization
This project demonstrates how to dockerize a simple Flask web application that prints the multiplication table of a number.

#### 🔥 Step 1: Create `requirements.txt`
List the project dependencies:
```txt
Flask==2.0.3
```

#### 📝 Step 2: Write `Dockerfile`
```dockerfile
# Use Python 3.9 base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
```

#### 🏗 Step 3: Build Docker Image
Run the following command in your project directory (where Dockerfile exists):
```bash
docker build -t flask-multiplier-app .
```

#### 🚀 Step 4: Run Container with Port Mapping
Map container’s port `5000` to host’s port `8080`:
```bash
docker run -p 8080:5000 flask-multiplier-app
```

Access the app in browser at [http://localhost:8080](http://localhost:8080)

---

### ✅ Project 2: ML Project – Laptop Price Predictor
This project demonstrates dockerizing a Streamlit-based ML application and sharing it via Docker Hub.

#### 📥 Step 1: Clone the Repository
```bash
git clone https://github.com/username/laptop-price-predictor.git
cd laptop-price-predictor
```

#### 📝 Step 2: Create `Dockerfile`
```dockerfile
# Use Python 3.8 base image
FROM python:3.8

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]
```

#### 🏗 Step 3: Build Docker Image
```bash
docker build -t username/laptop-price-predictor:latest .
```

#### ☁️ Step 4: Push Image to Docker Hub
Login to Docker Hub:
```bash
docker login
```
Push the image:
```bash
docker push username/laptop-price-predictor:latest
```

#### 📥 Step 5: Pull and Run Image on Another Machine
On a different machine, pull the image:
```bash
docker pull username/laptop-price-predictor:latest
```
Run the container with port mapping:
```bash
docker run -p 8501:8501 username/laptop-price-predictor:latest
```
Open [http://localhost:8501](http://localhost:8501) to access the app.

---

## 🚀 Docker Use-Cases

### 1️⃣ Microservices Architecture
- Containerize each service independently.

### 2️⃣ CI/CD Pipelines
- Consistent environments for automation.

### 3️⃣ Cloud Migration
- Seamless portability between cloud providers.

### 4️⃣ Scalable Web Applications
- Spin up/down containers based on load.

### 5️⃣ Machine Learning & AI
- Deploy models in consistent environments.

### 6️⃣ API Development
- Simplify deployment and scaling.

---

## 🛠 Tools & Setup
- **Docker Desktop:** Local Docker Engine GUI
- **Docker Hub:** Online registry for images

### 🔗 Verification Steps
1. Install Docker Desktop
2. Log into Docker Hub
3. Pull & Run `hello-world`

---

## 📝 Summary
Docker provides:
- **Consistency**
- **Portability**
- **Isolation**
- **Scalability**

With Docker, applications run the same everywhere, streamlining development and deployment workflows.

---

## 🔗 References
- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)

