# Store-Sales-Forecast-ML

[![Unit Tests](https://github.com/Alpha-Mintamir/Store-Sales-Forecast-ML/actions/workflows/unittests.yml/badge.svg)](https://github.com/Alpha-Mintamir/Store-Sales-Forecast-ML/actions/workflows/unittests.yml)

This repository contains a machine learning project for predicting Rossmann store sales. The project utilizes various data science techniques, including data preprocessing, feature engineering, and time series modeling, to forecast future sales based on historical data.


## Project Overview

This project focuses on predicting daily sales for Rossmann stores using historical sales data. The model is designed to help store managers understand future sales trends and make informed business decisions.

### Key Features

- **Data Preprocessing:** Handling missing data, feature scaling, and feature engineering.
- **Time Series Forecasting:** Utilizing advanced time series models to predict future sales.
- **Exploratory Data Analysis (EDA):** Understanding trends, seasonality, and sales patterns.
- **Modeling and Evaluation:** Multiple models (e.g., XGBoost, LightGBM) are trained and evaluated to find the best-performing one.

## Installation

To set up the project environment, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Alpha-Mintamir/Store-Sales-Forecast-ML.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Store-Sales-Forecast-ML
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1. **Data Exploration:**
   The notebooks in the `notebooks/` directory provide step-by-step data exploration, visualization, and feature engineering.

2. **Model Training:**
   Use the scripts in the `src/` and `scripts/` directories to preprocess the data and train the machine learning models.

3. **Unit Testing:**
   Run the unit tests to ensure code quality:
   ```bash
   pytest tests/


### Explanation:
- The **badge** at the top shows the status of unit tests using GitHub Actions.
- The **Project Overview** provides a brief description of the project.
- The **Installation** section details how to set up the project on a local machine.
- The **How to Use** section explains what the different parts of the project do and how to run unit tests.
- The **Folder Structure** section explains each directory's role.


## Folder Structure

Store-Sales-Forecast-ML/
│
├── .vscode/
│   └── settings.json
│
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── src/
│
├── notebooks/
│   ├── __init__.py
│   └── README.md
│
├── tests/
│   ├── __init__.py
│
├── scripts/
│   ├── __init__.py
│   └── README.md
│
├── .gitignore
│
├── requirements.txt
│
└── README.md



