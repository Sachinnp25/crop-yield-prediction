# 🌾 Crop Yield Prediction & Recommendation System

## 📌 Overview

This project leverages **Machine Learning** to empower farmers and agricultural experts with data-driven insights, helping them make informed decisions to optimize crop production.

The system provides four core functionalities:

* 🌱 **Smart Crop Recommendation**: Suggests the ideal crop based on soil composition and weather conditions.
* 📈 **Crop Yield Prediction**: Estimates crop output tailored to specific regions, seasons, and cultivated area.
* 📊 **Interactive Analytics Dashboard**: Visualizes agricultural production metrics across Indian states and crops.
* 📥 **Downloadable Reports**: Exports recommendation summaries and prediction results in CSV format.

---

## 🚀 Live Demo

### 🌐 Web Application

https://sachin-crop-yield-prediction.streamlit.app

### 💻 GitHub Repository

https://github.com/Sachinnp25/crop-yield-prediction

---

## 📂 Project Structure

```plaintext
CROP-YIELD-PROJECT/
│
├── app/
│   ├── app.py
│   ├── train_crop_recommendation.py
│   └── train_yield_model.py
│
├── dataset/
│   ├── crop_data.csv
│   └── Crop_recommendation.csv
│
├── models/
│   ├── crop_recommendation.pkl
│   ├── yield_encoders.pkl
│   └── yield_model.pkl
│
├── README.md
└── requirements.txt
```

---

## ✨ Features

### 🌱 Crop Recommendation

Recommends the most suitable crop based on:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH Value
* Rainfall

### 📈 Yield Prediction

Predicts crop yield (Ton/Hectare) using:

* State
* District
* Crop
* Season
* Area
* Year

### 📊 Dashboard Analytics

* Top Producing States
* Top Crops by Production
* Crop Distribution Analysis
* Dataset Summary
* Interactive Charts

### 📥 Download Reports

* Crop Recommendation Report
* Yield Prediction Report

---

## 🛠️ Technologies Used

### Frontend & Deployment

* Streamlit

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Joblib

### Visualization

* Plotly Express

### Version Control

* Git
* GitHub

---

## 🤖 Machine Learning Models

### 1. Crop Recommendation Model

**Algorithm:** Random Forest Classifier

**Purpose:** Predict the most suitable crop based on environmental and soil conditions.

**Accuracy:** ~99%

---

### 2. Yield Prediction Model

**Algorithm:** Random Forest Regressor

**Purpose:** Estimate crop yield using agricultural production data.

**R² Score:** 0.8245 (82.45%)

---

## 📊 Datasets Used

### Indian Crop Production Dataset

Contains historical agricultural data including:

* State
* District
* Crop
* Season
* Area
* Production

### Crop Recommendation Dataset

Contains environmental attributes:

* N
* P
* K
* Temperature
* Humidity
* pH
* Rainfall
* Crop Label

---

## 💻 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sachinnp25/crop-yield-prediction.git

cd crop-yield-prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app/app.py
```

### 4️⃣ Open in Browser

```text
http://localhost:8501
```

---

## 📈 Results

### Crop Recommendation

* Accuracy: ~99%
* Fast real-time predictions
* Confidence score included

### Yield Prediction

* R² Score: 0.8245
* Supports state-wise and crop-wise predictions
* Downloadable prediction reports

---

## 🔮 Future Enhancements

* 🌦 Live Weather API Integration
* 🗺 Interactive India Map
* 🤖 AI Chatbot for Farmers
* 🌐 Multi-language Support (Hindi & Regional Languages)
* 📱 Mobile App Version
* 💰 Profit Prediction Module

---

## 👨‍💻 Developer

**Sachin **

BCA (Artificial Intelligence & Machine Learning)

Galgotias University

Machine Learning Major Project – 2026

---

## 📜 License

This project is developed for educational and research purposes.
Feel free to use and modify it with proper attribution.

```
```
