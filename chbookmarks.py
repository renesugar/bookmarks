#!/usr/bin/env python
import os
import argparse
import sys
import json
from pprint import pprint

# https://pythonexample.com/code/parse-chrome-bookmarks-file/

def bookmarklist(path):
    if path['type'] == 'folder':
        for n in path['children']:
            if n['type'] == 'url':
                if n['name'] == None:
                    title = ""
                else:
                    title = n['name']
                print(title)
                print(n['url'])
            elif n['type'] == 'folder':
                for child in n['children']:
                    bookmarklist(child)
    elif path['type'] == 'url':
        if path['name'] == None:
            title = ""
        else:
            title = path['name']
        print(title)
        print(path['url'])

def main():
  parser = argparse.ArgumentParser(description="chbookmarks")
  parser.add_argument("--path", help="Path of the JSON file to be scanned")
 
  args = vars(parser.parse_args())

  jsonPath = os.path.abspath(os.path.expanduser(args['path']))

  with open(jsonPath) as data_file:    
    jsonObject = json.load(data_file)

    roots = jsonObject['roots']
    for root in roots:
        rootObject = roots[root]
        bookmarklist(rootObject)

if __name__ == "__main__":
  main()
