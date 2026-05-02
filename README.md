# Data Engineering & Data Science Internship Project

## Overview

This project demonstrates an end-to-end data engineering and data science workflow, including data preprocessing, machine learning, API deployment, and optimization.

---

##  Tasks Completed

###  Task 1: Data Pipeline

* Built ETL pipeline using Pandas
* Handled missing values and feature engineering
* Processed Netflix dataset

###  Task 2: Machine Learning Model

* Built classification model using Random Forest
* Predicted whether content is Movie or TV Show

###  Task 3: API Deployment

* Developed REST API using FastAPI
* Real-time prediction endpoint

###  Task 4: Optimization

* Solved profit maximization problem using Linear Programming (PuLP)

---

##  Tech Stack

* Python
* Pandas, Scikit-learn
* FastAPI
* PuLP
* Git & GitHub

---

##  How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run pipeline

python task1_pipeline/pipeline.py

### 3. Train model

python task2_model/model.py

### 4. Run API

python -m uvicorn task3_api.app:app --reload

### 5. Run optimization

python task4_optimization/optimization.py

---

## API Example

http://127.0.0.1:8000/predict?duration=100&genre_count=2&release_year=2020

---

##  Outcome

Successfully built an end-to-end data system covering:

* Data Engineering
* Machine Learning
* API Deployment
* Optimization Techniques
