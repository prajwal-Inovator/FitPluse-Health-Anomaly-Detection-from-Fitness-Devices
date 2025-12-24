# Milestone 2 – Feature Extraction and Modeling
## FitPulse Health Anomaly Detection from Fitness Devices

## Objective
The objective of Milestone 2 is to derive meaningful insights from preprocessed fitness device data by extracting statistical and time-series features, modeling temporal trends, and identifying behavioral patterns. This milestone prepares the dataset for anomaly detection in future stages.

---

## Dataset Description
The dataset consists of fitness device data collected from multiple users, including:
- Heart rate readings
- Step count data
- Sleep duration
- Timestamps and user identifiers

These time-series signals are used to analyze user behavior and detect deviations from normal patterns.

---

## Steps Performed

### 1. Feature Extraction
- Extracted automated time-series features using **TSFresh**.
- Computed statistical features such as mean, standard deviation, skewness, and kurtosis.
- Applied feature selection techniques to retain relevant features.

### 2. Trend Modeling
- Modeled temporal trends and seasonality using **Facebook Prophet**.
- Generated forecasts with confidence intervals for heart rate, steps, and sleep.
- Analyzed deviations from expected trends to highlight unusual behavior.

### 3. Behavioral Pattern Clustering
- Applied **KMeans** and **DBSCAN** for unsupervised clustering.
- Used **PCA** for dimensionality reduction and visualization.
- Identified clusters representing normal and atypical behavioral patterns.

---

## Tools and Libraries Used
- Python
- Google Colaboratory
- TSFresh
- Facebook Prophet
- Scikit-learn
- Pandas, NumPy, Matplotlib, Seaborn

---
