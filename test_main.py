"""
Test goes here

"""
import pandas as pd
import os
from main import main


def test_dataset():
    """
    Test that the dataset is available
    """
    assert os.path.exists("data/instagram_Data.csv")
    # df = pd.read_csv("data/instagram_Data.csv")
    df = pd.read_csv("data/instagram_Data.csv", delimiter=",")
    assert df.shape[0] > 0
    assert df.shape[1] > 0


if __name__ == "__main__":
    test_dataset()
