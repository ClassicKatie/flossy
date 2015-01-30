__author__ = 'katherineford'

def main():
    import csv
    floss_list = []
    with open('DMC Floss.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            floss_list.append(row)
    return 0

if __name__ == '__main__':
    exit(main())
