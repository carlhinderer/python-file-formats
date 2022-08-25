import csv
import pandas as pd


EXISTING_CSV_FILENAME = 'data/csv/nba_teams.csv'


def read_csv(filename):
    rows = []

    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        fields = next(csv_reader)
        
        for row in csv_reader:
            rows.append(row)

        print('Total number of rows: ', csv_reader.line_num)

    print('Fields: ', fields)
    print('Rows: ', rows)


def read_csv_into_dictionary(filename):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            print(row['city'], row['name'], row['short_name'], row['url_name'])

        print('Total number of rows: ', csv_reader.line_num)


def read_csv_pandas(filename):
    df = pd.read_csv(filename)
    print(df)


if __name__ == '__main__':
    # read_csv(EXISTING_CSV_FILENAME)
    # read_csv_into_dictionary(EXISTING_CSV_FILENAME)
    # read_csv_pandas(EXISTING_CSV_FILENAME)
