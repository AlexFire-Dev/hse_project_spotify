import pandas as pd
import argparse

from typing import List, Dict


def open_file(path: str) -> List[List[object]]:
    df = pd.read_csv(path)

    return df.values.tolist()


def get_year_stats(table: List[List[object]]) -> Dict:
    """
    :param table:
    :return: {
        '2010'
    }
    """

    data = {}

    years = [x[1] for x in table]
    set_years = set(years)

    for year in set_years:
        data[str(year)] = 0

    for year in years:
        data[str(year)] += 1

    return data


def get_most_mentioned_artist(table: List[List[object]]) -> str:
    """
    returns
    the most mentioned artist in the dataset
    """

    data = {}

    artists = [x[7] for x in table]
    set_artists = set(artists)

    for artist in set_artists:
        data[str(artist)] = 0

    for artist in artists:
        data[str(artist)] += 1

    name = ''
    maxx = 0

    for artist in set_artists:
        if data[str(artist)] > maxx:
            maxx = data[str(artist)]
            name = artist

    return name


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="our cute spotify experience"
    )

    parser.add_argument(
        "file_path",
        type=str,
        help="input path to the table"
    )

    args = parser.parse_args()

    table = open_file(args.file_path)

    print(get_year_stats(table))
    print(get_most_mentioned_artist(table))
