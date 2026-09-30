def generate_key_findings(df, target_correlations):

    print("\n" + "=" * 60)
    print("KEY FINDINGS")
    print("=" * 60)

    total = len(df)

    target_counts = df["target"].value_counts()

    no_disease = target_counts.get(0, 0)
    disease = target_counts.get(1, 0)

    print("\n1. Target Distribution")

    print(
        f"No heart disease: {no_disease} "
        f"({no_disease / total * 100:.2f}%)"
    )

    print(
        f"Heart disease: {disease} "
        f"({disease / total * 100:.2f}%)"
    )

    print("\n2. Average Age")

    age_summary = df.groupby("target")["age"].mean()

    print(
        f"No heart disease: "
        f"{age_summary.get(0):.2f}"
    )

    print(
        f"Heart disease: "
        f"{age_summary.get(1):.2f}"
    )

    print("\n3. Average Cholesterol")

    chol_summary = df.groupby("target")["chol"].mean()

    print(
        f"No heart disease: "
        f"{chol_summary.get(0):.2f}"
    )

    print(
        f"Heart disease: "
        f"{chol_summary.get(1):.2f}"
    )

    print("\n4. Average Maximum Heart Rate")

    heart_rate_summary = (
        df.groupby("target")["thalach"].mean()
    )

    print(
        f"No heart disease: "
        f"{heart_rate_summary.get(0):.2f}"
    )

    print(
        f"Heart disease: "
        f"{heart_rate_summary.get(1):.2f}"
    )

    print("\n5. Correlation with Target")

    print(
        target_correlations.round(3)
    )