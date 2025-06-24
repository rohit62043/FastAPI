# 🧠 Pydantic: Comprehensive Notes on Data Validation in Python

## 📌 Introduction to Pydantic and Its Importance

**Pydantic** is a powerful Python library used for data validation and settings management based on Python's type annotations. It is widely integrated in frameworks like **FastAPI** and is essential for creating structured, reliable, and maintainable applications.

### Why Use Pydantic?

- Python’s dynamic typing is beginner-friendly but prone to runtime errors in production.
- Type hints in Python are not enforced at runtime.
- Manual validation logic is tedious and error-prone.
- Pydantic automates both type validation and structure enforcement.

**Common use cases:**

- FastAPI request/response validation
- YAML/JSON configuration file validation
- Input pipelines in machine learning

---

## 🛑 Problems in Python Without Pydantic

### 1. No Runtime Type Enforcement

```python
# Example showing the problem

def insert_patient(name: str, age: int):
    print(f"Inserting {name} with age {age} into the database")

insert_patient("Alice", "30")  # Accepts string instead of int
```

- Type hints are ignored at runtime.
- Incorrect types can be passed silently.

### 2. Manual Validation Is Inefficient

```python
def insert_patient(name, age):
    if not isinstance(name, str) or not isinstance(age, int):
        raise TypeError("Invalid types!")
    print("Valid data inserted.")
```

- Leads to bloated and hard-to-maintain code.

### 3. Complex Data Constraints

```python
if age < 0:
    raise ValueError("Age must be non-negative")
```

- Must manually enforce rules like `age >= 0` or valid email formats.

---

## ⚙️ Pydantic’s Core Workflow

### Step 1: Define a Model

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
```

### Step 2: Instantiate the Model

```python
data = {"name": "Nitish", "age": 30}
patient = Patient(**data)
```

### Step 3: Use the Validated Object

```python
def insert_patient(patient: Patient):
    print(patient.name, patient.age)
```

---

## 🚀 Pydantic V2 Highlights

- Faster performance
- Cleaner syntax and structure
- New features: `computed_field`, `field_validator`, native `Annotated` support

---

## 🎛 Advanced Field Handling

### ✅ Optional Fields

```python
from typing import Optional

class Patient(BaseModel):
    married: Optional[bool] = None
```

### 🧩 Default Values

```python
married: bool = False
```

---

## 🔒 Built-in Custom Types

### 📧 `EmailStr`

```python
from pydantic import EmailStr

class Contact(BaseModel):
    email: EmailStr
```

### 🌐 `AnyUrl`

```python
from pydantic import AnyUrl

class Profile(BaseModel):
    linkedin: AnyUrl
```

---

## 🧱 Field Constraints and Metadata

```python
from typing import Annotated
from pydantic import Field

name: Annotated[str, Field(max_length=50, title="Full Name")]
allergies: Annotated[List[str], Field(max_length=5)]
```

### 🔍 Strict Type Validation

```python
weight: Annotated[float, Field(strict=True)]
```

---

## 🛠 Custom Validators

### 🔧 Field Validators

```python
from pydantic import BaseModel, EmailStr, field_validator

class Patient(BaseModel):
    email: EmailStr

    @field_validator("email")
    def validate_email(cls, value):
        allowed_domains = ["hdfc.com", "icici.com"]
        domain = value.split("@")[1]
        if domain not in allowed_domains:
            raise ValueError("Invalid domain")
        return value
```

### ⚙️ Validator Modes

```python
@field_validator("age", mode="before")
def validate_age(cls, v):
    if isinstance(v, str):
        return int(v)
    return v
```

---

## 🔄 Model Validators (Cross-field Logic)

```python
from pydantic import BaseModel, model_validator

class Patient(BaseModel):
    age: int
    contact: dict

    @model_validator(mode="after")
    def check_emergency_contact(cls, values):
        if values.age > 60 and "emergency" not in values.contact:
            raise ValueError("Senior patients must have emergency contact")
        return values
```

---

## 📐 Computed Fields

```python
from pydantic import BaseModel, computed_field

class Patient(BaseModel):
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
```

---

## 🧩 Nested Models

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):
    name: str
    address: Address

patient = Patient(
    name="Ravi",
    address={"city": "Delhi", "state": "DL", "pincode": 110001}
)
```

---

## 📤 Exporting Model Data

### 🧾 To Dictionary

```python
patient.dict()
```

### 🌐 To JSON

```python
patient.json()
```

### 🔍 Controlling Export Behavior

```python
patient.dict(include={"name"})
patient.dict(exclude={"contact"})
patient.dict(exclude_unset=True)
```

---

## ✅ Summary

Pydantic enhances Python development by:

- Enforcing runtime type and data validation
- Reducing redundant validation logic
- Supporting complex models and constraints
- Facilitating integrations with tools like FastAPI
- Improving code readability, maintainability, and safety

**Ideal for:**

- Backend API development
- Data transformation and ingestion pipelines
- Configuration and schema validation

Pydantic is a must-have library for writing robust, production-grade Python applications.

