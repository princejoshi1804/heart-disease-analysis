import matplotlib.pyplot as plt
import seaborn as sns


def perform_bivariate_analysis(df, output_dir):

    print("\n" + "=" * 60)
    print("BIVARIATE ANALYSIS")
    print("=" * 60)

    numerical_variables = [
        ("age", "Age"),
        ("chol", "Cholesterol"),
        ("trestbps", "Resting Blood Pressure"),
        ("thalach", "Maximum Heart Rate"),
        ("oldpeak", "Oldpeak")
    ]

    for column, label in numerical_variables:

        plt.figure(figsize=(8, 5))

        sns.boxplot(
            data=df,
            x="target",
            y=column
        )

        plt.title(
            f"{label} by Heart Disease Status"
        )

        plt.xlabel("Heart Disease")
        plt.ylabel(label)

        plt.xticks(
            [0, 1],
            ["No Heart Disease", "Heart Disease"]
        )

        plt.tight_layout()

        plt.savefig(
            output_dir / f"{column}_vs_target.png",
            dpi=300
        )

        plt.close()

    # Chest pain
    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="cp",
        hue="target"
    )

    plt.title("Heart Disease by Chest Pain Type")
    plt.xlabel("Chest Pain Type")
    plt.ylabel("Number of Patients")

    plt.tight_layout()

    plt.savefig(
        output_dir / "chest_pain_vs_target.png",
        dpi=300
    )

    plt.close()

    # Exercise angina
    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="exang",
        hue="target"
    )

    plt.title(
        "Heart Disease by Exercise-Induced Angina"
    )

    plt.xlabel("Exercise-Induced Angina")
    plt.ylabel("Number of Patients")

    plt.tight_layout()

    plt.savefig(
        output_dir / "exercise_angina_vs_target.png",
        dpi=300
    )

    plt.close()

    # Sex
    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="sex",
        hue="target"
    )

    plt.title("Heart Disease Distribution by Sex")

    plt.xlabel("Sex")
    plt.ylabel("Number of Patients")

    plt.tight_layout()

    plt.savefig(
        output_dir / "sex_vs_target.png",
        dpi=300
    )

    plt.close()

    print("Bivariate analysis completed.")