#! /usr/bin/env python

import argparse
import random
import string

DEFAULT_LENGTH = 12
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', metavar='N', type=int,
                    help='password length',
                    default=DEFAULT_LENGTH)
args = parser.parse_args()
length = args.number

ascii = string.ascii_letters
digits = string.digits
special_charactors = '"?!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"'
charactors = ascii + digits + special_charactors
password = ''.join(random.sample(charactors, length))

print(password)
