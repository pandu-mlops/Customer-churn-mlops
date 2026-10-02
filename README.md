# Customer Churn Prediction — MLOps Project

## 📌 Project Overview

This project demonstrates an end-to-end MLOps workflow for predicting customer churn.

The project includes:

* Data preprocessing
* Machine learning model training
* Model evaluation
* Flask REST API
* Docker containerization
* Git and GitHub
* Automated testing with pytest
* GitHub Actions CI/CD
* AWS ECR for Docker image storage
* AWS EC2 for deployment

## 🏗️ Project Architecture

```text
Customer Data
      ↓
Data Preprocessing
      ↓
ML Model Training
      ↓
Model Evaluation
      ↓
Model Artifact (churn_model.pkl)
      ↓
Flask REST API
      ↓
Docker Image
      ↓
GitHub
      ↓
GitHub Actions
      ↓
Run Tests
      ↓
Build Docker Image
      ↓
Push Image to AWS ECR
      ↓
Deploy to AWS EC2
      ↓
Flask API
```

## 📁 Project Structure

```text
customer-churn-mlops/
│
├── data/
│   └── churn.csv
│
├── src/
│   ├── check_data.py
│   └── train.py
│
├── tests/
│   └── test_app.py
│
├── model/
│   └── churn_model.pkl
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── README.md
│
└── .github/
    └── workflows/
        └── ci.yml
```

## 📊 Dataset

The project uses a Telco Customer Churn dataset.

The dataset contains customer information such as:

* Gender
* Senior citizen status
* Partner
* Dependents
* Tenure
* Internet service
* Contract
* Monthly charges
* Total charges
* Churn

The target variable is:

```text
Churn
```

where:

```text
No  → 0
Yes → 1
```

## 🤖 Machine Learning Model

A Logistic Regression model is used for binary classification.

The training pipeline performs:

1. Loading the dataset
2. Converting `TotalCharges` to numeric
3. Handling missing values
4. Removing `customerID`
5. Encoding categorical variables
6. Splitting data into training and testing sets
7. Training Logistic Regression
8. Evaluating the model
9. Saving the trained model

The trained model is saved as:

```text
model/churn_model.pkl
```

## 🔌 Flask API

The trained model is served using Flask.

Start the application locally:

```bash
python app.py
```

The API runs on:

```text
http://127.0.0.1:5000
```

### Health Check

Open:

```text
http://127.0.0.1:5000
```

Expected response:

```text
Customer Churn Prediction API is running!
```

### Prediction API

Endpoint:

```text
POST /predict
```

Example request:

```json
{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 85.0,
    "TotalCharges": 1020.0
}
```

Example response:

```json
{
    "churn": "Yes",
    "probability": 0.70
}
```

## 🐳 Docker

Build the Docker image:

```bash
docker build -t customer-churn .
```

Run the container:

```bash
docker run -p 5000:5000 customer-churn
```

The API can then be accessed at:

```text
http://localhost:5000
```

## 🧪 Testing

The project uses pytest for automated testing.

Run tests locally:

```bash
pytest
```

GitHub Actions automatically runs the tests whenever code is pushed to the `main` branch.

## ⚙️ GitHub Actions CI/CD

The GitHub Actions workflow performs the following steps:

```text
Checkout code
      ↓
Install Python
      ↓
Install dependencies
      ↓
Run pytest
      ↓
Build Docker image
      ↓
Authenticate with AWS
      ↓
Login to Amazon ECR
      ↓
Push Docker image to ECR
```

The workflow file is:

```text
.github/workflows/ci.yml
```

## ☁️ AWS ECR

Amazon Elastic Container Registry (ECR) is used to store the Docker image.

The Docker image is pushed to:

```text
AWS ECR
    ↓
customer-churn
```

Docker images are tagged using the Git commit SHA so that each version can be identified.

Example:

```text
customer-churn:ed95523f5e86d6d857e719cb051825f2f6d7dae6
```

## 🖥️ AWS EC2

The Docker container is deployed to an Amazon EC2 instance running Amazon Linux 2023.

The deployment architecture is:

```text
AWS ECR
   ↓
Docker pull
   ↓
EC2
   ↓
Docker container
   ↓
Flask API
```

The Flask application runs on port:

```text
5000
```

Docker maps:

```text
EC2 port 5000
       ↓
Docker port 5000
       ↓
Flask port 5000
```

## 🔐 Security

AWS credentials and private SSH keys should never be stored in the GitHub repository.

Sensitive information is stored using GitHub Actions Secrets.

Examples:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
ECR_REGISTRY
EC2_HOST
EC2_SSH_PRIVATE_KEY
```

The `.gitignore` file prevents the Python virtual environment and Python cache files from being committed.

## 🚀 MLOps Workflow

The overall workflow is:

```text
Developer
    ↓
Git commit
    ↓
Git push
    ↓
GitHub
    ↓
GitHub Actions
    ↓
Automated Tests
    ↓
Docker Build
    ↓
AWS ECR
    ↓
AWS EC2
    ↓
Docker Container
    ↓
Flask API
```

## 🎯 Future Improvements

Possible future improvements include:

* Automated EC2 deployment
* Model versioning
* Experiment tracking
* Data versioning
* Model monitoring
* API authentication
* HTTPS
* CI/CD rollback
* CloudWatch monitoring
* Infrastructure as Code
* Automated model retraining

## 👨‍💻 Technologies Used

| Technology     | Purpose                |
| -------------- | ---------------------- |
| Python         | Programming language   |
| Pandas         | Data processing        |
| NumPy          | Numerical operations   |
| Scikit-learn   | Machine learning       |
| Joblib         | Model serialization    |
| Flask          | REST API               |
| Pytest         | Automated testing      |
| Docker         | Containerization       |
| Git            | Version control        |
| GitHub         | Source code hosting    |
| GitHub Actions | CI/CD                  |
| AWS ECR        | Docker image registry  |
| AWS EC2        | Application deployment |

## 📌 Project Goal

The goal of this project is to demonstrate how a machine learning model can be developed, tested, containerized, stored in a container registry, and deployed to a cloud server using an automated MLOps workflow.
