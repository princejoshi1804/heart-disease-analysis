from pathlib import Path

from src.data_loader import load_heart_disease_data
from src.data_quality import (
    assess_data_quality,
    detect_outliers
)
from src.descriptive_analysis import (
    descriptive_statistics,
    categorical_statistics
)
from src.univariate_analysis import (
    perform_univariate_analysis
)
from src.bivariate_analysis import (
    perform_bivariate_analysis
)
from src.grouping_analysis import (
    perform_grouping_analysis
)
from src.correlation_analysis import (
    perform_correlation_analysis
)
from src.visualizations import (
    create_additional_visualizations
)
from src.findings import (
    generate_key_findings
)


# ============================================================
# PROJECT CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "output"
TABLES_DIR = OUTPUT_DIR / "tables"
VISUALIZATIONS_DIR = OUTPUT_DIR / "visualizations"

TABLES_DIR.mkdir(
    parents=True,
    exist_ok=True
)

VISUALIZATIONS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# MAIN ANALYSIS
# ============================================================

def main():

    print("=" * 60)
    print("HEART DISEASE ANALYSIS")
    print("=" * 60)

    # --------------------------------------------------------
    # 1. Load Dataset
    # --------------------------------------------------------

    df = load_heart_disease_data()

    # --------------------------------------------------------
    # 2. Data Quality
    # --------------------------------------------------------

    assess_data_quality(df)

    numeric_columns = [
        "age",
        "trestbps",
        "chol",
        "thalach",
        "oldpeak",
        "ca"
    ]

    outlier_summary = detect_outliers(
        df,
        numeric_columns
    )

    outlier_summary.to_csv(
        TABLES_DIR / "outlier_summary.csv",
        index=False
    )

    # --------------------------------------------------------
    # 3. Descriptive Statistics
    # --------------------------------------------------------

    summary, additional_statistics = (
        descriptive_statistics(
            df,
            numeric_columns
        )
    )

    summary.to_csv(
        TABLES_DIR / "descriptive_statistics.csv"
    )

    additional_statistics.to_csv(
        TABLES_DIR / "additional_statistics.csv",
        index=False
    )

    categorical_columns = [
        "sex",
        "cp",
        "fbs",
        "restecg",
        "exang",
        "slope",
        "thal",
        "target"
    ]

    categorical_statistics(
        df,
        categorical_columns
    )

    # --------------------------------------------------------
    # 4. Univariate Analysis
    # --------------------------------------------------------

    perform_univariate_analysis(
        df,
        VISUALIZATIONS_DIR
    )

    # --------------------------------------------------------
    # 5. Bivariate Analysis
    # --------------------------------------------------------

    perform_bivariate_analysis(
        df,
        VISUALIZATIONS_DIR
    )

    # --------------------------------------------------------
    # 6. Grouping and Aggregation
    # --------------------------------------------------------

    grouping_results = perform_grouping_analysis(df)

    target_summary = grouping_results[0]
    sex_percentage = grouping_results[1]
    cp_percentage = grouping_results[2]
    exang_percentage = grouping_results[3]

    target_summary.to_csv(
        TABLES_DIR / "target_group_summary.csv"
    )

    sex_percentage.to_csv(
        TABLES_DIR / "sex_target_percentage.csv"
    )

    cp_percentage.to_csv(
        TABLES_DIR / "chest_pain_target_percentage.csv"
    )

    exang_percentage.to_csv(
        TABLES_DIR / "exercise_angina_target_percentage.csv"
    )

    # --------------------------------------------------------
    # 7. Correlation Analysis
    # --------------------------------------------------------

    correlation_matrix, target_correlations = (
        perform_correlation_analysis(
            df,
            VISUALIZATIONS_DIR
        )
    )

    correlation_matrix.to_csv(
        TABLES_DIR / "correlation_matrix.csv"
    )

    target_correlations.to_csv(
        TABLES_DIR / "target_correlations.csv"
    )

    # --------------------------------------------------------
    # 8. Additional Visualizations
    # --------------------------------------------------------

    create_additional_visualizations(
        df,
        VISUALIZATIONS_DIR
    )

    # --------------------------------------------------------
    # 9. Key Findings
    # --------------------------------------------------------

    generate_key_findings(
        df,
        target_correlations
    )

    # --------------------------------------------------------
    # 10. Save Cleaned Dataset
    # --------------------------------------------------------

    df.to_csv(
        OUTPUT_DIR / "heart_disease_cleaned.csv",
        index=False
    )

    # --------------------------------------------------------
    # Finished
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print(
        f"\nCleaned dataset:"
        f"\n{OUTPUT_DIR / 'heart_disease_cleaned.csv'}"
    )

    print(
        f"\nTables:"
        f"\n{TABLES_DIR}"
    )

    print(
        f"\nVisualizations:"
        f"\n{VISUALIZATIONS_DIR}"
    )


if __name__ == "__main__":
    main()