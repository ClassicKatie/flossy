#!/usr/bin/env python
__author__ = 'katherineford'

"""
Copyright 2015
Katherine Ford
All Rights Reserved
"""

import csv
import sys
import argparse
import string
import math
import helpers
from PIL import Image
from jinja2 import Environment, PackageLoader, Template
env = Environment(loader=PackageLoader('floss', 'templates'))

floss_list = []

class Pattern(object):
    def __init__(self, image):
        image = image.convert('RGB')

        # print 'Image size is ', im.size Get the width and height of the image for iterating over

        self.floss_num_chart = []
        self.avail_symbols = list(":,.()-=!@#$%^&*+=?;<>~") + list(string.digits) + list(string.lowercase[::-1]) + list(string.uppercase[::-1])
        self.floss_symbol_map = {}

        for row in range(image.size[0]):
            templist = []
            for col in range(image.size[1]):
                r, g, b = image.getpixel((row,col))
                floss_num = find_floss(r, g, b)[0]
                if floss_num not in self.floss_symbol_map:
                    floss_data = {'symbol': self.avail_symbols.pop(),
                                  'count': 0,
                                  'hex': find_floss(r, g, b)[1],
                                  'text_color': get_text_color(r, g, b)}
                    self.floss_symbol_map[floss_num] = floss_data
                self.floss_symbol_map[floss_num]['count'] += 1
                templist.append(floss_num)
            self.floss_num_chart.append(templist)

    def get_context_data(self):
        return {'floss_symbol_map': self.floss_symbol_map,
                'floss_num_chart': self.floss_num_chart,
                #'image_size': self.image.size()
        }

    def render_HTML(self):
        template = env.get_template('screen.html')
        return template.render(self.get_context_data())

    def get_print_context_data(self):
        page_data = helpers.divide_pattern(self.floss_num_chart, (60, 75))
        new_context = self.get_context_data()
        new_context.update({'divided_pattern': page_data})
        return new_context

    def render_print(self):
        template = env.get_template('print.html')
        return template.render(self.get_print_context_data())

    pass


def get_text_color(red, green, blue):
    bright_sqrd = .299*(red**2) + .587*(green**2) + .114*(blue**2)
    if bright_sqrd <= (130**2):
        return 'FFFFFF'
    else:
        return '000000'


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
            floss_num = item['Floss#'].strip()
            rgb_hex = item['RGB code']
    return floss_num, rgb_hex


def distance_sqrd(input_RGB, floss_RGB):
    distance_sqrd = (floss_RGB[0]-input_RGB[0])**2 + (floss_RGB[1]-input_RGB[1])**2 + (floss_RGB[2]-input_RGB[2])**2
    return distance_sqrd


def main():
    parser = argparse.ArgumentParser(description='''Convert RGB Value to DMC Floss #.  Enter either RGB values or a .csv file''')
    parser.add_argument('-r', '--red', metavar='Red', type=int, required=False, help='Enter the Red Value:')
    parser.add_argument('-g', '--green', metavar='Green', type=int, required=False, help='Enter the Green Value:')
    parser.add_argument('-b', '--blue', metavar='Blue', type=int, required=False, help='Enter the Blue Value:')
    parser.add_argument('-p', '--picture', metavar='Pixellated Image File', required=False, help='Enter path to image, max size 150 x 150 pixels')

    args = parser.parse_args()

    with open('DMC Floss.csv', 'U') as csv_file:
        reader = csv.DictReader(csv_file)
        for row_dict in reader:
            row_dict['Red'] = int(row_dict['Red'])
            row_dict['Green'] = int(row_dict['Green'])
            row_dict['Blue'] = int(row_dict['Blue'])
            floss_list.append(row_dict)
            #print row

    all_args = args.red, args.green, args.blue, args.picture
    color_args = args.red, args.green, args.blue




    if not any(all_args):
        parser.print_help()
        return 1

    elif any(color_args) and not all(color_args):
        parser.print_help()
        return 1

    elif all(color_args):
        print find_floss(args.red, args.green, args.blue)

    elif all(all_args):
        parser.print_help()
        return 1

    elif args.picture:
        im = Image.open(args.picture) #Can be many different formats.
        image_size = im.size

        # if image_size[0] > 150 and image_size[1] > 150:
            # parser.print_help()
            # return 1
        # else:
        my_pattern = Pattern(im)
        with open('renderedchart.html', 'w') as htmlfile:
            htmlfile.write(my_pattern.render_HTML())
        with open('printchart.html', 'w') as htmlfile:
            htmlfile.write(my_pattern.render_print())
            #print my_pattern.render_HTML()


    return 0

if __name__ == '__main__':
    exit(main())
