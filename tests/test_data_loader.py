from src.data_loader import load_data

def test_load_data():
    df = load_data("data/raw/sample.csv")

    assert df is not None