# Semantic Sensor Data Imputation Testbed

This repository contains the full implementation and datasets used for the thesis exploring whether semantic clustering can improve the quality of missing data imputation in multivariate sensor datasets. The code is included for the datasets for which both the testbed and the imputation task was performed.
All data resulting from the testbed can be found in the following Google Drive folder, including sensor data CSV and semantic data TTL.

## Data Folder:

https://drive.google.com/drive/folders/1_42NOmAj7VQmZnmme0VEVyPvD4QLG9Jr

##  Repository Structure

Each of the following directories contains all necessary files for preprocessing, semantic clustering, and imputation:

- `LeakDB/` – Imputation project for the LeakDB water distribution dataset
- `L-Town/` – Imputation project for the L-Town water network benchmark
- `Metr-LA/` – Imputation project for the Metr-LA traffic dataset
- `LBNL_FDD_Dataset_FCU/` – Imputation project for the LBNL HVAC system dataset

Each project folder includes:
- Raw or intermediate sensor data
- Semantic information files
- Notebooks for construction of the CSV and TTL data
- Notebooks for clustering, imputation, and evaluation
- Evaluation metrics for various missingness scenarios
