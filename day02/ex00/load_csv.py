import pandas as pd


def load(path: str):
    try:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        return data
    except Exception:
        return None
