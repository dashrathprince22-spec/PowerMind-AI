def detect_waste(df):

    df["waste_kwh"] = df["actual_kwh"] - df["predicted_kwh"]

    threshold = 10  # kWh threshold
    df["anomaly"] = df["waste_kwh"].apply(lambda x: 1 if x > threshold else 0)

    total_waste = df[df["anomaly"] == 1]["waste_kwh"].sum()

    money_saved = total_waste * 8
    co2_reduced = total_waste * 0.82

    return df, total_waste, money_saved, co2_reduced
