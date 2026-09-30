# Heart Disease Analysis

Exploratory Data Analysis (EDA) of the UCI Heart Disease dataset using Python.

## 1. Project Overview

This project analyzes the **Heart Disease dataset** from the UCI Machine Learning Repository.

The analysis focuses on understanding the structure, quality, distribution, relationships, and statistical patterns present in the dataset.

The project covers:

- Dataset description
- Data types and variables
- Data quality assessment
- Descriptive statistics
- Univariate analysis
- Bivariate analysis
- Grouping and aggregation
- Correlation analysis
- Data visualization
- Key findings

> **Note:** This project is intended for educational and exploratory data analysis purposes. The results should not be interpreted as medical diagnosis or medical advice.

---

## 2. Dataset

### Source

**UCI Machine Learning Repository – Heart Disease**

https://archive.ics.uci.edu/dataset/45/heart+disease

### Dataset Information

| Property           | Details                         |
| ------------------ | ------------------------------- |
| Dataset Name       | Heart Disease                   |
| Repository         | UCI Machine Learning Repository |
| Dataset ID         | 45                              |
| Number of Records  | 303                             |
| Number of Features | 13                              |
| Target Variable    | target                          |
| Data Type          | Multivariate                    |
| Domain             | Health and Medicine             |

The dataset contains information related to patients and several clinical characteristics.

The original target variable is:

- `0` = No heart disease
- `1–4` = Presence of heart disease

For this project, the target is converted into a binary variable:

- `0` = No Heart Disease
- `1` = Heart Disease

---

## 3. Variables

| Variable | Description                          |
| -------- | ------------------------------------ |
| age      | Age of the patient                   |
| sex      | Sex of the patient                   |
| cp       | Chest pain type                      |
| trestbps | Resting blood pressure               |
| chol     | Serum cholesterol                    |
| fbs      | Fasting blood sugar > 120 mg/dl      |
| restecg  | Resting electrocardiographic result  |
| thalach  | Maximum heart rate achieved          |
| exang    | Exercise-induced angina              |
| oldpeak  | ST depression induced by exercise    |
| slope    | Slope of peak exercise ST segment    |
| ca       | Number of major vessels              |
| thal     | Thalassemia result                   |
| target   | Presence or absence of heart disease |

---

## 4. Project Objectives

The main objectives of this project are:

1. Understand the structure of the Heart Disease dataset.
2. Assess the quality and completeness of the data.
3. Calculate descriptive statistics.
4. Perform univariate analysis.
5. Perform bivariate analysis.
6. Perform grouping and aggregation.
7. Analyze correlations between variables.
8. Create meaningful visualizations.
9. Identify important patterns in the dataset.
10. Summarize the findings from the analysis.

---

## 5. Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- ucimlrepo

### Development Environment

The project can be executed using:

- Python
- VS Code
- PyCharm
- Jupyter
- Terminal / Command Prompt

---

## 6. Project Structure

```text
heart-disease-analysis/
│
├── data/
│   └── README.md
│
├── output/
│   ├── tables/
│   └── visualizations/
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_quality.py
│   ├── descriptive_analysis.py
│   ├── univariate_analysis.py
│   ├── bivariate_analysis.py
│   ├── grouping_analysis.py
│   ├── correlation_analysis.py
│   ├── visualizations.py
│   └── findings.py
│
├── index.py
├── requirements.txt
└── README.md
```
