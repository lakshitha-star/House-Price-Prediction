# HOUSE PRICE PREDICTION MODEL USING LINEAR REGRESSION
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


os.makedirs("outputs", exist_ok=True)


df = pd.read_csv("data/train.csv")

print("Dataset loaded successfully!")

print("\nFirst five rows:")
print(df.head())

print("\nDataset information:")
df.info()



features = [
    "OverallQual",
    "GrLivArea",
    "GarageCars",
    "TotalBsmtSF",
    "YearBuilt",
    "FullBath",
    "BedroomAbvGr",
    "LotArea"
]

X = df[features]

y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)


model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("regressor", LinearRegression())
])

model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully!")



y_pred = model.predict(X_test)

print("\nActual prices:")
print(y_test.head().values)

print("\nPredicted prices:")
print(y_pred[:5])


r2 = r2_score(y_test, y_pred)

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

print("\n========== MODEL EVALUATION ==========")

print("R2 Score:", round(r2, 4))

print("Mean Absolute Error:", round(mae, 2))

print("Mean Squared Error:", round(mse, 2))

print("Root Mean Squared Error:", round(rmse, 2))


plt.figure(figsize=(8, 5))

plt.scatter(y_test, y_pred, alpha=0.6)

plt.xlabel("Actual House Prices")

plt.ylabel("Predicted House Prices")

plt.title("Actual vs Predicted House Prices")

plt.tight_layout()

plt.savefig("outputs/actual_vs_predicted.png")

print("\nGraph saved successfully!")


results = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})

results.to_csv(
    "outputs/house_price_predictions.csv",
    index=False
)

print("Prediction results saved successfully!")

print("\n========== PROJECT COMPLETED ==========")

print("Linear Regression Model: Successful")

print("House Price Prediction: Successful")

print("R2 Score Evaluation: Successful")

print("Graph Generation: Successful")

print("CSV Export: Successful")

print("\nAll project outputs are saved inside the outputs folder!")
plt.show()