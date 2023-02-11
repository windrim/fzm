from typing import Iterator

from rapidfuzz import fuzz, process


# ON STARTUP: get names to search
import pandas as pd
NAMES = pd.read_csv("data/netflix_titles.csv", usecols=["title"])["title"].tolist()

# Reading in CSV as text:
# https://github.com/Textualize/textual/blob/66d3e571f35ad8cd841afdb8b6b019dac5f4d20f/docs/examples/widgets/table.py
# import io
# import csv
# def get_data():
#     with open("data/netflix_titles.csv", "r") as file:
#         return csv.reader(io.StringIO(file.read()))


def match(s: str) -> list[tuple]:
    """Return matches for some string."""
    # return process.extract(s, NAMES, scorer=fuzz.ratio)
    return [
        (x[0], str(x[1]), str(x[2])) for x in
        process.extract(s, NAMES, scorer=fuzz.partial_ratio)
    ]

def match_iter(s: str) -> Iterator[tuple[str, str, str]]:
    for result in process.extract_iter(s, NAMES, scorer=fuzz.ratio):
        yield result[0], str(result[1]), str(result[2])
