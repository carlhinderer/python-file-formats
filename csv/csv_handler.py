import csv

EXISTING_CSV_FILENAME = 'data/csv/nba_teams.csv'

NEW_CSV_FILENAME = 'data/csv/nfl_teams.csv'
SAMPLE_FIELDS = ['City', 'TeamName', 'ShortName', 'UrlName']
SAMPLE_DATA = [
                  ['Atlanta', 'Falcons', 'atl', 'atlanta-falcons'],
                  ['Buffalo', 'Bills', 'buf', 'buffalo-bills'],
                  ['Dallas', 'Cowboys', 'dal', 'dallas-cowboys'],
                  ['San Francisco', '49ers', 'sf', 'san-francisco-49ers']
              ]


def read_csv(filename):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        fields = next(csv_reader)
        print('Fields: ', fields)

        for row in csv_reader:
            print('Row: ', row)

        print('Total number of rows: ', csv_reader.line_num)


def write_csv():
    with open(filename, 'w') as csvfile:
        pass


def read_csv_pandas():
    pass

def write_csv_pandas():
    pass


if __name__ == '__main__':
    read_csv(EXISTING_CSV_FILENAME)
