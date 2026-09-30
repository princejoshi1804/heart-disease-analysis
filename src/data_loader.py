from ucimlrepo import fetch_ucirepo


def load_heart_disease_data():
    print("Fetching Heart Disease dataset from UCI...")

    heart_disease = fetch_ucirepo(id=45)

    X = heart_disease.data.features
    y = heart_disease.data.targets

    df = X.copy()
    df["target"] = y.iloc[:, 0]

    df.columns = [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal",
        "target"
    ]

    # Convert original target:
    # 0 = No heart disease
    # 1-4 = Heart disease
    df["target"] = (df["target"] > 0).astype(int)

    print("Dataset loaded successfully.")
    print(f"Dataset shape: {df.shape}")

    return df