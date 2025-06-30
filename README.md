# Semantic Sensor Data Imputation Testbed

This repository contains the full implementation and datasets used for the thesis exploring whether semantic clustering can improve the quality of missing data imputation in multivariate sensor datasets. The code is included for the datasets for which both the testbed and the imputation task was performed.
All data resulting from the testbed can be found in the following Google Drive folder, including sensor data CSV and semantic data TTL.

## Data Folder:

https://drive.google.com/drive/folders/1_42NOmAj7VQmZnmme0VEVyPvD4QLG9Jr

(all processed data can be found in the folder "Processed_Data" inside each of the datasets.

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

To execute, first download the following files (they can all be found in the Data Folder:
- Files for `LeakDB/`: scenario_data.pkl, knowledge_graph1-LeakDB.ttl, measurements_1_LeakDB.csv
- Files for `L-Town/`: measurements_LTown.csv, 2018_Scada-Demands.csv, 2018_SCADA_Flows.csv, 2018_SCADA_Levels.csv, 2018_SCADA_Pressures.csv
- Files for `Metr-LA/`: metr-la.h5, LA_nodes_coordinates.json, speed_readings.csv
- Files for `LBNL_FDD_Dataset_FCU/`: FCU_FaultFree.csv, measurements_LBNL.csv


