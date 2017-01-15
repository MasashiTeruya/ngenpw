#! /usr/bin/env python

import argparse
import random
import string

DEFAULT_LENGTH = 12
parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, required=False,
                    help='password length', metavar='N')
args = parser.parse_args()
length = DEFAULT_LENGTH
if args.n:
    length = args.length

ascii = string.ascii_letters
digits = string.digits
special_charactors = '"?!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"'
charactors = ascii + digits + special_charactors
password = ''.join(random.sample(charactors, length))

print(password)
