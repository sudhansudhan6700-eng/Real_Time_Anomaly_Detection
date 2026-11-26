# Real-Time Financial Anomaly Detection

## Project Overview
This project detects suspicious financial transactions using Machine Learning anomaly detection algorithms.

It compares Isolation Forest and Local Outlier Factor (LOF), tunes the Isolation Forest threshold, and provides a web interface for testing transactions.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- FastAPI
- Streamlit
- Joblib
- Jupyter Notebook

## Machine Learning Models
1. Isolation Forest
2. Local Outlier Factor (LOF)

The Isolation Forest model was selected and its threshold was tuned to improve anomaly detection performance.

## Tuned Model Performance

| Metric | Score |
|---|---:|
| Precision | 0.7538 |
| Recall | 0.8089 |
| F1 Score | 0.7804 |

Confusion Matrix:

| | Predicted Normal | Predicted Anomaly |
|---|---:|---:|
| Actual Normal | 4870 | 130 |
| Actual Anomaly | 94 | 398 |

## Project Structure
- `anomaly_detection.ipynb` – Model training and evaluation
- `anomaly_model.py` – Model-related Python code
- `main.py` – FastAPI backend
- `frontend.py` – Streamlit frontend
- `app/` – Application files
- `model/` – Saved model files
- `saved_model/` – Model artifacts
- `.gitignore` – Files excluded from Git

## How to Run

### 1. Install dependencies
```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib fastapi uvicorn streamlit requests
```

### 2. Start the API
```bash
python -m uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to access the API documentation.

### 3. Start the frontend
Open another terminal and run:
```bash
python -m streamlit run frontend.py
```

## Features
- Financial transaction anomaly detection
- Isolation Forest model training
- Threshold tuning
- Model evaluation and visualization
- FastAPI prediction endpoint
- Interactive Streamlit interface
- Sample fraud transaction testing

## Author
Sudhan

## Project Purpose
This project demonstrates an end-to-end Machine Learning anomaly detection application using Python, FastAPI, and Streamlit.
