# IoT-Smoke-Detection-Project-MTH2526-G45
PROJECT FOR MTH2526-G45 NESNELERİN İNTERNETİ VE VERİ BİLİMİ
# 🔥 IoT Fire Alarm Detection System

## Project Overview
This project is an end-to-end IoT Data Science solution designed to detect fire hazards in smart home environments. By analyzing real-time data from IoT sensors (Temperature, Humidity, TVOC, eCO2), the system predicts whether a fire alarm should be triggered using a Machine Learning model.

The solution is deployed as a web application on **AWS EC2** using **Streamlit**.

## Problem Statement
I want to **classify fire alarm status** for **indoor smart home environments**, because it impacts **resident safety and minimizes fire-related property damage**. I use data from **IoT sensors (Smoke Detection Dataset)**. Success looks like **achieving >95% accuracy in detecting fire events**.

## Technologies Used
* **Language:** Python 3.x
* **Cloud:** AWS EC2 (Free Tier) - Ubuntu
* **Web Framework:** Streamlit
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn

## Repository Structure
* `data/`: Contains the raw and processed datasets.
* `notebooks/`: Jupyter notebooks for EDA (Exploratory Data Analysis) and Model Training.
* `src/`: Source scripts for data processing.
* `dashboards/`: The Streamlit application code (`app.py`).
* `models/`: Saved Machine Learning models (`.pkl`).
* `docs/`: Project report and presentation materials.

## How to Run Locally
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/halilberkayakkaya07/IoT-Smoke-Detection-Project-MTH2526-G45.git](https://github.com/halilberkayakkaya07/IoT-Smoke-Detection-Project-MTH2526-G45.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```bash
    streamlit run dashboards/app.py
    ```

## Live Demo (AWS)
The project is deployed on AWS EC2.
* **URL:** http://51.20.253.135:8501
*(Note: The instance might be stopped to preserve AWS Free Tier credits. Please contact for a live demo.)*

## Team AKKAYA
* **Course:** Internet of Things and Applied Data Science (Fall 2025)
* **Instructor:** Dr. Mehmet Ali Akyol
