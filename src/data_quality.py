import pandas as pd


def assess_data_quality(df):

    print("\n" + "=" * 60)
    print("DATA QUALITY ASSESSMENT")
    print("=" * 60)

    print("\nDataset shape:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nMissing value percentage:")
    print(
        (df.isnull().mean() * 100).round(2)
    )

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nData types:")
    print(df.dtypes)

    print("\nUnique values:")
    for column in df.columns:
        print(f"\n{column}:")
        print(df[column].unique())

    return df


def detect_outliers(df, numeric_columns):

    print("\n" + "=" * 60)
    print("OUTLIER ANALYSIS")
    print("=" * 60)

    results = []

    for column in numeric_columns:

        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[
            (df[column] < lower_bound)
            | (df[column] > upper_bound)
        ]

        results.append({
            "Variable": column,
            "Q1": Q1,
            "Q3": Q3,
            "IQR": IQR,
            "Lower Bound": lower_bound,
            "Upper Bound": upper_bound,
            "Outlier Count": len(outliers)
        })

    return pd.DataFrame(results)