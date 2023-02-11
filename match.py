from rapidfuzz import fuzz, process


# ON STARTUP: get names to search
import pandas as pd
NAMES = pd.read_csv("data/netflix_titles.csv", usecols=["title"])["title"].tolist()


def match(s: str) -> str:
    """Return matches for some string."""
    matches = process.extract(s, NAMES, scorer=fuzz.ratio)
    return "\n".join(x[0] for x in matches)
