import csv

def to_list(path):
    with open(path, 'r') as f:
        headers, *body = csv.reader(f, delimiter=',')
    return headers, body

if __name__ == '__main__':
    print(to_list('data.csv'))
