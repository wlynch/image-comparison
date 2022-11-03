"""Prepare image CVE data for publishing publicly."""

import os

import pandas as pd

from filter_data import filter_df


if __name__ == "__main__":
    df = pd.read_csv(os.environ.get("DATA_URL"))
    filtered_df = filter_df(df)
    filtered_df.to_csv("data.csv", parse_dates=["time"])
    # TODO: Commit and push to main
