import pandas as pd
from scipy.stats import skew, kurtosis


def descriptive_statistics(df, numeric_columns):

    print("\n" + "=" * 60)
    print("DESCRIPTIVE STATISTICS")
    print("=" * 60)

    summary = df[numeric_columns].describe().T

    print("\nBasic statistics:")
    print(summary)

    additional = []

    for column in numeric_columns:

        values = df[column].dropna()

        additional.append({
            "Variable": column,
            "Mean": values.mean(),
            "Median": values.median(),
            "Std Dev": values.std(),
            "Variance": values.var(),
            "Minimum": values.min(),
            "Maximum": values.max(),
            "Skewness": skew(values),
            "Kurtosis": kurtosis(values)
        })

    additional_df = pd.DataFrame(additional)

    print("\nAdditional statistics:")
    print(additional_df)

    return summary, additional_df


def categorical_statistics(df, categorical_columns):

    print("\n" + "=" * 60)
    print("CATEGORICAL STATISTICS")
    print("=" * 60)

    results = {}

    for column in categorical_columns:

        print(f"\n{column}:")
        counts = df[column].value_counts().sort_index()

        print(counts)

        results[column] = counts

    return results