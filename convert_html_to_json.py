#!/usr/bin/env python

import re
import csv
import json
import argparse
import logging
import gzip
import os
import pandas as pd
# import xlrd
# import spacy
import random
import os
import sys
import html2text


from os import listdir
from os.path import isfile, join

logger = logging.getLogger()
logger.setLevel(logging.INFO)
fmt = logging.Formatter('%(asctime)s: [ %(message)s ]', '%m/%d/%Y %I:%M:%S %p')
console = logging.StreamHandler()
console.setFormatter(fmt)
logger.addHandler(console)

parser = argparse.ArgumentParser()

parser.add_argument('input', type=str, default=None,
                    help='Path to folder with html files')

parser.add_argument('--output', type=str, default=None,
                    help='Path to output file')

args = parser.parse_args()

random.seed(9001)

if args.output is None:
    base=os.path.splitext(args.input)[0]
    if base.endswith(".xlsx"):
        base=os.path.splitext(base)[0]
    args.output=base+".json"

logger.info("Output file: "+args.output)


onlyfiles = [f for f in listdir(args.input) if isfile(join(args.input, f))]
logger.info(onlyfiles)


with open(args.output, "w") as f:
    for root, subdirs, files in os.walk(args.input):
        for filename in files:
            if str(filename).endswith(".html") or str(filename).endswith(".htm"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r') as content_file:
                        content = content_file.read()
                        text=html2text.html2text(content)
                        text=text.replace("**"," ")
                        text=text.replace("*"," ")
                        id=str(file_path)
                        base=os.path.basename(args.input)
                        id=id[id.find(base):]
                        logger.info('\t- file %s (full path: %s)' % (filename, id))
                        data = {"id":id , "text": text}
                        json.dump(data, f)
                except UnicodeDecodeError:
                    pass
