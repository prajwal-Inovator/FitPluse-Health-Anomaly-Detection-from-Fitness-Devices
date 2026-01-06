# Milestone 3: Anomaly Detection and Visualization

## Objective
The objective of Milestone 3 is to detect, label, and visualize health-related anomalies from fitness device data. This milestone focuses on identifying abnormal patterns in heart rate and sleep data using residual analysis, domain-based thresholds, and clustering-based outlier detection, followed by clear visualization of detected anomalies.

---

## Steps Followed

### 1. Residual Analysis using Prophet
Time-series forecasting models were built using Facebook Prophet to predict expected values for physiological parameters. Residuals were computed as the difference between actual values and predicted values. Large residual deviations were treated as potential anomalies, indicating unusual health behavior.

### 2. Threshold-Based Anomaly Detection
Domain-specific thresholds were defined based on physiological limits. Data points exceeding upper or lower bounds were flagged as anomalies. This method helped in identifying sudden spikes or drops in heart rate and abnormal sleep durations.

### 3. Cluster-Based Anomaly Detection
Clustering results obtained from Milestone 2 were reused to identify outlier clusters. Data points belonging to sparse or distant clusters were considered anomalous, as they significantly deviated from normal behavioral patterns.

### 4. Anomaly Labeling
Detected anomalies from residual analysis, threshold violations, and cluster-based detection were labeled in the dataset. This labeling ensured a clear distinction between normal and abnormal observations for further analysis and visualization.

### 5. Visualization of Anomalies
Time-series visualizations were created for heart rate and sleep data. Anomalies were highlighted using distinct colors and markers. These visualizations help in clearly identifying abnormal patterns over time and support easier interpretation of detected anomalies.

---

## Tools Used
- Python
- Google Colaboratory
- Facebook Prophet
- Pandas and NumPy
- Matplotlib / Seaborn
- Scikit-learn

---

## Key Insights
- Residual analysis effectively captured sudden deviations from expected health patterns.
- Threshold-based detection helped identify physiologically unsafe values.
- Cluster-based methods successfully highlighted outliers missed by thresholding alone.
- Visual representations made anomaly interpretation intuitive and informative.

---

## Visualizations
- Heart rate time-series with highlighted anomalies
- Sleep pattern visualization showing abnormal segments
