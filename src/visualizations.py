import matplotlib.pyplot as plt
import seaborn as sns


def create_additional_visualizations(df, output_dir):

    print("\n" + "=" * 60)
    print("ADDITIONAL VISUALIZATIONS")
    print("=" * 60)

    # Age vs Maximum Heart Rate
    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="age",
        y="thalach",
        hue="target"
    )

    plt.title("Age vs Maximum Heart Rate")
    plt.xlabel("Age")
    plt.ylabel("Maximum Heart Rate")

    plt.tight_layout()

    plt.savefig(
        output_dir / "age_vs_heart_rate.png",
        dpi=300
    )

    plt.close()

    # Age vs Cholesterol
    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="age",
        y="chol",
        hue="target"
    )

    plt.title("Age vs Cholesterol")
    plt.xlabel("Age")
    plt.ylabel("Cholesterol")

    plt.tight_layout()

    plt.savefig(
        output_dir / "age_vs_cholesterol.png",
        dpi=300
    )

    plt.close()

    # Pairplot
    columns = [
        "age",
        "trestbps",
        "chol",
        "thalach",
        "oldpeak",
        "target"
    ]

    pairplot = sns.pairplot(
        df[columns],
        hue="target",
        diag_kind="hist"
    )

    pairplot.savefig(
        output_dir / "pairplot.png",
        dpi=300
    )

    plt.close("all")

    print("Additional visualizations completed.")