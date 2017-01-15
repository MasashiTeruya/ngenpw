#! /usr/bin/env python

import argparse
import random
import string

DEFAULT_LENGTH = 12
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', metavar='N', type=int,
                    help='password length',
                    default=DEFAULT_LENGTH)
parser.add_argument('-ia', '--ignore-ascii-charactors',
                    action='store_true',
                    help='excludes ascii charactors from being used',
                    default=False)
parser.add_argument('-in', '--ignore-numbers',
                    action='store_true',
                    help='excludes numbers from being used',
                    default=False)
parser.add_argument('-is', '--ignore-special-charactors',
                    action='store_true',
                    help='excludes special charactors from being used',
                    default=False)
args = parser.parse_args()

length = args.number
ignore_ascii_charactors = args.ignore_ascii_charactors
ignore_numbers = args.ignore_numbers
ignore_special_charactors = args.ignore_special_charactors

charactors = ''
if not ignore_ascii_charactors:
    charactors += string.ascii_letters

if not ignore_numbers:
    charactors += string.digits

if not ignore_special_charactors:
    special_charactors = '"?!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"'
    charactors += special_charactors

password = ''.join(random.sample(charactors, length))

print(password)
