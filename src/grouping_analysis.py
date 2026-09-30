import pandas as pd


def perform_grouping_analysis(df):

    print("\n" + "=" * 60)
    print("GROUPING AND AGGREGATION")
    print("=" * 60)

    numeric_columns = [
        "age",
        "trestbps",
        "chol",
        "thalach",
        "oldpeak"
    ]

    target_summary = df.groupby("target").agg({
        "age": ["count", "mean", "median"],
        "trestbps": ["mean", "median"],
        "chol": ["mean", "median"],
        "thalach": ["mean", "median"],
        "oldpeak": ["mean", "median"]
    })

    print("\nStatistics by heart disease status:")
    print(target_summary)

    sex_target = pd.crosstab(
        df["sex"],
        df["target"]
    )

    print("\nHeart disease by sex:")
    print(sex_target)

    sex_percentage = pd.crosstab(
        df["sex"],
        df["target"],
        normalize="index"
    ) * 100

    print("\nPercentage by sex:")
    print(sex_percentage.round(2))

    cp_target = pd.crosstab(
        df["cp"],
        df["target"]
    )

    print("\nHeart disease by chest pain:")
    print(cp_target)

    cp_percentage = pd.crosstab(
        df["cp"],
        df["target"],
        normalize="index"
    ) * 100

    print("\nPercentage by chest pain:")
    print(cp_percentage.round(2))

    exang_percentage = pd.crosstab(
        df["exang"],
        df["target"],
        normalize="index"
    ) * 100

    print("\nPercentage by exercise-induced angina:")
    print(exang_percentage.round(2))

    return (
        target_summary,
        sex_percentage,
        cp_percentage,
        exang_percentage
    )