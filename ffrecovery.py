#!/usr/bin/env python
import os
import argparse
import sys
import json
from pprint import pprint


def main():
  parser = argparse.ArgumentParser(description="ffrecovery")
  parser.add_argument("--path", help="Path of the JSON file to be scanned")
 
  args = vars(parser.parse_args())

  jsonPath = os.path.abspath(os.path.expanduser(args['path']))

  with open(jsonPath) as data_file:    
    jsonObject = json.load(data_file)
    # https://www.jeffersonscher.com/res/session-extract.html

    windows = jsonObject['windows']
    for window in windows:
        tabs = window['tabs']
        for tab in tabs:
            entries = tab['entries']
            for entry in entries:
                print(entry['title'].encode('utf-8'))
                print(entry['url'].encode('utf-8'))

if __name__ == "__main__":
  main()
