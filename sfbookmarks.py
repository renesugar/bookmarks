#!/usr/bin/env python
import os
import argparse
import sys
import plistlib

def bookmarklist(path):
    if path['WebBookmarkType'] == 'WebBookmarkTypeList':
        if "Children" in path:
            for n in path['Children']:
                if n['WebBookmarkType'] == 'WebBookmarkTypeLeaf':
                    url = n["URLString"]
                    title = n["URIDictionary"]["title"]
                    if title == None:
                        title = ""
                    print(title)
                    print(url)
                elif n['WebBookmarkType'] == 'WebBookmarkTypeList':
                    if "Children" in n:
                        for child in n['Children']:
                            bookmarklist(child)
    elif path['WebBookmarkType'] == 'WebBookmarkTypeLeaf':
        url = path["URLString"]
        title = path["URIDictionary"]["title"]
        if title == None:
            title = ""
        print(title)
        print(url)

def main():
  parser = argparse.ArgumentParser(description="sfbookmarks")
  parser.add_argument("--path", help="Path of the PLIST file to be scanned")
 
  args = vars(parser.parse_args())

  plistPath = os.path.abspath(os.path.expanduser(args['path']))

  with open(plistPath, 'rb') as data_file:
    pl = plistlib.load(data_file)
    bookmarklist(pl)

if __name__ == "__main__":
  main()
