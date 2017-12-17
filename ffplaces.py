#!/usr/bin/env python
import os
import argparse
import sys
import json
from pprint import pprint
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

# References:
#
# https://www.blog.pythonlibrary.org/2010/09/10/sqlalchemy-connecting-to-pre-existing-databases/
# https://developer.mozilla.org/en-US/docs/Mozilla/Tech/Places/Database
# https://wiki.mozilla.org/images/d/d5/Places.sqlite.schema3.pdf

class Bookmarks(object):
  pass

def main():
  parser = argparse.ArgumentParser(description="ffplaces")
  parser.add_argument("--path", help="Path of the Places SQLite database file to be scanned")
 
  args = vars(parser.parse_args())

  dbPath = os.path.abspath(os.path.expanduser(args['path']))

  engine = create_engine('sqlite:///%s' % dbPath, echo=False)

  metadata = MetaData(engine)
  moz_places = Table('moz_places', metadata, autoload=True)
  mapper(Bookmarks, moz_places)

  Session = sessionmaker(bind=engine)
  session = Session()

  bookmarks = session.query(Bookmarks).all()

  for bookmark in bookmarks:
    if bookmark.title == None:
      title = ""
    else:
      title = bookmark.title
    url = bookmark.url
    print(title)
    print(url) 

if __name__ == "__main__":
  main()


