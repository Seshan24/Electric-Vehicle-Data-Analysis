# Electric Vehicle Data Analysis

## Project Overview

This project analyzes an electric vehicle dataset using Python and machine learning.

The main objective is to clean and preprocess the data, perform exploratory data analysis, test statistical hypotheses, and build machine learning models to predict the driving range of electric vehicles.

## Files

- `Data_electric_vehicles.csv` - Electric vehicle dataset
- `Electric_vehicle_analysis_completed.ipynb` - Completed Jupyter Notebook
- `README.md` - Project documentation

## Tasks Completed

### 1. Data Cleaning

The dataset was checked for:

- Missing values
- Duplicate records
- Incorrect or inconsistent data

Missing numerical values were handled using median imputation.

Duplicate rows were removed.

### 2. Data Preprocessing

The following preprocessing techniques were used:

- One-Hot Encoding for categorical variables
- StandardScaler for numerical features
- Feature selection using SelectKBest
- Train-test data splitting

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

## 3. Exploratory Data Analysis

At least four visualizations were created.

### Visualizations

1. Distribution of Electric Vehicle Range
2. Battery Capacity vs EV Range
3. EV Range by Car Body Type
4. Correlation Heatmap

These visualizations help identify patterns, relationships, distributions, and correlations in the dataset.

## 4. Hypothesis Testing

Two statistical hypothesis tests were performed.

### Test 1 - Pearson Correlation Test

Purpose:

To check whether battery capacity has a significant relationship with electric vehicle range.

**Null Hypothesis (H0):**

There is no significant linear relationship between battery capacity and EV range.

**Alternative Hypothesis (H1):**

There is a significant linear relationship between battery capacity and EV range.

The p-value was used to decide whether to reject or fail to reject the null hypothesis.

### Test 2 - Independent Samples T-Test

Purpose:

To test whether the average driving range of SUVs is significantly different from the average driving range of Sedans.

**Null Hypothesis (H0):**

The mean range of SUVs is equal to the mean range of Sedans.

**Alternative Hypothesis (H1):**

The mean range of SUVs is different from the mean range of Sedans.

The decision was made using a significance level of 0.05.

## 5. Machine Learning Models

The target variable used in this project is:

`range_km`

Because range is a continuous numerical value, regression models were used.

### Models

1. Linear Regression
2. Random Forest Regressor

## Model Evaluation

The models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The model with a higher R² score and lower error values is considered the better model.

## Python Libraries Used

- NumPy
- Pandas
- Matplotlib
- SciPy
- Scikit-learn

## Installation

Install the required libraries using:

```bash
pip install numpy pandas matplotlib scipy scikit-learn jupyter
```

## How to Run

1. Download or clone the project.
2. Keep the CSV file and notebook in the same folder.
3. Open the folder using VS Code or Jupyter Notebook.
4. Open:

```text
Electric_vehicle_analysis_completed.ipynb
```

5. Run the notebook cells from top to bottom.

To start Jupyter Notebook from the terminal:

```bash
jupyter notebook
```

## Project Structure

```text
Electric-Vehicle-Analysis/
│
├── Data_electric_vehicles.csv
├── Electric_vehicle_analysis_completed.ipynb
└── README.md
```

## Conclusion

This project demonstrates a complete machine learning workflow including data cleaning, preprocessing, exploratory data analysis, statistical hypothesis testing, model development, and model evaluation.

The analysis can be used to understand important factors that influence electric vehicle driving range and to build models that predict EV range using vehicle specifications.

---

## 👨‍💻 Authors

**Seshan Rodrigo**

- LinkedIn: [seshan-rodrigo](https://www.linkedin.com/in/seshan-rodrigo-1279ba2b6/)
- GitHub: [Seshan24](https://github.com/Seshan24)

**Heshan Bandara**

- LinkedIn: [heshan-bandara](https://www.linkedin.com/in/heshan-yapa-bandara-aa368a431/)
- GitHub: [Heshan-V]([https://github.com/Seshan24](https://github.com/Heshan-V))
---
