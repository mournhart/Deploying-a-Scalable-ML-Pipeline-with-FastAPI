import pytest
# TODO: add necessary import
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import train_model, compute_model_metrics, inference

# TODO: implement the first test. Change the function name and input as needed

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# Read in the first 60 rows of the file as data for unit testing
data = pd.read_csv("data/census.csv", nrows=60)

train, test = train_test_split(data, test_size=0.2, random_state=20)


def test_model_used_is_rfc():
    """
    # Test that the ML model used is RandomForestClassifier.
    """
    # Your code here
    X_train, y_train, encoder, lb = process_data(
        train,
        categorical_features=cat_features,
        label="salary",
        training=True
    )

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_process_data():
    """
    # Check that the shape of the training data and the labels have the same row count.
    """
    # Your code here
    X_train, y_train, encoder, lb = process_data(
        train,
        categorical_features=cat_features,
        label="salary",
        training=True
    )

    assert X_train.shape[0] == y_train.shape[0]
    assert encoder is not None
    assert lb is not None


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # Check that the model metrics are scores between 0 and 1.
    """
    # Your code here
    X_train, y_train, encoder, lb = process_data(
        train,
        categorical_features=cat_features,
        label="salary",
        training=True
    )

    X_test, y_test, encoder, lb = process_data(
        subset,
        categorical_features=cat_features,
        label="salary",
        training=True,
        encoder=encoder,
        lb=lb
    )

    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)

    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1

