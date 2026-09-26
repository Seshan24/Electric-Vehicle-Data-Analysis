## Electric Vehicle Data Analysis

### 📌 Project Overview

This project analyzes an Electric Vehicle (EV) dataset using Python. The analysis covers data cleaning, preprocessing, exploratory data analysis (EDA), hypothesis testing, and machine learning models to predict EV driving range.

### 🎯 Objectives
```
* Clean and prepare the EV dataset
* Handle missing values
* Encode categorical variables
* Apply feature scaling where required
* Select and transform relevant features
* Perform Exploratory Data Analysis (EDA)
* Conduct statistical hypothesis testing
* Build and evaluate machine learning models
* Predict EV range using vehicle specifications
```
### 📊 Dataset
```
Dataset: electric_vehicles_spec_2025.csv
```
* Total records: 478
* Training records: 382
* Testing records: 96
* Target variable: range_km

### 🛠️ Technologies Used
```
* Python
* Pandas
* NumPy
* SciPy
* Scikit-learn
* Matplotlib
```
### 🔄 Data Preprocessing

The following preprocessing techniques were applied:
```
* Missing value handling using median and most-frequent imputation
* Categorical variable encoding using One-Hot Encoding
* Feature scaling using StandardScaler
* Feature selection
* Conversion of cargo volume into a numerical feature
* 80/20 train-test split
```
### 📈 Exploratory Data Analysis

The project includes four visualizations:
```
1. Battery Capacity vs EV Range
2. EV Range by Drivetrain
3. Average Range by Brand
4. Distribution of EV Range
```
### Exploratory data analysis Finding

Battery capacity showed a strong positive relationship with EV range, with a Pearson correlation of r = 0.8804.

### 🧪 Hypothesis Testing

#### 1. Pearson Correlation Test
```
H₀: There is no linear correlation between battery capacity and EV range.

H₁: There is a linear correlation between battery capacity and EV range.
```
* Pearson correlation: r = 0.8804
* p-value: 2.31 × 10⁻¹⁵⁶
* Significance level: α = 0.05

Conclusion: Since p < 0.05, H₀ is rejected. The dataset shows a statistically significant positive relationship between battery capacity and EV range.

#### 2. Welch’s Independent Samples T-Test

This test compares the mean EV range between SUV and Sedan vehicles.
```
H₀: The mean range of SUVs and Sedans is equal.

H₁: The mean range of SUVs and Sedans is different.
```
* SUV mean range: 396.52 km
* Sedan mean range: 496.83 km
* t-statistic: -8.9138
* p-value: 6.77 × 10⁻¹⁴
* Significance level: α = 0.05

Conclusion: Since p < 0.05, H₀ is rejected. The observed mean range differs significantly between SUVs and Sedans in this dataset.

### 🤖 Machine Learning Models

Two regression models were developed:

#### 1. Linear Regression
```
* R² Score: 0.9695
* MAE: 14.43 km
* RMSE: 17.96 km
```
#### 2. Random Forest Regressor
```
* R² Score: 0.9632
* MAE: 14.31 km
* RMSE: 19.73 km
```
### 📊 Model Performance

Model	R² Score	MAE (km)	RMSE (km)
Linear Regression	0.9695	14.43	17.96
Random Forest	0.9632	14.31	19.73

The models were evaluated on the held-out 20% test set (96 records).

### 📁 Project Structure
```
electric-vehicle-data-analysis/
│
├── Data_electric_vehicles.csv
├── electric_vehicle_analysis.ipynb
├── electric_vehicle_data_analysis_report.pdf
├── eda1.png
├── eda2.png
├── eda3.png
├── eda4.png
├── model_results.csv
├── electric_vehicles_cleaned_fixed.csv
└── README.md
```
### 🚀 How to Run

1. Clone the repository
```
git clone https://github.com/your-username/electric-vehicle-data-analysis.git
cd electric-vehicle-data-analysis
```
2. Install dependencies
```
pip install pandas numpy scipy scikit-learn matplotlib
```
3. Run the analysis
```
electric_vehicle_analysis.ipynb
```
### 📌 Conclusion

This project demonstrates a complete data analysis and machine learning workflow using an Electric Vehicle dataset. The analysis includes data cleaning, preprocessing, visualization, statistical hypothesis testing, and EV range prediction using Linear Regression and Random Forest models.

### 👨‍💻 Author

