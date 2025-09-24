# fraud-detection-project
---

## Project Description

This project aims to **analyze banking transactions data to detect fraudulent activities (Fraud Detection)**.
The workflow starts with collecting raw data (CSV & JSON), uploading it into **SQL Server**, performing **data cleaning and analysis (EDA)** in **Python**, and visualizing key insights with **Power BI**.
Additionally, a **Machine Learning model** was built on the final dataset to experiment with fraud prediction.

---

## 📂 Project Structure

* **📁 Data Collection**

  * Dataset downloaded from [Kaggle](https://www.kaggle.com/) using `kagglehub`.
  * Data consists of:

    * 3 CSV files
    * 2 JSON files

* **🗄️ Database (SQL Server)**

  * Raw data uploaded into **SQL Server**.
  * Merged all files into one table: `merged_dataset`.
  * Script: [📄 merge\_sql\_server\_data.py](merge_sql_server_data.py)

* **📊 Exploratory Data Analysis (EDA)**

  * Data cleaning and transformation.
  * Exploratory analysis on transaction types, fraud distribution, and correlations.
  * Script: [📄 eda\_part.py](eda_part.py)
  * Final dataset after EDA: [`final data(1).csv`](final%20data%20%281%29.csv)

* **📈 Visualization (Power BI)**

  * Interactive dashboard highlighting:

    * Fraud vs. legitimate transactions
    * Key influencing factors
    * Distribution of operations by type and location
  * File: [📊 FRAUD PROJECT.pbix](FRAUD%20PROJECT.pbix)

* **📑 Presentation (PowerPoint)**

  * Summary of findings, insights, and recommendations.
  * File: [📄 Fraud Detection Analysis.pptx](Fraud%20Detection%20Analysis.pptx)

* **🤖 Machine Learning (Optional)**

  * Applied ML models on the final dataset.
  * Notebook: [📓 ML\_on\_final\_data\_(additional).ipynb](ML_on_final_data_%28additional%29.ipynb)

---

## ⚙️ Technologies & Tools

* **Programming**: Python (Pandas, Matplotlib, Seaborn, Scikit-learn)
* **Database**: SQL Server
* **Visualization**: Power BI
* **Presentation**: PowerPoint
* **Dataset**: Kaggle

---

## 🚀 How to Run

1. **Download dataset from Kaggle**:

   ```python
   import kagglehub
   path = kagglehub.dataset_download("computingvictor/transactions-fraud-datasets")
   print("Path to dataset files:", path)
   ```

2. **Upload to SQL Server**:

   * Create a new database.
   * Import CSV & JSON files.
   * Run [merge\_sql\_server\_data.py](merge_sql_server_data.py).

3. **Run EDA**:

   ```bash
   python eda_part.py
   ```

4. **Open Power BI Dashboard**:

   * File: [`FRAUD PROJECT.pbix`](FRAUD%20PROJECT.pbix).

5. **Run Machine Learning (Optional)**:

   * Open [ML\_on\_final\_data\_(additional).ipynb](ML_on_final_data_%28additional%29.ipynb) in Jupyter Notebook.

---

## 📌 Results

* Identified key indicators of fraudulent transactions.
* Built an interactive dashboard for fraud monitoring.
* Generated recommendations for better fraud detection.
* Implemented a preliminary ML model for classification.

---


