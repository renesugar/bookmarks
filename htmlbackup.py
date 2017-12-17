#!/usr/bin/env python
import os
import argparse
import sys
import datetime

def main():
  parser = argparse.ArgumentParser(description="htmlbackup")
  parser.add_argument("--path", help="Path of the bookmarks file to be scanned")
 
  args = vars(parser.parse_args())

  path = os.path.abspath(os.path.expanduser(args['path']))

  unixtime = int(datetime.datetime.utcnow().strftime("%s"))

  unixtime_str = str(unixtime)

  folder_str = "Bookmarks" + " " + unixtime_str

  with open(path, 'r') as f:
    lines = f.readlines()

    if (len(lines) % 2) != 0:
        # File consists of a title line followed by a URL line for each bookmark
        print("Error: Uneven number of lines in file.\n")
        sys.exit(1);

    print('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n')
    print('<!-- This is an automatically generated file.\n')
    print('     It will be read and overwritten.\n')
    print('     DO NOT EDIT! -->\n')
    print('<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n')
    print('<TITLE>Bookmarks</TITLE>\n')
    print('<H1>Bookmarks Menu</H1>\n')
    print('\n')
    print('<DL><p>\n')

    # Give the folder a unique name
    print('<DT><H3 ADD_DATE="{add_date}" LAST_MODIFIED="{last_modified}">{folder}</H3>\n'.format(add_date=unixtime_str, last_modified=unixtime_str, folder=folder_str))
    print('<DL><p>\n')

    index = 0
    while index < len(lines):
        title = lines[index]
        url = lines[index+1]

        if title == "":
            title = url
        
        print('    <DT><A HREF="{url}" ADD_DATE="{add_date}" LAST_MODIFIED="{last_modified}">{title}</A>\n'.format(url=url, add_date=unixtime_str, last_modified=unixtime_str, title=title))
        index += 2

    print('</DL><p>\n')
    print('</DL>\n')

if __name__ == "__main__":
  main()