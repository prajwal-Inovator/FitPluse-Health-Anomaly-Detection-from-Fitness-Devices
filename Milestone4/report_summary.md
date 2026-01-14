# Milestone 4: Dashboard for Insights  
## FitPulse – Health Anomaly Detection from Fitness Devices

---

## Overview
This milestone focuses on developing an interactive dashboard to visualize and analyze health anomalies detected from fitness device data. The dashboard is built using **Streamlit** and executed in **Google Colaboratory**, enabling users to upload fitness data, trigger anomaly detection dynamically, visualize insights, and download anomaly reports.

---

## Objectives
- Build a Streamlit-based interactive dashboard
- Enable CSV/JSON fitness data upload
- Integrate preprocessing and anomaly detection pipelines from previous milestones
- Visualize health trends and anomalies
- Provide downloadable anomaly summary reports

---

## Dashboard Features

### 1. Streamlit-Based Interactive UI
- Clean and intuitive dashboard layout
- Sidebar controls for user interaction
- Executed successfully within Google Colab environment

### 2. Data Upload & Integration
- Supports fitness data upload in **CSV and JSON** formats
- Automatically processes uploaded data
- Integrates anomaly detection logic from earlier milestones
- Dynamic execution of anomaly detection upon data upload or filter changes

### 3. Filtering Options
- **Date-wise filtering** to analyze specific time ranges
- **Metric-wise filtering** for:
  - Heart Rate
  - Sleep Duration
  - Step Count

---

## Visualization of Insights

### Heart Rate Analysis
- Line chart displaying heart rate trends over time
- Anomaly points highlighted clearly using markers

### Sleep Pattern Analysis
- Visualization of sleep duration
- Identification of abnormal sleep patterns

### Step Count Behavior
- Step count trends over time
- Alerts for unusually high or low activity levels

All visualizations are interactive and update dynamically based on selected filters.

---

## Report Generation
- Automatically generates an **anomaly summary report**
- Report includes:
  - Timestamp of anomaly
  - Metric name
  - Anomalous value
- Users can download the report in **CSV format** directly from the dashboard

---

## Observations
- Anomaly detection model successfully identified unusual patterns across all health metrics
- Heart rate anomalies corresponded to sudden spikes or drops
- Sleep anomalies reflected irregular or insufficient sleep durations
- Step count anomalies highlighted abnormal inactivity or excessive activity
- Filters enabled focused and efficient analysis of specific metrics and time periods

---

## Conclusion
The Streamlit dashboard effectively fulfills all Milestone-4 requirements by providing an end-to-end interactive system for health anomaly detection and visualization. The solution supports proactive health monitoring, is easy to use, and enables exportable insights for further analysis or reporting.

---
