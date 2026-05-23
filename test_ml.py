import pytest
# TODO: add necessary import
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed

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
def test_two():
    """
    # add description for the second test
    """
    # Your code here
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
