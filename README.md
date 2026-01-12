# EV Battery Degradation Prediction 🔋⚡

An end-to-end Machine Learning project that predicts **EV battery degradation (%)** based on vehicle usage patterns, charging behavior, and operating conditions.

---

## 📌 Project Overview
Electric Vehicle batteries degrade over time due to multiple factors such as usage intensity, charging cycles, fast charging habits, and temperature.  
This project builds a regression-based ML model to **estimate battery health loss (%)** using realistic EV usage data.

---

## 📊 Features Used
- Vehicle Age (Years)
- Battery Capacity (kWh)
- Daily Usage (km)
- Total Distance Driven (km)
- Charge Cycles
- Fast Charging Percentage (%)
- Average Operating Temperature (°C)

**Target Variable:**  
- Battery Degradation (%)

---

## 🧠 Machine Learning Workflow
1. Data Loading & Cleaning  
2. Exploratory Data Analysis (EDA)
   - Distribution plots
   - Scatter plots
   - Correlation heatmap
   - Boxplots (before & after outlier treatment)
3. Outlier Handling (IQR method)
4. Train–Test Split
5. Model Training & Comparison
   - Linear Regression
   - Decision Tree
   - Random Forest
   - KNN
   - AdaBoost
   - Gradient Boosting
6. Model Evaluation (R², MAE, RMSE)
7. K-Fold Cross Validation
8. Hyperparameter Tuning (GridSearchCV)
9. Final Model Selection
10. Prediction on new EV data
11. Streamlit Web App Deployment

---

## 🏆 Best Model
- **Random Forest Regressor**
- Achieved **R² ≈ 0.98**
- Tuned using GridSearchCV for optimal performance

---

## 🌐 Streamlit Web App
An interactive web app where users can input EV parameters and instantly get predicted battery degradation.

**Features:**
- Background image with dark overlay
- User-friendly sliders & inputs
- Real-time prediction output

Run locally:
```bash
streamlit run APPP.py
