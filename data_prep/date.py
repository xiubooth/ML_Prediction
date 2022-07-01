from global_settings import DATA_PATH
import pickle
import glob
import os


def build_date():
    """Check for dates overlap in the X and y dataframes"""

    X_dates = []
    for file in glob.glob(os.path.join(DATA_PATH, "X", "*.pkl")):
        name = file.split("/")[-1].split(".")[0]
        if "index" not in name:
            X_dates.append(name)

    y_dates = []
    for file in glob.glob(os.path.join(DATA_PATH, "y", "*.pkl")):
        name = file.split("/")[-1].split(".")[0]
        if "index" not in name:
            y_dates.append(name)

    X_dates, y_dates = sorted(X_dates), sorted(y_dates)
    trddt_all = sorted(set(X_dates) & set(y_dates))
    X_unique = sorted(set(X_dates) - set(trddt_all))
    y_unique = sorted(set(y_dates) - set(trddt_all))

    with open(os.path.join(DATA_PATH, "trddt_all.pkl"), "wb") as f:
        pickle.dump(trddt_all, f)

    with open(os.path.join(DATA_PATH, "X_unique.pkl"), "wb") as f:
        pickle.dump(X_unique, f)

    with open(os.path.join(DATA_PATH, "y_unique.pkl"), "wb") as f:
        pickle.dump(y_unique, f)
