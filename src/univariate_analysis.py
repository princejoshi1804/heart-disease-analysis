import matplotlib.pyplot as plt
import seaborn as sns


def perform_univariate_analysis(df, output_dir):

    print("\n" + "=" * 60)
    print("UNIVARIATE ANALYSIS")
    print("=" * 60)

    plots = [
        ("age", "Distribution of Age", "age_distribution.png"),
        ("trestbps", "Distribution of Resting Blood Pressure",
         "blood_pressure_distribution.png"),
        ("chol", "Distribution of Cholesterol",
         "cholesterol_distribution.png"),
        ("thalach", "Distribution of Maximum Heart Rate",
         "heart_rate_distribution.png"),
        ("oldpeak", "Distribution of Oldpeak",
         "oldpeak_distribution.png")
    ]

    for column, title, filename in plots:

        plt.figure(figsize=(8, 5))

        sns.histplot(
            data=df,
            x=column,
            bins=20,
            kde=True
        )

        plt.title(title)
        plt.xlabel(column)
        plt.ylabel("Frequency")

        plt.tight_layout()
        plt.savefig(
            output_dir / filename,
            dpi=300
        )
        plt.close()

    # Target
    plt.figure(figsize=(7, 5))

    sns.countplot(
        data=df,
        x="target"
    )

    plt.title("Heart Disease Distribution")
    plt.xlabel("Heart Disease")
    plt.ylabel("Number of Patients")

    plt.xticks(
        [0, 1],
        ["No Heart Disease", "Heart Disease"]
    )

    plt.tight_layout()

    plt.savefig(
        output_dir / "target_distribution.png",
        dpi=300
    )

    plt.close()

    print("Univariate analysis completed.")