# wine-classifier-api
 REST API wine classification in Python

## What is this folder about?
This project is a REST API developed with FastAPI to expose a wine classification machine learning model, using the Wine dataset from the sklearn library. The model predicts the class of a wine based on its chemical characteristics.

## Features
- *Wine Class Prediction:* The API receives characteristics of a wine through json and returns the predicted class (0, 1 or 2).
- *API Health Check:* A status check endpoint that confirms that the API is working correctly.

## Technologies Used
- *FastAPI:* Framework for creating APIs.
- *Sklearn:* Used to load the dataset and train the model.
- *Pandas:* Data manipulation.
- *RandomForestClassifier:* Classification model.
- *Swagger UI:* Automatically generated interactive interface for testing the API.
- *Joblib:* To save and load the trained model.


## Folder structure
This folder is organized as follows:  

```
wine-classifier-api/
 ┣ app/
 ┣   ┣ __init__.py
 ┣   ┣ main.py                    # API entry point
 ┣   ┣ model.py                   # Model prediction and loading function
 ┣   ┣ wine_model.pkl             # Trained model
 ┣ Notebook:  
 ┣   ┣ wine_model_training.ipynb  # Notebook to train and save the model
 ┣ requirements.txt               # Project dependencies
 ┗ README.md                   # Project documentation
 ```
 
## Installation

1) Install the dependencies:
pip install -r requirements.txt

2) Clone the repository:
git clone https://github.com/seuusuario/wine-classifier-api.git
cd wine-classifier-api

3) Train the model by running the wine_model_training.ipynb notebook

4) Run the API in the terminal:
uvicorn app.main:app --reload --port 8001

5) Access the Swagger UI in the browser to interact with the API:
http://127.0.0.1:8001/docs


# Endpoints

## Health Check:

- GET /api/health
Returns a message confirming that the API is healthy.
Example Response:
{
  "status": "I'm healthy"
}

## Predict

- POST /api/predict
Receives characteristics of the wine and returns the class prediction.
Request body example:
{
  "alcohol": 13.2,
  "malic_acid": 2.77,
  "ash": 2.51,
  "alcalinity_of_ash": 18.5,
  "magnesium": 103,
  "total_phenols": 1.6,
  "flavanoids": 0.63,
  "nonflavanoid_phenols": 0.53,
  "proanthocyanins": 1.8,
  "color_intensity": 3.0,
  "hue": 1.1,
  "od280_od315_of_diluted_wines": 2.87,
  "proline": 1285
}{
  "alcohol": 13.2,
  "malic_acid": 2.77,
  "ash": 2.51,
  "alcalinity_of_ash": 18.5,
  "magnesium": 103,
  "total_phenols": 1.6,
  "flavanoids": 0.63,
  "nonflavanoid_phenols": 0.53,
  "proanthocyanins": 1.8,
  "color_intensity": 3.0,
  "hue": 1.1,
  "od280_od315_of_diluted_wines": 2.87,
  "proline": 1285
}

Example Response:
{
  "prediction": 1
}
