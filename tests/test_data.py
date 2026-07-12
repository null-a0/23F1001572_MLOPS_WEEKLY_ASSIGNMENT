import pandas as pd

DATA_PATH = "data/iris_data_adapted_for_feast.csv"


def test_dataset_exists():
    df = pd.read_csv(DATA_PATH)
    assert not df.empty, "Dataset is empty."


def test_expected_columns():
    df = pd.read_csv(DATA_PATH)

    expected_columns = [
        "event_timestamp",
        "iris_id",
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species",
        "created_timestamp",
    ]

    assert list(df.columns) == expected_columns


def test_no_missing_values():
    df = pd.read_csv(DATA_PATH)
    assert df.isnull().sum().sum() == 0, "Dataset contains missing values."


def test_feature_dtypes():
    df = pd.read_csv(DATA_PATH)

    assert df["iris_id"].dtype == "int64"
    assert df["sepal_length"].dtype == "float64"
    assert df["sepal_width"].dtype == "float64"
    assert df["petal_length"].dtype == "float64"
    assert df["petal_width"].dtype == "float64"
    assert df["species"].dtype == "object"


def test_value_ranges():
    df = pd.read_csv(DATA_PATH)

    assert df["sepal_length"].between(4.0, 8.0).all()
    assert df["sepal_width"].between(2.0, 5.0).all()
    assert df["petal_length"].between(1.0, 7.5).all()
    assert df["petal_width"].between(0.1, 3.0).all()


def test_species_values():
    df = pd.read_csv(DATA_PATH)

    expected_species = {
        "setosa",
        "versicolor",
        "virginica",
    }

    assert set(df["species"].unique()).issubset(expected_species)