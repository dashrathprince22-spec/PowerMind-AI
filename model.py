import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

def train_model(df):

    df["lag_1"] = df["actual_kwh"].shift(1)
    df["rolling_mean"] = df["actual_kwh"].rolling(3).mean()

    df = df.dropna()

    features = ["hour", "day_of_week", "lag_1", "rolling_mean"]
    target = "actual_kwh"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = XGBRegressor()
    model.fit(X_train, y_train)

    df["predicted_kwh"] = model.predict(X)

    return df
