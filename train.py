import sys

import os

import pandas as pd
from pathlib import Path
import tomllib

import statsmodels.api as sm

from utils.main_utils import save_model


def main():

    base_path = Path().resolve()
    with open("config.toml", "rb") as f:
        params = tomllib.load(f)

    y_train = pd.read_csv(os.path.join(base_path, "datasets", "train", "labels.csv"))
    X_train = pd.read_csv(os.path.join(base_path, "datasets", "train", "data.csv"))

    model = sm.Logit(y_train, X_train).fit(**params["model_params"])

    summary = save_model(model)
    print(summary)

    sys.exit(0)


if __name__ == "__main__":
    main()
