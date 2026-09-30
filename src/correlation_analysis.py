import matplotlib.pyplot as plt
import seaborn as sns


def perform_correlation_analysis(df, output_dir):

    print("\n" + "=" * 60)
    print("CORRELATION ANALYSIS")
    print("=" * 60)

    columns = [
        "age",
        "trestbps",
        "chol",
        "thalach",
        "oldpeak",
        "ca",
        "target"
    ]

    correlation_matrix = df[columns].corr()

    print("\nCorrelation matrix:")
    print(correlation_matrix.round(3))

    target_correlations = (
        correlation_matrix["target"]
        .drop("target")
        .sort_values(
            ascending=False
        )
    )

    print("\nCorrelation with target:")
    print(target_correlations.round(3))

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0
    )

    plt.title("Correlation Matrix")

    plt.tight_layout()

    plt.savefig(
        output_dir / "correlation_heatmap.png",
        dpi=300
    )

    plt.close()

    return correlation_matrix, target_correlations