import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)

    hours = 24 * 7  # 7 days
    timestamps = pd.date_range(start="2024-01-01", periods=hours, freq="H")

    data = []

    for ts in timestamps:
        hour = ts.hour

        # Base load pattern
        if 9 <= hour <= 17:
            base = 50
        elif 18 <= hour <= 22:
            base = 35
        else:
            base = 20

        noise = np.random.normal(0, 5)
        value = base + noise

        data.append(value)

    df = pd.DataFrame({
        "timestamp": timestamps,
        "actual_kwh": data
    })

    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek

    # Add spikes (waste simulation)
    spike_indices = np.random.choice(df.index, size=5, replace=False)
    df.loc[spike_indices, "actual_kwh"] += 25

    df.to_csv("energy_data.csv", index=False)

    return df
