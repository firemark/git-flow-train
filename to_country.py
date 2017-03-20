import csv

def to_dict(path):
    index_dict = {}
    with open(path) as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',')
        for row in spamreader:
          #  print row['Common Name'], row['ISO 3166-1 2 Letter Code']
            index_dict[row['Common Name']]=row['ISO 3166-1 2 Letter Code']
    return index_dict

if __name__ == '__main__':
    print to_dict('countries.csv')
