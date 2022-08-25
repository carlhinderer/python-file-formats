import csv
import pandas as pd


NEW_CSV_FILENAME = 'data/output/nfl_teams.csv'
SAMPLE_FIELDS = ['City', 'TeamName', 'ShortName', 'UrlName']
SAMPLE_DATA = [
                  ['Atlanta', 'Falcons', 'atl', 'atlanta-falcons'],
                  ['Buffalo', 'Bills', 'buf', 'buffalo-bills'],
                  ['Dallas', 'Cowboys', 'dal', 'dallas-cowboys'],
                  ['San Francisco', '49ers', 'sf', 'san-francisco-49ers']
              ]

SAMPLE_DATA_DICT = [
    {'City': 'Atlanta', 'TeamName': 'Falcons', 'ShortName': 'atl', 'UrlName': 'atlanta-falcons'},
    {'City': 'Buffalo', 'TeamName': 'Bills', 'ShortName': 'buf', 'UrlName': 'buffalo-bills'},
    {'City': 'Dallas', 'TeamName': 'Cowboys', 'ShortName': 'dal', 'UrlName': 'dallas-cowboys'},
    {'City': 'San Francisco', 'TeamName': '49ers', 'ShortName': 'sf', 'UrlName': 'san-francisco-49ers'}
]


def write_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(SAMPLE_FIELDS)
        csv_writer.writerows(SAMPLE_DATA)


def write_csv_from_dictionary(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=SAMPLE_FIELDS)

        writer.writeheader()
        for entry in SAMPLE_DATA_DICT:
            writer.writerow(entry)


def write_csv_pandas(filename):
    df = pd.DataFrame(SAMPLE_DATA, columns=SAMPLE_FIELDS)
    df.to_csv(filename, index=False)


if __name__ == '__main__':
    # write_csv(NEW_CSV_FILENAME)
    # write_csv_from_dictionary(NEW_CSV_FILENAME)
    write_csv_pandas(NEW_CSV_FILENAME)
