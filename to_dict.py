import csv

def to_dict(path):
    index_dict = []
    with open(path) as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',')
        for row in spamreader:
            index_dict.append(row)
    return index_dict

if __name__ == '__main__':
    print to_dict('data.csv')
