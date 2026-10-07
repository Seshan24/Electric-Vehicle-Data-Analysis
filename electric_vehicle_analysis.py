import pandas as pd, numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df=pd.read_csv("electric_vehicles_spec_2025.csv")
df["cargo_volume_l_num"]=pd.to_numeric(
    df["cargo_volume_l"].astype(str).str.extract(r"(\\d+\\.?\\d*)")[0], errors="coerce"
)

# Cleaning / feature selection
df=df.drop(columns=["cargo_volume_l","source_url","battery_type",
                    "number_of_cells","model","fast_charge_port"])

X=df.drop(columns=["range_km"])
y=df["range_km"]
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.20,random_state=42
)

num_cols=X.select_dtypes(include=np.number).columns.tolist()
cat_cols=X.select_dtypes(exclude=np.number).columns.tolist()

num_pipe=Pipeline([
    ("imputer",SimpleImputer(strategy="median")),
    ("scaler",StandardScaler())
])
cat_pipe=Pipeline([
    ("imputer",SimpleImputer(strategy="most_frequent")),
    ("onehot",OneHotEncoder(handle_unknown="ignore"))
])
pre=ColumnTransformer([
    ("num",num_pipe,num_cols),
    ("cat",cat_pipe,cat_cols)
])

models={
    "Linear Regression":Pipeline([("pre",pre),("model",LinearRegression())]),
    "Random Forest":Pipeline([
        ("pre",ColumnTransformer([
            ("num",SimpleImputer(strategy="median"),num_cols),
            ("cat",Pipeline([
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("onehot",OneHotEncoder(handle_unknown="ignore"))
            ]),cat_cols)
        ])),
        ("model",RandomForestRegressor(
            n_estimators=400,random_state=42,min_samples_leaf=2
        ))
    ])
}

for name,model in models.items():
    model.fit(X_train,y_train)
    pred=model.predict(X_test)
    print(name)
    print("R2:",r2_score(y_test,pred))
    print("MAE:",mean_absolute_error(y_test,pred))
    print("RMSE:",mean_squared_error(y_test,pred)**0.5)

# Hypothesis test 1: Pearson correlation
r,p=stats.pearsonr(df["battery_capacity_kWh"],df["range_km"])
print("H1 Pearson correlation:",r,"p-value:",p)

# Hypothesis test 2: Welch t-test, SUV vs Sedan
suv=df.loc[df["car_body_type"]=="SUV","range_km"]
sedan=df.loc[df["car_body_type"]=="Sedan","range_km"]
t,p=stats.ttest_ind(suv,sedan,equal_var=False)
print("H2 Welch t-test:",t,"p-value:",p)
