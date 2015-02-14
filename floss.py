__author__ = 'katherineford'

import csv
import sys
import argparse
floss_list = []

def get_RGB():
    """
    Gets user input of RGB value
    :return:
    """

    # todo: make this work

    return (0,0,0)

def find_floss(red, green, blue):
    """
    Given an RGB value, find the closest DMC floss
    :param red:
    :param green:
    :param blue:
    :return: Floss Number
    """

    # todo: make this work

    input_RGB = (red, green, blue)
    min_distance = sys.maxint
    floss_num = None
    for item in floss_list:
        floss_RGB = (item['Red'], item['Green'], item['Blue'])
        dist = distance_sqrd(input_RGB, floss_RGB)
        if dist < min_distance:
            min_distance = dist
            floss_num = item['Floss#']
    return floss_num

def distance_sqrd(input_RGB, floss_RGB):
    distance_sqrd = (floss_RGB[0]-input_RGB[0])**2 + (floss_RGB[1]-input_RGB[1])**2 + (floss_RGB[2]-input_RGB[2])**2
    return distance_sqrd

def main():
    parser = argparse.ArgumentParser(description='Convert RGB Value to DMC Floss #')
    parser.add_argument('-r', '--red', metavar='Red', type=int, required=True, help='Enter the Red Value:')
    parser.add_argument('-g', '--green', metavar='Green', type=int, required=True, help='Enter the Green Value:')
    parser.add_argument('-b', '--blue', metavar='Blue', type=int, required=True, help='Enter the Blue Value:')
    args = parser.parse_args()


    with open('DMC Floss.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row['Red'] = int(row['Red'])
            row['Green'] = int(row['Green'])
            row['Blue'] = int(row['Blue'])
            floss_list.append(row)
            # print row

    print find_floss(args.red, args.green, args.blue)
    return 0

if __name__ == '__main__':
    exit(main())
