FitPulse Health Anomaly Detection from Fitness Devices
Milestone 1: Data Collection and Preprocessing
Objective
The objective of this milestone is to collect fitness tracker data from wearable devices, preprocess it by handling missing values and normalizing timestamps to UTC, align all metrics to a consistent 1-minute interval, and generate a clean, consolidated dataset ready for analysis and anomaly detection.

Dataset Source
The dataset used in this project is the Fitbit Fitness Tracker Dataset from Kaggle.

Dataset Link: https://www.kaggle.com/datasets/prince7489/fitness-tracker-dataset?resource=download

Files Used
heartrate_seconds_merged.csv (Heart rate data)
minuteStepsNarrow_merged.csv (Steps data)
sleepDay_merged.csv (Sleep logs)
Steps Performed
Created the required project folder structure.
Uploaded fitness data CSV files into the data directory.
Read and validated datasets using Pandas.
Converted all timestamp columns into Pandas datetime format and normalized them to UTC.
Handled missing and null values using simple and appropriate strategies.
Resampled heart rate data to a consistent 1-minute interval.
Aligned steps and sleep data to the same time scale.
Merged heart rate, steps, and sleep data into a single consolidated dataset.
Saved the final cleaned dataset as cleaned_dataset.csv.
Output
The final cleaned and time-aligned dataset is available at: Milestone1/data/cleaned_dataset.csv

Visualization
A Streamlit application was created to visualize the cleaned dataset.

Live Demo
https://huggingface.co/spaces/Prajwalvs/FitPulse

Tools Used :
Python
Pandas
NumPy
Streamlit
Google Colab
GitHub
Hugging Face Spaces
