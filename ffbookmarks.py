#!/usr/bin/env python3
import os
import argparse
import sys
import json
from datetime import datetime, timedelta, timezone
from pprint import pprint

# Decompress Mozilla Firefox bookmarks .jsonlz4 backup files to .json:
# https://github.com/andikleen/lz4json

def bookmarklist(path):
    if path['type'] == 'text/x-moz-place-container':
        if 'children' in path:
            for n in path['children']:
                if n['type'] == 'text/x-moz-place':
                    if n['title'] == None:
                        title = ""
                    else:
                        title = n['title']
                    print(title)
                    print(datetime.utcfromtimestamp(float(n['dateAdded'])/1000000.).strftime('%Y-%m-%d %H:%M:%S.%f'))
                    print(datetime.utcfromtimestamp(float(n['lastModified'])/1000000.).strftime('%Y-%m-%d %H:%M:%S.%f'))
                    print(n['uri'])
                elif n['type'] == 'text/x-moz-place-container':
                    if 'children' in n:
                        for child in n['children']:
                            bookmarklist(child)
    elif path['type'] == 'text/x-moz-place':
        if path['title'] == None:
            title = ""
        else:
            title = path['title']
        print(title)
        print(datetime.utcfromtimestamp(float(path['dateAdded'])/1000000.).strftime('%Y-%m-%d %H:%M:%S.%f')) 
        print(datetime.utcfromtimestamp(float(path['lastModified'])/1000000.).strftime('%Y-%m-%d %H:%M:%S.%f'))        
        print(path['uri'])

def main():
  parser = argparse.ArgumentParser(description="chbookmarks")
  parser.add_argument("--path", help="Path of the JSON file to be scanned")
 
  args = vars(parser.parse_args())

  jsonPath = os.path.abspath(os.path.expanduser(args['path']))

  with open(jsonPath) as data_file:
    for jsonObject in data_file:
        root = json.loads(jsonObject)
        bookmarklist(root)

if __name__ == "__main__":
  main()
