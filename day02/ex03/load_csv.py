import pandas as pd


def load(path: str):
    """Read a CSV file into a pandas DataFrame.

    Prints the dimensions of the loaded dataset as a (rows, columns)
    tuple, then returns the DataFrame. Any error raised while reading
    (missing file, bad path, unreadable format) is caught and None is
    returned instead.

    Args:
        path: Path to the CSV file to read.

    Returns:
        The DataFrame on success, None on any failure.
    """
    try:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        return data
    except Exception:
        return None
